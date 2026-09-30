#!/usr/bin/env python3
"""Profit per sale for an Etsy + Printify listing, for a French micro-entrepreneur.

Usage examples:
  python3 price_calc.py --price 29 --shipping 5.90 --base 12.74 --ship-cost 5.00
  python3 price_calc.py --price 29 --shipping 5.90 --base 12.74 --ship-cost 5.00 --offsite-ads
  python3 price_calc.py --target-profit 8 --shipping 5.90 --base 12.74 --ship-cost 5.00

All amounts in EUR. Fee rates are the 2026 figures from
research/france_setup_facts.md — re-check them on Etsy/URSSAF before relying on them.
"""
import argparse

# Etsy (France, 2026)
LISTING_FEE = 0.18          # $0.20 per listing/renewal, ~EUR 0.18
TRANSACTION_RATE = 0.065    # on item price + shipping charged to buyer
PROCESSING_RATE = 0.04      # Etsy Payments, France
PROCESSING_FIXED = 0.30
REGULATORY_RATE = 0.0114    # France regulatory operating fee since 22 June 2026
OFFSITE_ADS_RATE = 0.15     # 12% once over $10k/yr sales; capped at $100/order
VAT_ON_ETSY_FEES = 0.20     # charged to sellers without an EU VAT number

# URSSAF micro-entrepreneur, vente de marchandises (2026)
URSSAF_RATE = 0.123
VL_RATE = 0.01              # optional versement liberatoire (income tax)


def breakdown(price, shipping, base, ship_cost, offsite_ads=False, vl=True):
    revenue = price + shipping
    etsy_fees = (
        LISTING_FEE
        + TRANSACTION_RATE * revenue
        + PROCESSING_RATE * revenue + PROCESSING_FIXED
        + REGULATORY_RATE * revenue
    )
    ads = min(OFFSITE_ADS_RATE * revenue, 92.0) if offsite_ads else 0.0
    etsy_vat = VAT_ON_ETSY_FEES * (etsy_fees + ads)
    social = (URSSAF_RATE + (VL_RATE if vl else 0)) * revenue
    printify = base + ship_cost
    profit = revenue - etsy_fees - ads - etsy_vat - social - printify
    return {
        "Buyer pays (item + shipping)": revenue,
        "Etsy fees": -etsy_fees,
        "Offsite Ads": -ads,
        "VAT on Etsy fees (20%)": -etsy_vat,
        "URSSAF" + (" + VL" if vl else ""): -social,
        "Printify (base + shipping)": -printify,
        "Profit": profit,
        "Margin": profit / revenue,
    }


def price_for_profit(target, shipping, base, ship_cost, **kw):
    lo, hi = 0.0, 500.0
    for _ in range(60):
        mid = (lo + hi) / 2
        if breakdown(mid, shipping, base, ship_cost, **kw)["Profit"] < target:
            lo = mid
        else:
            hi = mid
    return hi


def main():
    p = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument("--price", type=float, help="item price shown on Etsy (EUR)")
    p.add_argument("--target-profit", type=float, help="solve for the price giving this profit")
    p.add_argument("--shipping", type=float, default=0.0, help="shipping charged to buyer (EUR)")
    p.add_argument("--base", type=float, required=True, help="Printify base cost (EUR)")
    p.add_argument("--ship-cost", type=float, required=True, help="Printify shipping cost (EUR)")
    p.add_argument("--offsite-ads", action="store_true", help="include a 15%% Offsite Ads fee")
    p.add_argument("--no-vl", action="store_true", help="without versement liberatoire")
    a = p.parse_args()
    kw = dict(offsite_ads=a.offsite_ads, vl=not a.no_vl)

    price = a.price
    if a.target_profit is not None:
        price = price_for_profit(a.target_profit, a.shipping, a.base, a.ship_cost, **kw)
        print(f"Price needed for EUR {a.target_profit:.2f} profit: EUR {price:.2f}\n")
    if price is None:
        p.error("give --price or --target-profit")

    for k, v in breakdown(price, a.shipping, a.base, a.ship_cost, **kw).items():
        print(f"{k:32s} {v:8.1%}" if k == "Margin" else f"{k:32s} {v:8.2f}")


if __name__ == "__main__":
    main()
