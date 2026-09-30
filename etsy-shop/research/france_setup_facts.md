# France setup facts: Etsy + Printify POD shop selling mostly to EU customers

Research date: 2026-09-30.

**How this was checked.** The sandbox's egress proxy blocked direct page fetches from etsy.com, printify.com, service-public, economie.gouv.fr and valueaddedresource.net. Every fact below therefore comes from web-search result extracts of the cited pages, not from reading the pages first-hand. Before you rely on a number (especially fees and prices), open the cited official page and check it.

Status tags used below:
- **[OK]**: several consistent sources, or an official source seen in search.
- **[CHECK]**: one or secondary source only, or sources disagree.
- **[OLD]**: the source is dated before 2025.
- **[INTERP]**: my own legal reading, not taken from a source.

---

## 1. French legal status: micro-entrepreneur (entreprise individuelle, micro regime)

### Registration
- **Where:** all business formalities go through the single online portal (guichet unique) run by INPI at https://formalites.entreprises.gouv.fr. It replaced the old CFE (centres de formalités des entreprises) networks on 2023-01-01, and the business is entered in the RNE (national business register). [OK]
  Sources: https://www.rocketlawyer.com/fr/fr/entreprise/creation-d-entreprise/guide-juridique/guichet-unique-ce-qui-change-au-1er-janvier-2023, https://unec.fr/wp-content/uploads/2022/12/2022-12-20-guichet-unique.pdf [OLD, but the rule is unchanged]
- **Is registration required before the first sale? Yes.** Buying POD goods to resell them to Etsy buyers on a regular basis is a commercial activity (acte de commerce), and formalities must be done when the activity starts. Selling habitually without registering can count as travail dissimulé (dissimulation d'activité). Income is taxable from the first euro. [OK]
  Sources: https://www.keobiz.fr/le-mag/doit-on-creer-une-entreprise-pour-vendre-en-ligne/, https://propulsebyca.fr/vendre-creations/etsy
- **Cost:** creating a micro-entreprise on the guichet unique is generally free. [CHECK: the search results did not state this explicitly, so confirm on the portal.]

### Activity classification
- **POD resale counts as "vente de marchandises" (achat-revente), taxed as BIC (bénéfices industriels et commerciaux).** You buy the finished item from Printify and resell it. The micro-BIC flat allowance (abattement) for sales is 71%. Declare it as e-commerce / vente à distance of goods; the likely APE code is 47.91B (vente à distance sur catalogue spécialisé), which INSEE assigns. [OK for BIC-vente; CHECK for the APE code, which no source confirmed.]
  Sources: https://lamicrobyflo.fr/les-categories-dactivite-en-micro-entreprise/, https://www.entreprises.cci-paris-idf.fr/web/formalites/micro-entrepreneur-bic-ou-bnc

### Social contributions (cotisations) in 2026
- **Achat-revente de marchandises: 12.3% of turnover collected (CA encaissé), unchanged on 2026-01-01.** Only the liberal-profession (BNC) rate changed, to 25.6%. [OK]
  Sources: https://www.lecoindesentrepreneurs.fr/taux-cotisations-sociales-2026-micro-entrepreneur/, https://abby.fr/guide/micro-entreprise/cotisations-sociales-auto-entrepreneur, https://www.portail-autoentrepreneur.fr/academie/statut-auto-entrepreneur/changements-2026-auto-entrepreneurs
  - [CHECK] One search summary claimed the 2026 rate was 13.1%. That contradicts most sources. The 12.3% figure is the consensus, but confirm it on https://www.autoentrepreneur.urssaf.fr or https://www.economie.gouv.fr/entreprises/micro-entreprise-auto-entreprise-charges-sociales (updated 2026-03-06).
- On top of this there is a small CFP (contribution à la formation professionnelle), about 0.1% of turnover for traders. [CHECK: not confirmed in 2026 results.]
- ACRE (a first-year contribution reduction) may apply. [CHECK: not researched here.]

### Versement libératoire (optional flat-rate income tax)
- **Rate for sales of goods: 1% of turnover**, paid monthly or quarterly with the cotisations. [OK]
- **Eligibility:** the household's revenu fiscal de référence for N-2 (the 2024 income tax notice, for 2026) must be at most **€29,315 per part** (the figure given for a single person). [OK]
  Sources: https://wisestart.fr/guides/fiscalite/taux-versement-liberatoire-2026/, https://www.economie.gouv.fr/entreprises/micro-entrepreneur-auto-entrepreneur-declaration-revenus (updated 2026-03-23)
- **When to opt:** at creation, or by 30 September to apply from the next 1 January. [CHECK: this is standard, but not re-verified for 2026.]

### Turnover ceilings (plafonds) for the micro regime, 2026–2028
- **Sales (vente/hébergement): €203,100**, up from €188,700. Services: €83,600. These are revalued every three years. You stay in the regime unless you exceed the ceiling two years in a row. [OK]
  Sources: https://www.entreprises.cci-paris-idf.fr/actualites/micro-entrepreneur-revalorisation-des-seuils-pour-2026-2028, https://www.legifiscal.fr/actualites-fiscales/4436-nouveaux-seuils-micro-entreprises-annee-2026.html, https://propulsebyca.fr/actualites/nouveaux-plafonds-chiffre-affaires-2026-micro-entreprise

### VAT exemption threshold (franchise en base de TVA) in 2026: what actually applies
- **Background of the reform debate.** The 2025 Finance Law set a single €25,000 threshold from 2025-03-01. After protests, it was suspended until 2025-12-31. **Law no. 2025-1044 of 3 Nov 2025 then repealed the €25,000 single threshold for good** and kept the earlier thresholds. The draft 2026 Finance Law (PLF 2026, article 25) proposed a single €37,500 threshold, but Parliament deleted it. [OK]
  Sources: https://www.legifiscal.fr/actualites-fiscales/4317-promulgation-loi-stabilisant-seuils-franchise-base-tva.html, https://www.labase-lextenso.fr/breves/franchise-en-base-de-tva-suppression-du-seuil-unique-d-exoneration-BREVEBO141, https://www.publicsenat.fr/actualites/economie/auto-entrepreneurs-le-senat-rejette-la-modification-des-seuils-dexemption-de-tva-dans-le-budget-2026, https://bpifrance-creation.fr/entrepreneur/actualites/plf-2026-franchise-base-tva-annoncee-a-37-500-eu
- **Thresholds in force in 2026 for sales of goods: €85,000** (previous calendar year) **and €93,500** (current-year tolerance). Services: €37,500 and €41,250. [OK]
  - Some older articles quote €91,900/€101,000. Those are the pre-2025 figures and are no longer valid.
- **Invoice wording.** Invoices must say "TVA non applicable, art. 293 B du CGI". According to one source, **from 2026-09-01 the reference becomes "art. L. 223 et s. du CIBS"**, and the old wording is accepted until 2027-12-31. [CHECK: single source]
  Source: https://www.legalstart.fr/fiches-pratiques/autoentrepreneur/mention-obligatoire-facture-autoentrepreneur/

### VAT trap specific to POD for EU buyers [INTERP; ask an accountant]
- The French franchise en base covers only supplies taxable in France. For B2C distance sales within the EU there is a €10,000 EU-wide threshold (the OSS regime). Below it, French rules apply; above it, the buyer country's VAT is due, declared through the OSS portal on impots.gouv.
  Sources: https://www.impots.gouv.fr/professionnel/suis-je-concerne-0, https://www.fiducial.fr/Relations-commerciales/Prix-de-vente-facturation/E-commerce-Evolution-de-la-TVA-sur-les-ventes-a-distance-au-1er-juillet-2021
- **The €10,000 threshold only applies when goods are shipped from the member state where the seller is established.** Printify orders are often printed and shipped from Germany, Latvia, Czechia, Spain and so on. Goods leaving another member state do not qualify. They may make destination-country VAT due from the first sale (usable via OSS), and a sale where goods are delivered inside the provider's own country can be a domestic supply in that country, which may require local VAT registration. Secondary sources warn that goods "shipped from a warehouse in another member state require local VAT registration in addition to OSS". [CHECK]
  Sources: https://www.hr-associes.fr/blog/tva-dropshipping, https://www.superindep.fr/blog/2026/tva-ecommerce-autoentrepreneur/, https://www.info-ecommerce.fr/tva-ecommerce-europe-oss-seuil-10000-ventes-distance/
- **Practical consequence.** This is the biggest open compliance question. **Get written advice from an expert-comptable** before choosing between an FR-only print provider and multiple EU providers. The EU cross-border SME scheme (the "SME-EX", from 2025-01-01) was not researched here.

### Bank account
- **A dedicated account is required only once turnover exceeds €10,000 for two consecutive calendar years** (art. L613-10 CSS). You then have 12 months to open one. It can be a separate personal account; a "compte pro" is not required. There is no specific fine. [OK]
  Sources: https://entreprendre.service-public.gouv.fr/vosdroits/F35991, https://lamicrobyflo.fr/le-compte-bancaire-en-micro-entreprise/
  - [CHECK] The research summary cited "article L. 613-7 CSS". I believe L613-10 is correct (codified in the Code de la sécurité sociale, CSS); verify the article number.
- Recommended anyway, so Etsy payouts are easy to reconcile.

### CFE (cotisation foncière des entreprises)
- Exempt in the calendar year the business is created.
- 50% reduction on the tax base in the second year.
- Fully exempt in any year where turnover is at most €5,000 over 12 months.
- Otherwise a minimum amount set by the commune applies: roughly €250–€1,194 for the €10,001–€32,600 turnover bracket.
- The first-year declaration 1447-C-SD is due by 31 December of the creation year. [CHECK: date not re-verified]
- [OK/CHECK]: the amount ranges come from a secondary source.
  Sources: https://www.legalstart.fr/fiches-pratiques/fiscalite-entreprises/exoneration-cfe/, https://www.legalplace.fr/guides/cfe-micro-entreprise-domicile/

---

## 2. Etsy for a France-based seller

| Fee | Amount | Status and source |
|---|---|---|
| Shop setup fee | One-time, non-refundable, **$15–$29 depending on country**. Rolled out gradually since 2024; not every new shop is charged, and Etsy shows it during onboarding. | [CHECK] https://help.erank.com/fr/blog/comprendre-les-frais-dinstallation-detsy/, https://litcommerce.com/blog/how-much-does-it-cost-to-start-an-etsy-shop/ |
| Listing fee | **$0.20** per listing for 4 months, also charged again when an item sells (auto-renew). Billed in USD and converted to the billing currency; the EUR amount varies. | [OK] https://printify.com/blog/how-much-does-etsy-take-per-sale/ |
| Transaction fee | **6.5%** of item price + shipping + gift wrap | [OK] same source; https://crosslist.com/blog/etsy-review |
| Payment processing (France) | **4% + €0.30** per order | [OK] https://help.etsy.com/hc/articles/115015628847 |
| Regulatory operating fee (France) | **1.14% since 2026-06-22** (was 0.47%), on item + shipping + gift wrap | [OK, secondary sources only] https://www.geekseller.com/blog/etsy-announces-regulatory-operating-fee-increase-in-uk-france-and-italy/, https://www.growtsy.com/etsy-fees/regulatory-operating-fee, https://iscompliant.app/Blog/etsy-regulatory-fee-2026 |
| Offsite Ads | **15%** per attributed sale if the shop made under $10k in the last 12 months (opt-out allowed); **12%** and mandatory at $10k or more. **Capped at $100 per order.** 30-day attribution window. | [OK] https://www.outfy.com/blog/etsy-offsite-ads/, https://checkoutpage.com/blog/etsy-fees |
| Currency conversion | 2.5% if the listing currency differs from the payment account currency. Avoid it by listing in EUR. | [CHECK: 2025/2026 source not found] |
| VAT on Etsy's fees | France charges **20% VAT on Etsy's seller fees**. Etsy does not charge it if you submit a valid VAT ID (reverse charge). A micro-entrepreneur in the franchise normally has no active intra-EU VAT number, so **expect 20% on top of the fees**. | [OK] https://printify.com/blog/how-much-does-etsy-take-per-sale/, https://help.etsy.com/hc/en-us/articles/11766287905303-How-Tax-Laws-Affect-Etsy-Sellers-Around-the-World |

**Rough total on a €25 order, before Offsite Ads:** 6.5% + 1.14% + 4% + €0.30 + $0.20 ≈ 11.6% + about €0.48, plus 20% VAT on the fees. [INTERP]

- **Etsy Payments / payouts.** France is eligible for Etsy Payments, with payouts in EUR to your bank account. You can choose daily, weekly (the default for new sellers), biweekly or monthly deposits. New sellers may have reserves or holds. [OK/CHECK]
  Sources: https://help.etsy.com/hc/articles/115015710408, https://app.craftybase.com/blog/understanding-your-etsy-payment-account
- **Etsy as marketplace facilitator for EU VAT.** Etsy collects VAT on **digital** items for all sellers, and **import VAT on physical goods up to €150 shipped into the EU from outside the EU**. **For an EU-based seller (FR) selling physical goods to EU buyers, Etsy does NOT collect or remit VAT; you remain responsible** (franchise en base in FR, OSS, or local registration, as discussed in section 1). [OK]
  Sources: https://www.bontello.com/en/blog/eu-vat-etsy-sellers-2026, https://help.etsy.com/hc/en-us/articles/360000337247-Custom-Fees-and-Physical-VAT-Collection, https://linkmybooks.com/blog/etsy-vat
- **New EU customs item (for awareness).** From 2026-07-01 to 2028-07-01, a **flat €3 customs duty** applies to low-value (≤€150) parcels entering the EU from outside it. This only matters if you route orders to non-EU (US/UK) Printify providers. Printify handles it via IOSS. [CHECK]
  Source: https://printify.com/blog/eu-customs-duty/
- **DAC7 / French platform reporting.** Etsy reports seller identity (tax ID, address, bank account) and sales data to the French tax authority (DGFiP) when you have **≥30 sales or ≥€2,000** in a calendar year. You must be under both limits to be excluded. Etsy also sends French sellers an annual summary (art. 242 bis CGI). [OK]
  Sources: https://help.etsy.com/hc/en-us/articles/360048262494-What-Are-Sales-Reporting-Requirements-for-French-Sellers, https://beancount.io/blog/2026/07/13/dac7-us-online-sellers-eu-customers-reporting-guide
- **Trader / business status.** Register as a Business on Etsy's Legal and Tax page. Etsy then shows EU buyers your trader status, business registration number (SIREN) and business location, plus the address if different from home, under the EU Omnibus Directive and the Digital Services Act (DSA). [OK]
  Source: https://help.etsy.com/hc/articles/5703129136407

---

## 3. EU General Product Safety Regulation (GPSR, Regulation (EU) 2023/988, applicable since 2024-12-13)

### What each Etsy listing needs for EU buyers
- **Manufacturer** name, postal address and electronic contact.
- **EU Responsible Person** (an EU-based economic operator) name, address and contact.
- **Safety information** (warnings and instructions, care) in the language of the buyer's country.
- A product identifier (type, batch or model).
- Non-compliant listings can be removed, and repeated problems can lead to suspension of EU sales. [OK]
  Sources: https://help.etsy.com/hc/en-in/articles/28211364687383-What-is-the-General-Product-Safety-Regulation-GPSR, https://craftybase.com/blog/what-is-gpsr, https://listadum.com/blog/understanding-the-general-product-safety-regulation-gspr-what-etsy-sellers-need-to-know

### How Etsy's GPSR fields work
- The listing editor has **manufacturer** and **responsible person** fields.
- Since **April 2025** you can set the responsible person **shop-wide**, so it applies to all EU-facing listings.
- Etsy lists Cert-Rep and International Associates as partners who offer paid responsible-person services. **A French seller does not need one: you are EU-established.** [OK / INTERP]
  Source: https://craftybase.com/blog/what-is-gpsr

**Who fills which role [INTERP].** Under GPSR art. 3(8), a person who sells a product under their own name or trademark is treated as the manufacturer. A French micro-entrepreneur selling under their brand can therefore list:
- **themselves** as manufacturer and responsible person (EU address), or
- Printify's EU affiliate as responsible person.

In both cases the product safety information supplied by Printify must appear.

### How Printify supports GPSR
- Turn on **GPSR in Printify Store Settings**. Printify then adds the responsible-person details, mandatory product details and the 2-year EU legal warranty text to each listing's description.
- Printify supplies the product data per product: identification, country of origin, compliance details, age restrictions, handling or care instructions, warnings.
- If you have no EU address, you can use **Printify's EU affiliate contact details**. The EU legal representative on Printify's imprint page is **SIA "Printify Development", Raina bulvāris 25, Riga, LV-1050, Latvia**.
- For Etsy specifically, you still enter the EU economic operator in Etsy's own GPSR fields, using either Printify's default details or your own EU address.
- On defects: **Printify covers the first 30 days; after that the seller owes the buyer a refund or replacement under the 2-year legal guarantee.** [OK]
  Sources: https://help.printify.com/hc/en-us/articles/30680459082385, https://help.printify.com/hc/en-us/articles/30680548875025-How-do-I-make-my-products-compliant-with-the-GPSR-requirements, https://help.printify.com/hc/en-us/articles/30962618803345-How-do-I-add-GPSR-details-to-my-sales-channels, https://help.printify.com/hc/en-us/articles/31043082008465-Will-the-GPSR-business-information-be-visible-to-my-customers, https://printify.com/legal-imprint/

---

## 4. Printify for EU sellers

### EU print providers (names from third-party lists; confirm in the catalog)
| Provider | Location |
|---|---|
| Atelier Katanga | France |
| Textildruck Europa | Halle, Germany (ships via Deutsche Post, DPD, DHL, Asendia) |
| Posterflow | Germany |
| OPT OnDemand | Czech Republic |
| Ideju Druka, Drukātava, Print Pigeons | Latvia |
| LaTostadora | Spain |
| Flexmerch, HFT71 | Poland |
| Rogac | Slovenia |
| Print Clever, Eco Print Partner, Harrier | UK (non-EU, so the €3 duty and IOSS apply for EU buyers) |

[CHECK: Printify's own pages confirm providers in DE, CZ, PL and LV; the France listing comes from a third-party list.]
Sources: https://printify.com/print-on-demand/europe/, https://printify.com/shipping-rates/textildruck-europa/, https://merchize.com/print-on-demand-in-eu/, https://dodropshipping.com/best-print-on-demand-suppliers-in-europe/, https://printify.com/print-on-demand/france/

### Typical base costs (catalog "from" prices shown in EUR)
These are the cheapest provider for each product, **not necessarily an EU provider**; EU providers are often higher. [CHECK: all figures come from indexed catalog snippets, undated.] Printify bills seller accounts in USD.

| Product | Free plan | Premium |
|---|---|---|
| Stanley/Stella Creator 2.0 tee (EU-made organic cotton) | from €12.74 | €9.41 |
| Bella+Canvas 3001 | about $10.98 (≈ €9.4) | $8.77; range across providers $8.50–$13 [CHECK, secondary source, 2025] |
| 11 oz ceramic mug | from €4.29 | €3.20 |
| 11 oz white ceramic mug (other listing) | from €7.40 | €5.52 |
| 11 oz accent mug | €5.44 | €4.04 |
| Tote bag ("Bestseller Tote") | €10.77 | €8.05 |
| Poster | €5.55 | €4.02 |
| Polyester doormat | €11.13 | €8.06 |

Sources: https://printify.com/app/brand/15/stanley-stella, https://printify.com/app/products/home-decor, https://podvector.ai/articles/printify/costs-and-charges/printify-bella-canvas-3001-base-cost-2025-full-breakdown-for-pod-sellers

### Shipping (EU provider to EU buyer)
- A tee from an EU provider costs about **$5.49+ for the first item** and about **$1.50–$2.50 for each additional item**. For comparison, US to EU is about $12–18.
- Mugs cost more; a US provider to "Rest of World" is $21.19 for the first mug.
- **No reliable EU per-provider EUR table was retrievable.** Read the exact rates on each product's "Shipping" tab or at https://printify.com/shipping-rates/ (for example /textildruck-europa/). [CHECK]
  Sources: https://chayaani.com/blog/printify-shipping-costs-delivery-times-2026, https://help.printify.com/hc/en-us/articles/4483608897041-How-much-does-shipping-cost

### Production and delivery times
- Production is typically **2–5 business days** (up to 7).
- Delivery within the EU is **2–5 business days**, so expect **about 4–10 business days** in total.
- There are no customs charges on intra-EU fulfilment. [OK]
  Sources: https://help.printify.com/hc/en-us/articles/4483629751825-What-are-Printify-s-production-times-like, https://printify.com/cpc/cpc_nb_selling_made_simple_pod_europe/

### Printify Premium
- **$39/month on monthly billing since 2026-02-17** (was $29).
- **$299/year on annual billing**, about $24.99/month.
- Benefits: **up to 20% off most catalog products**, up to 33% off selected new products, plus mentorship (Sellers Club) and tools. [OK]
  Sources: https://help.printify.com/hc/en-us/articles/42641734110225-What-s-changing-with-the-Printify-Premium-plan-in-February-2026, https://printify.com/blog/new-printify-premium/
- **Break-even [INTERP]:** at about $2 saved per item, the monthly plan pays off at roughly 20 orders a month.

### Etsy integration
1. **Connect:** Printify dashboard → My Stores → Connect → Etsy, then authorize with OAuth.
2. **Publish:** design the product in Printify and click Publish. The listing, variants, prices and mockups are pushed to Etsy, and Printify creates and assigns its own shipping profiles.
3. **Orders:** Printify imports Etsy orders automatically; they sync periodically, and there is a manual "Sync" button under Orders. Printify routes orders to the chosen provider and pushes tracking numbers back to Etsy. Order approval can be manual or automatic (Store Settings).
4. **Best practice:** edit variants, prices and shipping in Printify, not directly on Etsy. Editing on Etsy breaks the link and orders will not route. [OK]
   Sources: https://help.printify.com/hc/en-us/articles/4483617508241-How-can-I-integrate-my-Etsy-shop, https://help.printify.com/hc/en-us/articles/36917933972881, https://printify.com/knowledge-hub/etsy-print-on-demand-sync-errors/, https://help.printify.com/hc/en-us/articles/4483625253265

### Samples
- Go to My Products or Orders → Create order → **Sample**. Your account address is filled in automatically.
- You pay base cost plus shipping. **There is no separate sample discount**, but Premium prices apply. [OK]
  Source: https://help.printify.com/hc/en-us/articles/4483617804689

---

## 5. Legal mentions and consumer rules for a French/EU e-seller, plus Etsy disclosures

### Mentions légales
- The LCEN applies (art. 1-1 in the numbering after the SREN law of 21 May 2024; formerly art. 6-III).
- Required details for an individual entrepreneur: surname, first name + **"EI" or "Entrepreneur individuel"** (mandatory since 2022-05-15 on all documents and invoices), address, email, phone, **SIREN / RNE number**, and the VAT number if you have one.
- For B2C sales you must also show the name and contact of a **consumer mediator (médiateur de la consommation)**. This is mandatory under Code de la consommation L612-1; the mediator is a paid membership.
- Penalty for missing mentions: up to €75,000 for an individual. [OK]
- **Where to put them on Etsy [INTERP]:** in the Legal and Tax information shown to EU buyers, the shop's "About" section, and the shop policies / "additional information" section.
  Sources: https://www.legalplace.fr/guides/mentions-legales/, https://www.legifiscal.fr/actualites-fiscales/3253-entreprise-individuelle-nouvelle-mention-obligatoire-factures.html, https://www.justice.fr/fiche/documents-commerciaux-entreprise-individuelle

### Right of withdrawal (droit de rétractation)
- **14 days from receipt of the goods** (Code de la consommation L221-18).
- If you do not tell the consumer about this right, the period is extended by 12 months.
- Refund within 14 days of the withdrawal, including standard outbound shipping.
- The consumer pays the return cost only if you told them so in advance. [OK]
- **Exception (L221-28 3°): goods "confectionnés selon les spécifications du consommateur ou nettement personnalisés".** **Being made to order is not enough.** A catalog design printed on demand is **not** exempt. Only a genuinely customised item (buyer's name, photo or text) is exempt. [OK]
  Sources: https://donneespersonnelles.fr/commande-personnalisee-retractation, https://www.legalstart.fr/fiches-pratiques/e-commerce/droit-retractation-achat-en-ligne/, https://www.soulier-avocats.com/remboursement-du-consommateur-apres-exercice-de-son-droit-de-retractation-et-notion-de-bien-personnalise/?pdf=33802
- **On Etsy:** set up return and exchange policies (Shop Manager → Settings → Policies). **For EU buyers you must accept returns within at least 14 days** on non-personalised items. You also owe the **2-year legal conformity guarantee** (garantie légale de conformité).
  Sources: https://help.etsy.com/hc/articles/5703129136407, https://help.etsy.com/hc/articles/115014372467
- **Cost reality [INTERP]:** Printify does not take back returns for buyer's remorse. Returns go to the address you give, so budget for them.

### Etsy creativity, POD and AI rules
- **Creativity Standards (July 2024)** classify items as Made by / **Designed by** / Handpicked by / Sourced by. POD items with the seller's original designs are **"Designed by"** and are allowed only with a production partner. [OK; OLD 2024, but still the current framework]
  Sources: https://techcrunch.com/2024/07/09/etsy-new-seller-policy-2024-generative-ai, https://www.etsy.com/seller-handbook/article/1276491338090, https://www.digitalcommerce360.com/2024/07/10/new-etsy-policies-what-sellers-will-be-able-to-offer/
- **Production partner disclosure is mandatory.** Set it up in Shop Manager → Settings → Production partners: name (e.g. "Printify" or the provider), location (city and country) and role (printing). In each listing, answer "Who made it?" with "Another company or person" and select the partner. Buyers see partners in the shop's About section. [OK]
  Sources: https://help.etsy.com/hc/articles/360000336547, https://www.listadum.com/blog/understanding-etsys-rules-for-print-on-demand-sellers, https://help.printful.com/hc/en-us/articles/360014067639-Do-I-have-to-list-Printful-as-a-production-partner-on-Etsy
- **AI:** AI-generated designs are allowed when they come from the seller's own prompts and creative input. The item must be under "Designed by", and **AI use must be disclosed**: in the listing description and in the listing's "how it's made" / AI attribute. Undisclosed AI can lead to removal. Selling prompt packs is banned. [OK/CHECK: 2026 enforcement details come only from secondary sources]
  Sources: https://www.bulkmockup.com/etsy-policy-changes/, https://ecombalance.com/ai-content-policies-2026/, https://www.etsy.com/seller-handbook/article/1276491338090

---

## Open items and things to verify first-hand
1. **Intra-EU VAT when goods ship from a non-French Printify provider** (OSS, local registration, or does the franchise still apply). This is the highest risk; get an expert-comptable's opinion.
2. Official confirmations:
   - the 2026 URSSAF rate for achat-revente (12.3% vs one outlier at 13.1%) and the CFP rate;
   - the Etsy France regulatory operating fee of 1.14% (Etsy help page) and the setup fee amount for France;
   - the EUR amount of the listing fee and whether a currency conversion fee applies.
3. Actual EU-provider base costs and shipping for each product. Check in the Printify catalog, filtering by provider location, and order samples.
4. Doormat and rug availability from **EU** providers (not confirmed).
5. Which consumer mediator to join, and its cost.
