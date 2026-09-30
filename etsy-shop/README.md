# Etsy + Printify launch kit (France, illustrated designs)

Goal: a live Etsy shop with 20–30 illustrated listings by early November 2026, in time
for Christmas. Budget under ~€60 before the first sale. Decide after 90 days or 10 sales.

Sources behind every number here:
- `research/france_setup_facts.md`: legal status, fees, product-safety rules, Printify
- `research/niche_shortlist.md`: the 5 ranked niches
- Fee figures come from search extracts, not the official pages. Check them before relying on them.

---

## 0. Pick the niche (do this first)

Recommended launch: **Dackel/Teckel (dachshund) illustrated gifts, German + French first**.
- Best data of the 5: "dackel" ≈165k searches (82% EU) vs ~1.3k Etsy listings.
- Christmas-friendly.
- Mugs, sweatshirts and totes all suit it.

Second collection: **vintage mushroom species plates for French/German foragers**. It peaks in
October, but only works with accurate regional species names.

Queue for November: après-ski / vintage Alpine posters, European garden birds.
See the shortlist for keywords, concepts and IP traps per niche.

One niche per shop at the start. A shop that mixes dachshunds and mushrooms reads as spam.

---

## 1. Admin setup (week 1): order matters

| # | Step | Where | Cost |
|---|------|-------|------|
| 1 | Register as **micro-entrepreneur**, activity "vente de marchandises" (BIC). Required before the first sale. Opt into the *versement libératoire* (1%) if eligible. | formalites.entreprises.gouv.fr | free |
| 2 | Get your SIREN (1–4 weeks). Open a separate bank account. Not mandatory yet, but it keeps things clean. | — | €0–10/mo |
| 3 | **Ask an expert-comptable one question** (see ⚠ VAT below) before choosing print providers. | — | ~€50–100 once |
| 4 | Sign up for a consumer mediator (médiateur de la consommation). This is mandatory. | e.g. CM2C, Medicys | ~€50–150/yr |
| 5 | Create the Printify account (free plan to start; skip Premium at $39/mo until ~15+ orders/month) | printify.com | free |
| 6 | Open the Etsy shop as a **Business** seller. Etsy displays your SIREN and location to EU buyers. | etsy.com/sell | $15–29 setup (not every shop) |
| 7 | In Etsy, fill in: production partner (Printify + provider name, city, country), the EU responsible-person setting (GPSR), shop policies (14-day returns, 2-year legal guarantee), and legal mentions ("EI", address, email, SIREN, mediator) | Etsy shop settings | — |
| 8 | Connect Printify → Etsy. Turn on Printify's **GPSR toggle** in Store Settings. | Printify > Stores | — |

⚠ **VAT when printing from another EU country.** Your VAT exemption (franchise en base, up to
€85,000) covers goods shipped *from France*. If a German or Latvian provider ships to a German
buyer, that sale may be taxable in Germany from the first euro. The €10,000 OSS threshold
applies only to goods dispatched from France. **Get a written answer from an accountant before
launch.** Possible outcomes: use a France-based provider where one exists, or register for the
relevant OSS/IOSS scheme. Never use non-EU providers for EU buyers: since July 2026 small parcels
from outside the EU pay €3 duty, and the parcels are slower.

Rules that apply to every listing:
- Label items **"Designed by"** (never "Handmade").
- Name the production partner in each listing.
- Tick the **AI disclosure** and mention it in the description (template below).
- Returns: POD designs from your catalog are *not* exempt from the 14-day withdrawal right.
  Only genuinely personalised items are.

---

## 2. Order samples (week 1–2)

Order 1 mug + 1 sweatshirt/tee + 1 tote from your chosen EU provider, at base cost via
Printify > Create order > Sample (≈€35–50 total).
- Check print sharpness, colours on the actual fabric, and delivery time.
- The samples also give you **real product photos**, which beat mockups for conversion.

---

## 3. Design workflow (repeat per design, ~30–45 min each)

1. **Brief with Claude.**
   - Give it the niche file and ask for 10 concepts, each with a one-line hook, target buyer, product and occasion.
   - Keep the 3–4 you like. Claude checks them against the IP traps list.
2. **Generate with a paid image tool.**
   - Midjourney Basic (~$10/mo) or Ideogram. Free tiers aren't licensed for commercial use.
   - Ask Claude to write the prompts in one consistent house style, so the shop looks like one artist.
   - Example direction for the dachshund line: *"loose ink-and-watercolour illustration, limited 3-colour palette, cream background"*.
3. **Edit by hand (this is what makes the design yours).**
   - Fix anatomy and paws, simplify, and recolour to the shop palette.
   - Add hand-lettered or typeset text (German/French pun, breed name).
   - Remove the background.
   - Tools: Photopea (free), Affinity, or Procreate.
   - The human edit is also your only route to copyright protection.
4. **Prepare print files.**
   - Transparent PNG at 300 DPI at the provider's print size (check each product's template in Printify).
   - Upscale if needed.
5. **Check trademarks.**
   - Search every text element on **EUIPO eSearch** and **INPI** (and USPTO if you sell to the US).
   - Skip anything that's a registered mark in the relevant class (25 = clothing, 21 = mugs).
6. **Mock up and publish from Printify.** Always edit in Printify, never in Etsy, or orders stop routing.

Target: 5 designs × 3–5 products each ≈ 20–30 listings by early November.

---

## 4. Listing template

Have Claude draft each listing in **FR + DE + EN**, then fix the translations yourself.
Etsy's auto-translation is weak and German buyers notice.

```
TITLE (≤140 chars, main keyword first, no keyword stuffing)
  Dackel Tasse Weihnachten – Aquarell Illustration, Geschenk für Dackel Liebhaber

TAGS (13, ≤20 chars each, long-tail phrases buyers type)
  dackel tasse | dackel geschenk | teckel mug | dackel weihnachten | ...

DESCRIPTION
  [1–2 lines: who it's for / the occasion]
  [Design story: 1 line in your own voice]
  Product: [material, size, dishwasher/microwave safe, care]
  Made to order by our print partner [Provider], [City, Country]. Ships in X–Y business days.
  Design: illustrated by me, created with the help of AI image tools and finished by hand.
  Returns: 14-day withdrawal right; 2-year legal guarantee of conformity.
```

Claude prompt to reuse:
> Here is my niche file and a design description: [paste]. Write an Etsy listing in German,
> French and English: a title under 140 chars with the main keyword first, 13 tags of ≤20 chars
> (long-tail, no trademarks), and a description following my template. Flag any word that might
> be a trademark.

---

## 5. Price it

Use `tools/price_calc.py`. Worked example: a mug at €24 + €4.90 shipping, with a €6.50 base and
€6.00 Printify shipping, leaves **€7.94 profit (27%)** after:
- Etsy fees
- 20% VAT on Etsy's fees
- URSSAF + versement libératoire

Put in your real base and shipping costs from Printify's EU provider.

```
python3 tools/price_calc.py --price 24 --shipping 4.90 --base 6.50 --ship-cost 6.00
python3 tools/price_calc.py --target-profit 8 --shipping 4.90 --base 6.50 --ship-cost 6.00 --offsite-ads
```

Rules of thumb:
- Aim for ≥€7 profit per item *without* ads.
- Offsite Ads (15%) can turn a mug unprofitable, which is the reason for the second command above.
- Price in round euros.
- Offer free shipping on posters/totes only if the math still works.

---

## 6. Traffic (from week 1, not after)

Etsy search alone is slow for a new shop. The Merch-style lesson applies here too: shops that
bring outside traffic win.
- **Pinterest**: pin every design (FR/DE boards). This is the highest-ROI free channel for illustration.
- **Instagram/TikTok**: short "sketch → finished mug" process clips. These prove human work and build trust.
- Dachshund owner groups and forums, only where self-promotion is allowed.
- Hold off on Etsy Ads until you have ~5 organic sales. Then run €1–2/day on your best listing only.

---

## 7. Budget to first sale

| Item | Cost |
|------|------|
| Micro-entrepreneur registration | €0 |
| Etsy setup fee (if charged) | ~€15–27 |
| 25 listings × $0.20 | ~€5 |
| Image tool, 1 month | ~€10 |
| Samples | ~€35–50 |
| Mediator | ~€50–150/yr (can't skip) |
| Accountant question | ~€50–100 (strongly advised) |

---

## 8. Scorecard: decide on day 90

Track weekly in a sheet:
- listings live
- views
- favourites
- orders
- conversion (orders/visits)
- profit

- **Keep going**: ≥10 sales, or conversion ≥1% with rising views. Add the next niche collection.
- **Pivot**: views but no sales. The problem is price, photos or product choice, so change those first.
- **Stop or change niche**: fewer than ~100 views/month after 25+ listings and active Pinterest.
