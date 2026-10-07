# Champagne: market structure and how transactions actually happen

*Research agent 01. Compiled 7 Oct 2026. Covers who the actors are and every step of the deal chain, from grape to glass, so an AI/automation agency can find openings.*

**Method and caveats.** Direct page fetching (WebFetch/curl) was **blocked by the egress proxy** in this session for every domain tried: lachampagneviticole.fr, vitisphere.com, thedrinksbusiness.com, meininger.de, euronews.com. All facts below therefore come from web-search result summaries, ~45 queries in French and English. The session-wide search budget then ran out, so several points could not be checked further. Those points are marked **[unverified]** or **[general knowledge]**. Treat figures as best-available, not audited. Where sources disagree, the range is shown.

---

## 0. Executive snapshot

| Metric | Latest value | Source |
|---|---|---|
| Shipments 2025 | ~266 M bottles (−1.8% to −2.2% vs 271.4 M in 2024); −18% vs 2022 peak of 326 M | [Pleinchamp](https://www.pleinchamp.com/actualite/les-ventes-de-champagne-en-baisse-pour-la-3eme-annee-consecutive), [Wine Industry Advisor](https://wineindustryadvisor.com/2026/01/21/champagne-266-million-bottles-shipped-in-2025/), [LSA](https://www.lsa-conso.fr/champagne-pour-la-troisieme-annee-consecutive-les-ventes-sont-en-baisse-en-2025,464047) |
| Turnover 2025 | ~€5.2–5.7 bn (sources diverge: €5.17 bn per Pleinchamp; ~€5.6–5.7 bn in CIVC figures cited by Lanson-BCC) | [Pleinchamp](https://www.pleinchamp.com/actualite/le-rendement-commercialisable-du-champagne-fixe-a-9000-kg-ha-en-2025-en-baisse-pour-la-3eme-annee-consecutive), [AMF/Lanson-BCC filing](https://echanges.dila.gouv.fr/OPENDATA/AMF/ECO/2026/03/FCECO081216_20260311.pdf) |
| France vs export (volume) 2025 | France 114 M (−3.7%, 42.9%); export ~152 M (−1%, 57.1%) | [Meininger](https://www.meininger.de/en/meiningers-international/champagne/champagne-sees-sales-decline), Lanson-BCC release via [Bourse Direct](https://www.boursedirect.fr/fr/actualites/categorie/actualites-financieres/lanson-bcc-a-realise-un-resultat-net-de-16-2-meur-en-2025-zone-bourse-c20b79cb5c0b07c1195d5ca9809e918d7eec931e) |
| By operator type 2025 | Houses 191.6 M (−1.4%, ~72%); growers 51.3 M (−4.5%, ~19%); co-ops 22.9 M (−3.5%, ~9%) | [Meininger, citing Sophie Claeys](https://www.meininger.de/en/meiningers-international/champagne/champagne-sees-sales-decline) |
| H1 2026 | 107.1 M bottles (+1.2%); France 39.8 M (−3%), export 67.2 M (+3.8%); growers −6.2% in France, +5.1% export | [La Champagne de Sophie Claeys](https://lachampagnedesophieclaeys.fr/expeditions-de-champagne-lexport-tire-la-croissance-au-premier-semestre-2026/), [Vinabox](https://www.vinabox.fr/actu/filiere-business/champagne-2026-export-croissance-france-baisse/) |
| Growers | ~16,000–16,460 vignerons farming ~90% of the vineyard | [DGCCRF](https://www.economie.gouv.fr/dgccrf/champagne-les-principaux-enseignements-des-enquetes-conduites-en-2020-et-2021), [INAO/SGV](https://inao.gouv.fr/sites/default/files/2024-09/05-SGV%20CIVC%20Champagne.pdf), [Vitaceae](https://vitaceae.fr/observatoire/filiere-champagne/) |
| Houses / co-ops | ~370–390 maisons; ~130–138 co-ops and unions | [DGCCRF](https://www.economie.gouv.fr/dgccrf/champagne-les-principaux-enseignements-des-enquetes-conduites-en-2020-et-2021), [Vitaceae](https://vitaceae.fr/observatoire/filiere-champagne/) |
| "Metteurs en marché" (operators who sell bottles) | ~4,100 (2024); of these, ">2,000" récoltants-manipulants (RM) | [Vitaceae](https://vitaceae.fr/observatoire/filiere-champagne/), [UMC – Les vignerons](https://maisons-champagne.com/fr/encyclopedies/histoire-du-champagne/deuxieme-partie-connaissance-du-champagne/chapitre-7-les-professions-du-champagne-et-l/article/les-vignerons) |
| Grape brokers | ~40 courtiers (SPCVC members), covering relationships across >90% of the AOC area | [UMC – courtiers](https://maisons-champagne.com/fr/filiere/associations-professionnelles/article/les-courtiers-en-vins-de-champagne), [SPCVC](https://www.spcvc.com/) |
| Stock | ~1.28 bn bottles (~4.7–4.8 years of shipments) | [Pleinchamp](https://www.pleinchamp.com/actualite/le-rendement-commercialisable-du-champagne-fixe-a-9000-kg-ha-en-2025-en-baisse-pour-la-3eme-annee-consecutive), [Yahoo/Euronews](https://fr.finance.yahoo.com/actualites/chute-50-r%C3%A9colte-pourquoi-champagne-050051276.html) |
| Marketable yield | 2022: 12,000 → 2023: 11,400 → 2024: 10,000 → 2025: 9,000 → 2026: 8,800 kg/ha | [Vitaceae](https://vitaceae.fr/observatoire/rendement-et-reserve-champagne/), [France 3](https://france3-regions.franceinfo.fr/grand-est/marne/epernay/vendanges-2026-en-champagne-le-rendement-commercialisable-fixe-a-8800-kg-de-raisin-a-l-hectare-a-nouveau-en-baisse-3390265.html) |
| 2026 harvest | Agreste: −48/49% in volume (2.57 M hl → 1.34 M hl); actual yield ~7,000 kg/ha on average, from ~1,000 to >10,000 by area | [Euronews](https://www.euronews.com/business/2026/09/09/why-a-50-harvest-collapse-wont-leave-shelves-short-of-champagne), [La Champagne Viticole](https://lachampagneviticole.fr/vendange-2026-la-reserve-individuelle-pour-amortir-le-deficit-de-recolte/), [12x75](https://www.12x75.com/champagne-production-falls/) |

**Main takeaway for the agency.** Champagne runs as a very dense, very regulated B2B system: ~16k growers, ~40 brokers, ~380 houses, one interprofession. Money moves through three loops:
1. grapes and vins clairs, grower to house, almost all brokered;
2. bottles, house or grower to trade (importers, GD, CHR, cavistes);
3. bottles, grower to consumer (cellar door, mailing lists, fairs, corporate gifts).

Every loop carries excise paperwork (GAMMA 2 DAE/DSA, monthly DRM, CIVC declarations). The ~4,100 operators who sell bottles, mainly ~2,000+ RMs plus small NMs and co-ops, are the realistic target market. Most are 1–5-person family firms whose volume, especially in France, is shrinking.

---

## 1. Actors and numbers

### 1.1 Growers (vignerons)
- **~16,000–16,460 growers** own and farm **~90% of the ~34,000 ha** vineyard. The houses own ~10% but ship >70% of volume ([DGCCRF](https://www.economie.gouv.fr/dgccrf/champagne-les-principaux-enseignements-des-enquetes-conduites-en-2020-et-2021); [INAO/SGV doc](https://inao.gouv.fr/sites/default/files/2024-09/05-SGV%20CIVC%20Champagne.pdf); [Vitaceae](https://vitaceae.fr/observatoire/filiere-champagne/)). The 34,000 ha figure comes from [Wine-law / Le Temps coverage of 120k pickers for 34,000 ha](https://www.letemps.ch/economie/apres-quatre-morts-et-des-soupcons-de-traite-d-etres-humains-les-vendanges-sous-haute-surveillance-en-champagne).
- Holdings are tiny and fragmented. The average is around 2 ha **[general knowledge, not re-verified]**. Many growers hold less than 1 ha: one SGV-cited case is 63 ares ([Pleinchamp 2018](https://www.pleinchamp.com/actualite/vigne-vin~champagne-trop-taxes-certains-petits-vignerons-renoncent-a-vendre-des-bouteilles)).
- Growers fall into three economic profiles:
  - **Pure grape sellers ("vendeurs de raisins")**: the majority. They sell under contract to houses through a broker, or deliver to a co-op.
  - **Coopérateurs**: deliver grapes to a co-op. Some take back finished bottles to sell under their own label, coded **RC**.
  - **Récoltants-manipulants (RM)**: make and sell their own champagne. The UMC counts **">2,000"**. Vitaceae counts **4,100 "metteurs en marché"** in 2024, a broader group that includes RC/SR/NM ([UMC](https://maisons-champagne.com/fr/encyclopedies/histoire-du-champagne/deuxieme-partie-connaissance-du-champagne/chapitre-7-les-professions-du-champagne-et-l/article/les-vignerons); [Vitaceae](https://vitaceae.fr/observatoire/filiere-champagne/)). In the 1990s about 5,000 growers sold under their own brand ([Persée 1999](https://www.persee.fr/doc/rgpso_1276-4930_1999_num_6_1_2715)). The long-term trend is **fewer growers bottling**.
- **Grower share of shipments is falling.** It was about 25% around 1999–2000, ~18–19% in recent years, and **51.3 M bottles (~19%) in 2025, −4.5%** ([Wine Business International](https://www.wine-business-international.com/wine/insights-wine/grower-champagne-success-story-never-happened); [Meininger](https://www.meininger.de/en/meiningers-international/champagne/champagne-sees-sales-decline)). Grower champagne sells mainly in France. Around 2017, growers had about 46% of French sales ([Champagnes de Vignerons partnership doc](https://ent2d.ac-bordeaux.fr/disciplines/hotellerie/wp-content/uploads/sites/46/2017/07/Partenariat-Champagnes-de-Vignerons-Enjeu-et-Mode-demploi-2017-2018.pdf)). That makes growers the group most exposed to the shrinking French market: H1 2026 France −6.2% ([Sophie Claeys](https://lachampagnedesophieclaeys.fr/expeditions-de-champagne-lexport-tire-la-croissance-au-premier-semestre-2026/)).
- **Rule on buying grapes:** an RM may buy only 5% of production in grapes, musts or wine under its own excise number (arrêté of 4 Aug 2017). Above that, it needs a second "négociant" excise number with separate books and storage. For 2026 the cap was **raised to 15%** because of the frost-hit crop (arrêté of 7 Aug 2026, JO 12 Aug) ([Vinetur](https://www.vinetur.com/fr/20260904106640/france-raises-champagne-growers-purchase-ceiling-to-15-for-the-2026-harvest.html); [L'Officiel des métiers](https://www.lofficieldesmetiers.fr/champagne-le-plafond-dachat-de-raisins-passe-de-5-a-15/)). Expect a one-off spike of grower-to-grower purchases in 2026–27, plus new compliance questions.

### 1.2 Cooperatives (CM)
- **~130–138 co-ops and unions** account for ~9% of shipments: 22.9 M bottles in 2025 ([Meininger](https://www.meininger.de/en/meiningers-international/champagne/champagne-sees-sales-decline); [DGCCRF](https://www.economie.gouv.fr/dgccrf/champagne-les-principaux-enseignements-des-enquetes-conduites-en-2020-et-2021)). Co-ops also supply houses with vins clairs and bottles "sur lattes", and supply BOB/MA labels.
- **Terroirs et Vignerons de Champagne (TEVC)** was formed in 2022 from the merger of CV-Nicolas Feuillatte and CRVC (Castelnau). It is a union of ~80 co-ops representing ~6,000 growers. Revenue was **€323 M in 2024 (+11.2%)**, net €4.2 M. It acquired Henriot in 2023 and is often described as the #2 group by volume after LVMH ([LSA](https://www.lsa-conso.fr/champagne-tevc-nicolas-feuillatte-affichent-une-activite-en-croissance,461245); [Le Monde du Droit](https://www.lemondedudroit.fr/deals/79351-aramis-conseille-le-centre-vinicole-champagne-nicolas-feuillatte-cv-cnf-dans-le-cadre-de-sa-fusion-avec-la-cooperative-regionale-des-vins-de-champagne-c-r-v-c.html); [Meininger DE](https://www.meininger.de/wein/erzeuger/terroirs-et-vignerons-de-champagne-waechst-weiter)).
- **Alliance Champagne / Union Champagne (De Saint Gall)**: a large co-op union and a major supplier of UK supermarket own labels ([essiavellan/MA explainer](https://essiavellan.com/?p=3056)). No 2025 figures were found **[unverified]**.

### 1.3 Houses (négociants-manipulants, NM)
- **~370–390 houses** ship ~72% of volume: 191.6 M bottles in 2025 ([Meininger](https://www.meininger.de/en/meiningers-international/champagne/champagne-sees-sales-decline)). They buy most of their grapes. In 2014 houses bought 59.2% of the regional crop ([INSEE/DRAAF](https://www.insee.fr/fr/statistiques/2018375)). Their share keeps creeping up.
- **LVMH (Moët Hennessy)**: ~22% of appellation shipments in 2025 (Moët & Chandon, Veuve Clicquot, Ruinart, Krug, Mercier, Dom Pérignon). Moët Hennessy revenue €5.4 bn (−5%), all categories. A ~10% workforce cut (~1,200 jobs) was announced May 2025. Champagne staff struck in Jan 2026 over a withheld profit-share ([FoodBusinessMEA](https://www.foodbusinessmea.com/lvmh-wine-and-spirits-revenue-falls-5-in-2025-as-champagne-shows-resilience/); [inside.beer](https://www.inside.beer/news/detail/france-moet-hennessy-to-cut-10-of-global-workforce); [Drinks Business](https://www.thedrinksbusiness.com/2026/01/moet-hennessy-champagne-workers-strike-over-unpaid-profit-share/)).
- **Lanson-BCC**:
  - 2025 revenue €233.3 M (−8.7%); H2 −15.7%; net income €16.2 M (vs €23.8 M).
  - France is 44.7% of its volume and fell 10.7%, notably in GD under an "aggressive promotional environment" in Q4.
  - EBITDA fell partly because of the **higher grape cost**.
  - Bought Heidsieck & Co Monopole from Vranken for €50 M (Sep 2025).
  - Sources: [Bourse Direct](https://www.boursedirect.fr/fr/actualites/categorie/actualites-financieres/lanson-bcc-a-realise-un-resultat-net-de-16-2-meur-en-2025-zone-bourse-c20b79cb5c0b07c1195d5ca9809e918d7eec931e), [La Libre](https://www.lalibre.be/economie/entreprises-startup/2025/09/25/vranken-pommery-vend-heidsieck-co-a-lanson-bcc-YYPTV3DRD5CRDILYAQOSA74EL4/).
- **Vranken-Pommery → "Maison Pommery & Associés"** (renamed 1 Jan 2026): 2025 revenue €293.2 M (−3.6%); bottled volume +3.6%. Champagne value −1.8% because of lower **interprofessional (bulk) sales** ([Bourse Direct](https://www.boursedirect.fr/fr/actualites/categorie/chiffre-d-affaires/maison-pommery-une-activite-2025-en-leger-retrait-boursier-38fc547ac38c5b27322c6419aeccc7fe89e4bb3b)).
- **Laurent-Perrier** (FY to 31 Mar 2026): champagne sales €294.8 M (+4.2%), volume +3.8%, net €49.5 M, operating margin 25.8% ([OptionFinance](https://www.optionfinance.fr/info-financiere-en-continu/d/2026-05-29-laurent-perrier-accroit-legerement-son-resultat-net-annuel.html)).
- Others include Thiénot, Piper/Charles Heidsieck (EPI), Taittinger, Bollinger, Roederer, Pol Roger and Mumm/Perrier-Jouët (Pernod). The mid-sized family houses selling 0.1–5 M bottles are a plausible mid-market target **[general knowledge]**.

### 1.4 Brokers (courtiers en vins de Champagne)
- About **40 brokers** sit in the SPCVC (founded 1941), some working in group offices. They intermediate grape and vin clair deals across **>90% of the AOC area**. The trade was codified by the Bourse de Reims rules of 1825 ([UMC](https://maisons-champagne.com/fr/filiere/associations-professionnelles/article/les-courtiers-en-vins-de-champagne); [SPCVC](https://www.spcvc.com/presentation)).
- Since 2004 the SPCVC has published an annual **"mercuriale"** of grape prices built from invoices. It is used as the reference, including in the prefectoral **fermage** (land-rent) grape price ([UMC – Les prix](https://maisons-champagne.com/fr/encyclopedies/histoire-du-champagne/deuxieme-partie-connaissance-du-champagne/chapitre-12-le-commerce-du-champagne/article/les-prix); [La Champagne Viticole](https://lachampagneviticole.fr/prix-du-raisin-2025-pour-le-paiement-des-loyers-viticoles/)).
- A broker is in effect a one-person or small-office firm that handles sourcing, contracting, invoicing and payment splitting for hundreds of growers (see §2). The work is largely relationship-based and document-heavy, which makes brokers **a natural, concentrated target for automation**.

### 1.5 Interprofession and unions
- **Comité Champagne (CIVC)**, Épernay, founded by the law of 12 Apr 1941. It sets the yield and reserve, writes the contract framework, collects mandatory contributions and receives harvest and stock declarations from growers and co-ops ([Légifrance](https://www.legifrance.gouv.fr/loda/id/LEGITEXT000006071660)).
- **SGV** (Syndicat Général des Vignerons) represents growers and sells services: capsules, fairs, support ([SGV services](https://www.sgv-champagne.fr/les-services/)).
- **UMC** (Union des Maisons de Champagne) represents houses.
- **SPCVC** represents brokers.
- There is also a federation of co-ops.

---

## 2. The grape market (raisins)

**How it works, step by step**

1. **Each July: yield and reserve decision.** The Comité sets the *rendement commercialisable* (marketable yield): 9,000 kg/ha for 2025 and 8,800 kg/ha for 2026, decided 22 Jul 2026. It also sets the *réserve individuelle* (individual reserve) rules. For 2026, grapes harvested between 8,800 kg/ha and the 15,500 kg/ha "butoir" can go into reserve, up to a 10,000 kg/ha ceiling. The reserve averaged ~7,000 kg/ha before the 2026 harvest. Reserve releases are paid in **three equal instalments: 5 Mar, 5 Jun, 5 Sep 2027** ([La Champagne Viticole](https://lachampagneviticole.fr/vendange-2026-la-reserve-individuelle-pour-amortir-le-deficit-de-recolte/); [Vitaceae reserve](https://vitaceae.fr/observatoire/champagne-reserve-individuelle/)). An interprofessional decision then becomes binding by ministerial arrêté. Example: the 23 Jul 2025 supply agreement for 2025-26 was approved by arrêté on 1 Dec 2025 ([BO Agri](https://info.agriculture.gouv.fr/boagri/document_administratif-81b5a070-25dd-48dc-b072-1ad365073d14/telechargement)).
2. **Multi-year contracts.** **CIVC Decision n°196** (13 Dec 2023) governs grape, must and wine contracts between sellers and buyers for campaigns **2024-25 to 2028-29**. It replaces n°182 and n°187. A contract that does not follow the CIVC model is **void** ([BO Agri / SPCVC Décision 187](https://www.spcvc.com/ouvrir/document/decision-n187du-14-decembre-2018)). It is a collective CIVC template that each house and grower signs individually:
   - Houses commit to buy each year a freely chosen share of their sales volume, up to 120%.
   - Growers commit to sell up to 100% of their crop.
   - Duration is "at least 4 years" according to the UMC, typically **5 years** according to the SPCVC.
   - In 1995 such contracts covered 91% of traded grapes ([UMC – transactions](https://maisons-champagne.com/fr/filiere/developpement-durable-champagne/economie/article/l-organisation-des-transactions-entre-les)).
3. **Price.** Price is negotiated freely between grower and house. The indexed interprofessional price ended in 1990 on competition grounds. Reference points:
   - Average ~€5.97/kg in 2018 and **€7.35/kg in 2024** including certification premiums (Cerfrance, cited by [CGT Reims](https://www.cgtchampagnereims.fr/vendanges-2026-lor-du-raisin-les-miettes-aux-salaries/)).
   - The Marne fermage reference for 2025 runs from **€6.64/kg** in most villages to **€8.70/kg** in Côte des Blancs grands crus. Aube examples are €7.56–7.61/kg ([La Champagne Viticole](https://lachampagneviticole.fr/prix-du-raisin-2025-pour-le-paiement-des-loyers-viticoles/); [Vitaceae fermage](https://vitaceae.fr/observatoire/fermage-viticole/champagne/prix-du-raisin-fermage-par-commune/)).
   - In 2025 some houses announced cuts. **Four large groups cut €0.20–0.25/kg**, but most houses did not follow, so the net average fell only about €0.07/kg (La Champagne Viticole, via search summary).
   - Pricing differs by cru (village) and by certification (HVE, VDC, organic) bonuses **[general knowledge]**.
   - The 2026 short crop (−49%) is likely to firm prices, which is bullish for growers with fruit. No 2026 price figures were found **[unverified]**.
4. **Execution at harvest.**
   - Grapes are pressed (often at the grower's or the house's press centre, the *centre de pressurage*). Must moves to the house under an excise movement document.
   - **Brokers obtain the customs movement documents and arrange transport of the must**.
   - They **often issue invoices on behalf of growers and split each house payment across the individual grape deliverers**, "per the agreed price and due dates" ([UMC – courtiers](https://maisons-champagne.com/fr/filiere/associations-professionnelles/article/les-courtiers-en-vins-de-champagne); [SPCVC charter](https://www.spcvc.com/deontologie)).
   - Payment terms are set by regulation, with different rules for multi-year and spot contracts (Decision 187/196). Payment usually comes in several instalments through the following year **[specific dates unverified]**.
   - The brokerage commission is charged at "rates in force" (SPCVC charter). The **% was not found [unverified]**.
5. **Fermage.** Many growers rent land and pay rent in kilos of grapes valued at the prefectoral price. A 2025 side effect: for some tenants the rent can exceed what they get selling grapes to certain houses (La Champagne Viticole).

**Digital platforms?** No B2B marketplace for Champagne grapes, musts or vins clairs was found. Searches returned only consumer and retail platforms such as Les Grappes. Trading stays **broker-led and relationship-based**. Paperwork consists of the CIVC model contract, broker confirmation letters, broker-issued invoices and customs DAE/DSA. **This looks like a whitespace, but it is politically sensitive**: brokers, the CIVC and unions control the process, so a "broker back-office" tool fits better than a disintermediating marketplace.

---

## 3. Bulk wine trade: vins clairs, "sur lattes", BOB/MA

- **Vins clairs (base wines)** are bought "au cas par cas" (one deal at a time) through brokers. The broker negotiates quality, quantity and price, then sends both parties a **"confirmation de transaction"**, which makes the deal binding ([UMC](https://maisons-champagne.com/fr/filiere/associations-professionnelles/article/les-courtiers-en-vins-de-champagne)). The decision framework also covers spot (*ponctuel*) contracts. No public vin clair price index was found. FranceAgriMer's bulk-wine notes do not cover Champagne vins clairs ([Vinabox/FranceAgriMer](https://www.vinabox.fr/actu/filiere-business/vin-vrac-prix-hausse-exportations-franceagrimer-septembre-2026/)).
- **"Sur lattes"** means finished, second-fermented bottles without labels, traded between houses, co-ops and growers, then disgorged and labelled by the buyer. One biased producer source values these bottles at **~€10–13 each** ([Bricout page](https://www.champagne-bricout.fr/vins%20sur%20lattes.htm)). UFC-Que Choisir cites an older figure of ~€11 HT for grower-to-négoce bottle exchanges ([Que Choisir](https://www.quechoisir.org/conseils-champagne-les-dix-questions-a-se-poser-pour-bien-choisir-une-bouteille-de-champagne-n61374/)). Pommery's 2025 value dip came from lower **interprofessional sales**, a sign that houses trim bulk/sur-lattes trade in a downturn ([Bourse Direct](https://www.boursedirect.fr/fr/actualites/categorie/chiffre-d-affaires/maison-pommery-une-activite-2025-en-leger-retrait-boursier-38fc547ac38c5b27322c6419aeccc7fe89e4bb3b)).
- **BOB / Marque d'Acheteur (MA)**: a brand owned by a retailer, restaurant or merchant and filled by an NM or co-op. MA labels account for about 8% of volume and 9% of value. Supply is concentrated among large co-op unions (e.g., Union Champagne/De Saint Gall) and some houses ([essiavellan](https://essiavellan.com/?p=3056); [Lea & Sandeman](https://www.leaandsandeman.co.uk/blog/?p=35294)). In French supermarkets, national brands average **€38** and private labels **€24** ([Economie Matin](https://www.economiematin.fr/?p=175195)).
- **How it's contracted:** through brokers or direct tenders. Specifications, tasting samples, price per bottle, allocation by year and private-label artwork approvals are handled by email and PDF **[general knowledge; no Champagne-specific process doc found]**.

---

## 4. Bottled champagne B2B sales

**Channels:**
- **Export**: importer or distributor per country (three-tier in the US). Major markets are the UK, US and Japan; the US took 26.5 M bottles in 2025.
- **France**: grande distribution (GD), CHR (cafés, hotels, restaurants), cavistes, wholesalers, duty free, and corporate buyers including works councils (CSE).

Key facts:
- **GD is a price battlefield.**
  - ~47 M bottles a year sell in French supermarkets.
  - **50.8% of supermarket champagne sales are on promotion**.
  - Promo prices "regularly fall below €10" ([Réussir](https://www.reussir.fr/les-prix-bas-du-champagne-font-debat)).
  - Lanson-BCC blamed an "aggressive promotional environment" in Q4 2025.
  - Many RMs refuse GD on principle ([Réussir](https://www.reussir.fr/les-prix-bas-du-champagne-font-debat)).
- **US tariffs.**
  - 10% from April 2025, **15% from 7 Aug 2025** (EU-US deal; wine got no exemption).
  - A 200% threat was voiced on 20 Jan 2026 but not enacted.
  - The US is ~10% of export volume and ~15% of value.
  - Houses cut euro FOB prices to absorb the duty; IÉSEG documents falling export prices ([Pleinchamp](https://www.pleinchamp.com/actualite/droits-de-douane-americains-sur-le-vin-le-taux-de-15-confirme-la-filiere-decue-mais-pas-resignee); [IÉSEG PDF](https://insights.ieseg.fr/wp-content/uploads/2026/03/Forte-baisse-des-prix-de-depart-en-euros-du-Champagne-Cognac-et-vins-exportes-par-la-France-vers-les-Etats-Unis-en-2025-a-cause-des-droits-de-douane-1.pdf); [AN question 12362](https://www.assemblee-nationale.fr/dyn/17/questions/QANR5L17QE12362)).
  - About **2 M bottles were pulled forward into Dec 2024** ahead of the tariffs (Comité co-president David Chatillon, via Drinks Business/Meininger).
  - Small growers with US exposure are diversifying. Charles Fourny has 18% of sales in the US and is looking at Brazil ([Business AM](https://fr.businessam.be/?p=172549)).
  - US restaurants are delisting some champagne and crémant ([Vinetur](https://www.vinetur.com/fr/amp/2026033098331/us-restaurants-drop-european-wines-as-tariffs-drive-up-prices.html)).
- **Trade fairs** are the main export prospecting channel. **Wine Paris 2026** (9–11 Feb) drew 63,541 trade visitors (51% international) and 6,537 exhibitors, with **25,958 pre-booked meetings through its matchmaking platform (+28%)**. Commentators say it is overtaking ProWein ([Vinexposium bilan PDF](https://www.vinexposium.com/wp-content/uploads/2026/02/CP_WINE-PARIS-2026_BILAN_FR.pdf); [Corriere del Vino](https://corrieredelvino.it/en/editorial/wine-paris-2026-hot-off-the-press-impressions/)). The SGV organises collective stands for growers ([SGV services](https://www.sgv-champagne.fr/les-services/)).
- **Order flow at small and mid players** **[general knowledge; consistent with the software vendors' feature lists]**:
  - Price lists (tarifs) go out as PDF or Excel per channel (particulier, CHR, caviste, importateur ex-cellar/EXW/FOB) and are updated each January.
  - Orders arrive by email, phone, WhatsApp or the fair order pad.
  - Pro-formas lead to prepayment for new importers.
  - Allocation of scarce cuvées (vintage, prestige) is managed in spreadsheets.
  - Export needs an excise DAE (GAMMA 2), the export declaration (DELTA, EX1 by the forwarder), and certificates of origin or analysis on request.
  - Invoicing and dunning are done in a general accounting tool or a wine ERP.
  - Baqio's "Bulles" module advertises **automatic excise-number checks and DAE generation** for export, evidence that this is a recognised pain ([Réussir – Baqio](https://www.reussir.fr/vigne/baqio-adapte-son-logiciel-aux-vignerons-champenois)).
- **Intra-EU B2C shipping is a nightmare for small growers.** Selling to a consumer in another member state means handling excise in the destination country, often through a fiscal representative. The SGV says it is "simpler to ship two pallets across the planet than two cartons to a neighbouring country". It lobbies for an EU excise one-stop shop modelled on VAT OSS ([Réussir – SGV](https://www.reussir.fr/vigne/le-syndicat-general-des-vignerons-de-champagne-plaide-pour-des-mesures-daccompagnement-commercial)). Existing public commercial-support schemes apply only from **€1 M turnover**, which excludes most RMs (same source).

---

## 5. Direct-to-consumer

- **The historic core of grower sales.** In 1990, growers' French sales went "mostly to private individuals and collective buyers such as works councils" ([Autorité de la concurrence 96-D-59](https://www.autoritedelaconcurrence.fr/sites/default/files/commitments/96d59.pdf)). Visitors buy from several growers so they can compare (Champagnes de Vignerons doc).
- **Channels** **[mostly general knowledge; no Champagne-specific channel split found]**:
  - cellar door (*caveau*) and tastings
  - the **private client file** (*fichier clients*), with the classic annual price list and order form posted in autumn for Christmas, now increasingly sent by email
  - consumer fairs (*salons des vins*, Vignerons Indépendants fairs, village fairs across France)
  - e-commerce (own Shopify/WooCommerce site, Les Grappes, Vinatis marketplaces)
  - CSE and works-council group orders
  - **corporate gifts** (*cadeaux d'affaires*)
  - weddings and events
  - clubs and subscriptions.

  The Vignerons Indépendants (all France) report that **96% sell direct at the estate and 73% at fairs**, at direct prices ~50% above GD ([VSNews PDF](https://www.vsnews.fr/images/Le_commerce_intracommunautaire_des_vins_a_destination_des_particuliers_-_Propositions_de_reforme.pdf)).
- **Oenotourism is booming.**
  - Grand Est had ~2 M wine tourists, with international visitors growing +29% against +14% for French visitors ([Assises de l'Oenotourisme 2025 PR](https://extranet.aube-champagne.com/assets/uploads/sites/34/2025/03/COMMUNIQUE-DE-PRESSE-2e-Assisses-de-lOenotourisme-en-Champagne.pdf)).
  - The UNESCO listing effect continues. Hautvillers and Aÿ have capped tourist rentals ([L'Écho touristique](https://www.lechotouristique.com/article/france-loenotourisme-petille-en-champagne-surfant-sur-leffet-unesco)).
  - In 2019 an average Champagne wine-tourism site received ~3,419 visitors ([Vignobles & Découvertes observatory](https://tourisme-en-champagne.com/assets/uploads/2025/07/chiffres-de-loenotourisme-enquete-vd-2019-2020-pour-diffusion.pdf)).
  - Bookings, multilingual enquiries and reviews are an automation opening.
- **The Q4 peak.**
  - Lanson-BCC did 47.2% of annual revenue in Q4 2013. Vranken says ~50% of its bottles sell at year-end ([TradingSat](https://www.tradingsat.com/lanson-bcc-FR0004027068/actualites/lanson-bcc-les-ventes-de-lanson-ont-grimpe-de-82-au-4e-trimestre-503943.html)).
  - Sales peak in November–December, with a spike in the ~10 days before the holidays.
  - Corporate gift catalogues concentrate in December. A comparable gourmet retailer does ~80% of corporate-gift catalogue sales in December ([OptionFinance](https://www.optionfinance.fr/carrieres/les-directeurs-financiers-de-la-gastronomie.html)).
  - No hard figure on corporate gifts' share of champagne sales was found **[unverified]**.

---

## 6. Regulatory and admin layer (per transaction)

| Obligation | What it is | Frequency / channel | Source |
|---|---|---|---|
| **Déclaration de récolte / production** | Harvest declaration. CIVC growers and co-ops **cannot use customs' VENDANGES service; they file through the CIVC**. Customs deadline is 10 Dec for growers and 10 Jan for co-ops/négociants | Yearly, Oct–Dec | [douane.gouv.fr](https://www.douane.gouv.fr/fiche/informations-sur-le-service-en-ligne-vendanges) |
| **Déclaration de stock** | Growers and co-ops file through the CIVC; négociants file directly with customs | Yearly (31 Jul) | same |
| **Réserve individuelle** mise en réserve / déblocage | Putting grapes into, and releasing them from, the individual reserve. Tracked per grower by the CIVC | Yearly + releases | [La Champagne Viticole](https://lachampagneviticole.fr/vendange-2026-la-reserve-individuelle-pour-amortir-le-deficit-de-recolte/) |
| **DAE / DAES / DSA** in **GAMMA 2** | Excise movement documents: DAE for duty-suspended movements (export, bulk, entrepositaire to entrepositaire); DAES for duty-paid shipments to the EU; DSA for some national moves. GAMMA 2 went live **25 Jun 2025** and replaced GAMMA legacy and MVV | Every shipment | [Vitisoft](https://vitisoft.fr/blog/gamma-2-circulation-vins-dae-daes/), [Wineriz](https://www.wineriz.com/gamma2-douane-domaine-viticole-guide/), [eDouane](https://www.edouane.com/dgddi-bascule-definitive-vers-gamma-2-les-dernieres-etapes-et-interruption-de-service/) |
| **DRM** | Monthly summary of stock movements and duties, due by the **10th of the following month** through customs CIEL (often via the interprofession portal). Plan: merge the DAI, stock declaration and August DRM (2026), and **link GAMMA→CIEL automatically by 2027** | Monthly | [Wineriz DRM](https://www.wineriz.com/drm-vin-guide-complet-declaration-recapitulative-mensuelle/), [Vitisphere](https://www.vitisphere.com/actualite-105631-ladministration-travaille-au-compte-unique-viticole-entre-la-complexification-mvv-gamma-2-et-vendanges-et-la-fusion-du-dai-de-la-declaration-de-stock-et-de-la-drm-daout.html) |
| **CIVC sales declarations and contributions** | Sales by country and quality. Mandatory parafiscal contributions are levied per kg of grapes and per bottle sold; rates are set yearly by arrêté (2026 budget decided 23 Jul 2025). Historic examples: €1.80/100 kg and €2.21/100 bottles. **Current rates not found** | Monthly/periodic | [EC state-aid doc](https://ec.europa.eu/competition/state_aid/cases/137103/137103_451315_4_2.pdf), [Baqio feature list](https://www.reussir.fr/vigne/baqio-adapte-son-logiciel-aux-vignerons-champenois) |
| **CRD capsules** | Duty-paid capsules. Optional nationally since 1 Jul 2019. Champagne developed a digital/smart capsule; the SGV sells capsules to growers | Per bottle | [douane.gouv.fr simplification](https://www.douane.gouv.fr/actualites/simplification-administrative-pour-les-professionnels-du-vin), [SGV](https://www.sgv-champagne.fr/les-services/) |
| **Registres / comptabilité matières** | Cellar records: vins clairs, tirage, sur lattes, sur pointes, disgorging, liqueur, bottled. Champagne's multi-stage process makes stock accounting unusually complex (Baqio Bulles exists for this) | Continuous | [Réussir – Baqio](https://www.reussir.fr/vigne/baqio-adapte-son-logiciel-aux-vignerons-champenois) |
| **Export** | EX1/export declaration (DELTA; a GAMMA 2–DELTA link was planned in 2026), certificates of origin, country label compliance, US COLA/importer formalities | Per export shipment | [Vitisphere](https://www.vitisphere.com/actualite-105631-ladministration-travaille-au-compte-unique-viticole-entre-la-complexification-mvv-gamma-2-et-vendanges-et-la-fusion-du-dai-de-la-declaration-de-stock-et-de-la-drm-daout.html) |
| **Intra-EU B2C excise** | Destination-country excise, fiscal representative | Per sale | [Réussir – SGV](https://www.reussir.fr/vigne/le-syndicat-general-des-vignerons-de-champagne-plaide-pour-des-mesures-daccompagnement-commercial) |
| **Labels** | Operator code (RM/NM/CM/RC/SR/ND/MA) + registration number, dosage, allergens, nutrition/ingredient QR (EU 2023 rules) | Per SKU | [DGCCRF labels](https://www.economie.gouv.fr/dgccrf/les-fiches-pratiques/champagne-connaitre-le-langage-des-etiquettes) |
| **Harvest labour** | ~120,000 seasonal pickers for ~34,000 ha. Housing rules tightened after four deaths and a trafficking case in 2023. The Anavim subcontractor case ended in prison sentences on 21 Jul 2025, with an appeal in Jan 2026. The Comité Champagne joined as civil party and adopted "zero tolerance" | Yearly | [Le Temps](https://www.letemps.ch/economie/apres-quatre-morts-et-des-soupcons-de-traite-d-etres-humains-les-vendanges-sous-haute-surveillance-en-champagne), [La Libre](https://www.lalibre.be/economie/emploi/2025/06/18/vendanges-en-champagne-un-proces-pour-traite-detre-humain-souvre-ce-jeudi-QO7B2EKMQJFD7OPOIKF3W3XSYE/), [Brut](https://www.brut.media/fr/articles/france/justice-faits-divers/vendanges-en-champagne-prison-ferme-pour-traite-detres-humains) |

**Who does the paperwork in a small domaine?**
- No Champagne-specific time study was found **[unverified]**.
- Sector evidence and the vendors' positioning point to the same pattern. Admin (DRM, DAE, CIVC declarations, invoicing, client file, orders) typically falls on **one family member, often the spouse working as *conjoint collaborateur*, or the grower in the evening**, sometimes with help from the accountant (Cerfrance) or the SGV.
- An Alsace MP described the DRM as heavy for independent growers, who track up to 20 products ([AN QE](https://www.assemblee-nationale.fr/dyn/14/questions/QANR5L14QE80021.pdf)).
- The CNAOC calls for a "choc de simplification" and a single window ([Agra](https://www.agra.fr/vin-la-cnaoc-appelle-poursuivre-le-choc-de-simplification-administrative)).
- Customs itself is building a "compte unique viticole" (single wine account) because the stack (MVV, GAMMA 2, VENDANGES, DAI, DRM) is acknowledged to be complex ([Vitisphere](https://www.vitisphere.com/actualite-105631-ladministration-travaille-au-compte-unique-viticole-entre-la-complexification-mvv-gamma-2-et-vendanges-et-la-fusion-du-dai-de-la-declaration-de-stock-et-de-la-drm-daout.html)).
- Existing software includes Baqio (with a Champagne "Bulles" module), Vitisoft, Wineriz, Wine'r, Sage X3 integrators for houses ([Arcanes](https://www.arcanes.info/2026/06/26/declarations-douanieres-vin-sage-x3/)), Isagri and others. Their market share in Champagne is **unknown**.

---

## 7. Seasonality and calendar

Rows marked † come from the sources above; the rest is **[general knowledge of AOC rules]**.

| Period | Vineyard / cellar | Commercial / admin |
|---|---|---|
| Jan | Assemblage (blending) of vins clairs; **tirage (bottling for second fermentation) allowed from 1 Jan** | New price lists; DRM; reserve release decisions (1 Feb release†) |
| Feb–Mar | Tirage, pruning | **Wine Paris (Feb)†**, ProWein (Mar); grape instalments; reserve payments 5 Mar† |
| Apr–Jun | Frost risk (2026: ~40% of buds lost region-wide, 85% in the Aisne†), disgorging for summer | Export orders; Vinexpo-style fairs; reserve payment 5 Jun† |
| Jul | — | **Yield and reserve decision (≈22–23 Jul)†**; stock declaration 31 Jul; interprofessional supply agreement† |
| Aug–Sep | **Harvest**: 2025 from 20 Aug, 2026 from 15–17 Aug (earliest ever)†; ~120k pickers†; pressing; musts moved to houses under DAE† | Hiring and housing compliance; broker confirmations; GAMMA DAEs for musts |
| Oct–Nov | Alcoholic and malolactic fermentation of vins clairs | **Harvest declaration (by 10 Dec)†**; vin clair spot deals; Q4 orders; corporate gift catalogues; client mailing |
| Dec | — | **Peak**: ~40–50% of year's sales in Q4†; GD promotions†; heaviest DAE/DRM month |

Minimum ageing on lees is 15 months for non-vintage and 3 years for vintage. Stock therefore turns over very slowly (~4.8 years of shipments†), which makes cash-flow and stock accounting central.

---

## 8. Key pain points (from press and interviews)

1. **Falling volumes, especially in France.** Three years of decline (−8.2% in 2023, −9.2% in 2024, −2% in 2025). France keeps falling into 2026 (H1 −3%). Growers are hit hardest because they depend on France and private customers ([Sophie Claeys](https://lachampagnedesophieclaeys.fr/expeditions-de-champagne-lexport-tire-la-croissance-au-premier-semestre-2026/)).
2. **Margin squeeze.** Grape costs are high (~€7.35/kg in 2024†) while GD promotions push shelf prices under €10†. Lanson's EBITDA fell partly on grape cost†.
3. **Over-stock and falling yields.** The yield fell 26% in four years. Growers selling grapes earn less per hectare (8,800 vs 12,000 kg/ha). Stocks equal ~4.8 years of shipments.
4. **2026 climate shock.** Frost, heat and drought cut the crop roughly in half by volume (Agreste −49%), with very uneven losses (1,000 to 10,000+ kg/ha). The reserve and the 15% purchase derogation are the buffer. The CIVC exceptionally allowed up to 15% alcohol ([Economie Matin](https://www.economiematin.fr/champagne-autorisation-exceptionnelle-commercialiser-jusqu-15-alcool)).
5. **Export tariffs.** 15% US duty since Aug 2025, plus a weak dollar and repeated threats. Some US restaurants are delisting.
6. **Labour.** Recruiting and housing 120k pickers; the trafficking scandal; subcontractor liability; the Comité's action plan.
7. **Admin burden.** GAMMA 2 rollout (2025), DRM, CIVC declarations and intra-EU excise all sit on micro-firms with no admin staff. Public commercial-support schemes start at a €1 M turnover.
8. **Succession and land cost.** Inheritance tax of roughly €100,000 per hectare inherited (SGV, 2018). The 2025 Finance Law improved the transmission regime ([La Champagne Viticole](https://lachampagneviticole.fr/en/loi-de-finances-pour-2025-une-avancee-majeure-pour-la-transmission-des-exploitations-viticoles/)). Growers stop bottling and sell grapes instead, which explains the long decline in RM numbers.
9. **Workforce cuts at the big houses.** Moët Hennessy −10%, and profit-share strikes.
10. **Grower vs house tension** over who pays for the downturn: "It is not up to independent growers to pay for the mistakes… of houses" (union view, via Euronews).

---

## 9. Top 10 manual or painful steps in the transaction chain

Ranked by likely automation value for a small agency. Evidence quality is noted in brackets.

1. **Broker back-office: contracts → confirmations → invoices → payment splits.** About 40 brokers each issue CIVC-model contracts, transaction confirmations, invoices "on behalf of growers" and per-deliverer payment splits across instalments, for hundreds of growers each [strong evidence on the tasks, UMC/SPCVC; tooling unknown]. *Opportunity:* a document-generation and reconciliation workflow, plus a grower portal.
2. **Excise movement documents (DAE/DSA/DAES in GAMMA 2)** for every pro, export or bulk shipment, including must transfers at harvest [strong; GAMMA 2 since Jun 2025]. *Opportunity:* auto-filling from orders, excise-number verification (Baqio already does part of this).
3. **Monthly DRM + CIVC sales declarations (by country and quality) + annual harvest and stock declarations.** These are re-keyed from cellar records into several portals (CIVC, CIEL) [strong]. *Opportunity:* reconciliation assistants. The 2027 GAMMA→CIEL link may commoditise part of this, so build around it.
4. **Champagne-specific stock accounting**: vins clairs → tirage → sur lattes → sur pointes → disgorgement → labelled stock, plus reserve wine and individual reserve kilos [strong]. Most small domaines use spreadsheets or a generic ERP **[inferred]**.
5. **Q4 order crush**: private-client mailing, CSE and corporate gift orders, personalised labels and cases, delivery scheduling and invoicing, with ~40–50% of revenue in ~10 weeks [moderate]. *Opportunity:* a CRM, an order portal, automated mailings and AI handling of email orders.
6. **Price-list and allocation management** across channels (private, CHR, caviste, importer EXW/FOB, GD) and scarce cuvées, sent as PDF and email [inferred, typical].
7. **Importer prospecting and fair follow-up**: Wine Paris alone handled ~26k pre-booked meetings. Follow-ups, samples, pro-formas, price quotes and label-compliance questions per country are handled manually [moderate]. *Opportunity:* an AI SDR, lead enrichment and a follow-up CRM. Tariffs push growers to diversify markets (Brazil, Asia).
8. **Intra-EU B2C shipping compliance** (destination excise, fiscal representative) [strong pain, SGV]. *Opportunity:* a guided workflow or partner integration rather than a full build.
9. **Harvest logistics and HR**: picker recruitment, contracts, housing compliance, press-centre scheduling, weigh tickets (*carnets de pressoir*), reserve allocation [strong pain; tooling unknown].
10. **Oenotourism bookings and multilingual enquiries**, plus review and response management, as international visitors grow +29% [moderate].

Other gaps found: no digital marketplace or price index for grapes or vins clairs (whitespace, but politically sensitive); no current per-unit CIVC contribution rates; no current broker commission %.

---

## 10. Segment lens: small vs mid vs giant

| | Small grower (RM/RC, 3–10 ha, 1–5 people) | Mid house / co-op (0.2–5 M bottles) | Giant (LVMH, TEVC, Lanson-BCC, Pommery, LP) |
|---|---|---|---|
| Sales | Mostly France: private clients, CSE, fairs, cellar door, some CHR and caviste; growing export | Mix of GD, CHR, export importers, BOB | Global distribution subsidiaries, GD, duty free |
| Admin | Owner or spouse; accountant; maybe Baqio/Vitisoft | 1–5 admin/ADV staff, wine ERP | SAP/Sage X3, in-house IT |
| Buys tools? | Price-sensitive; trusts SGV and peers | Yes, needs integration | Uses big integrators |
| Best fit for agency | Packaged CRM + order portal + DRM/DAE assistant + Q4 campaigns | Custom workflows: allocations, importer CRM, BOB tenders, scraping prices and listings | Unlikely, except niche pilots |
| Also | **Brokers (~40)**: concentrated, document-heavy, high-value niche | | |

---

## Sources (consulted through search summaries; direct fetch was blocked)

1. Pleinchamp – 2025 sales down for third year: https://www.pleinchamp.com/actualite/les-ventes-de-champagne-en-baisse-pour-la-3eme-annee-consecutive
2. Pleinchamp – 2025 yield 9,000 kg/ha: https://www.pleinchamp.com/actualite/le-rendement-commercialisable-du-champagne-fixe-a-9000-kg-ha-en-2025-en-baisse-pour-la-3eme-annee-consecutive
3. LSA – 2025 sales: https://www.lsa-conso.fr/champagne-pour-la-troisieme-annee-consecutive-les-ventes-sont-en-baisse-en-2025,464047
4. Meininger – 2025 by category: https://www.meininger.de/en/meiningers-international/champagne/champagne-sees-sales-decline
5. Wine Industry Advisor – 266 M: https://wineindustryadvisor.com/2026/01/21/champagne-266-million-bottles-shipped-in-2025/
6. Drinks Business – 2025 shipments: https://www.thedrinksbusiness.com/2026/01/global-champagne-shipments-fall-by-2-in-2025/
7. Sophie Claeys – H1 2026: https://lachampagnedesophieclaeys.fr/expeditions-de-champagne-lexport-tire-la-croissance-au-premier-semestre-2026/
8. Vinabox – 2026 export: https://www.vinabox.fr/actu/filiere-business/champagne-2026-export-croissance-france-baisse/
9. Vitaceae – filière: https://vitaceae.fr/observatoire/filiere-champagne/
10. Vitaceae – yields and reserve: https://vitaceae.fr/observatoire/rendement-et-reserve-champagne/
11. Vitaceae – fermage grape prices: https://vitaceae.fr/observatoire/fermage-viticole/champagne/prix-du-raisin-fermage-par-commune/
12. La Champagne Viticole – 2025 grape price for rents: https://lachampagneviticole.fr/prix-du-raisin-2025-pour-le-paiement-des-loyers-viticoles/
13. La Champagne Viticole – 2026 reserve: https://lachampagneviticole.fr/vendange-2026-la-reserve-individuelle-pour-amortir-le-deficit-de-recolte/
14. CGT Reims (Cerfrance price data): https://www.cgtchampagnereims.fr/vendanges-2026-lor-du-raisin-les-miettes-aux-salaries/
15. DGCCRF – Champagne enquiries: https://www.economie.gouv.fr/dgccrf/champagne-les-principaux-enseignements-des-enquetes-conduites-en-2020-et-2021
16. INAO – SGV/CIVC doc: https://inao.gouv.fr/sites/default/files/2024-09/05-SGV%20CIVC%20Champagne.pdf
17. UMC – courtiers: https://maisons-champagne.com/fr/filiere/associations-professionnelles/article/les-courtiers-en-vins-de-champagne
18. UMC – organisation of transactions: https://maisons-champagne.com/fr/filiere/developpement-durable-champagne/economie/article/l-organisation-des-transactions-entre-les
19. UMC – les vignerons: https://maisons-champagne.com/fr/encyclopedies/histoire-du-champagne/deuxieme-partie-connaissance-du-champagne/chapitre-7-les-professions-du-champagne-et-l/article/les-vignerons
20. UMC – les prix: https://maisons-champagne.com/fr/encyclopedies/histoire-du-champagne/deuxieme-partie-connaissance-du-champagne/chapitre-12-le-commerce-du-champagne/article/les-prix
21. SPCVC (presentation, charter, decision 187): https://www.spcvc.com/ ; https://www.spcvc.com/deontologie ; https://www.spcvc.com/ouvrir/document/decision-n187du-14-decembre-2018
22. BO Agri – CIVC decision 192-2 / supply agreement: https://info.agriculture.gouv.fr/boagri/document_administratif-81b5a070-25dd-48dc-b072-1ad365073d14/telechargement
23. Vinetur – 15% purchase ceiling 2026: https://www.vinetur.com/fr/20260904106640/france-raises-champagne-growers-purchase-ceiling-to-15-for-the-2026-harvest.html
24. L'Officiel des métiers – 5%→15%: https://www.lofficieldesmetiers.fr/champagne-le-plafond-dachat-de-raisins-passe-de-5-a-15/
25. Euronews – 50% harvest collapse: https://www.euronews.com/business/2026/09/09/why-a-50-harvest-collapse-wont-leave-shelves-short-of-champagne
26. 12x75 – production −49%: https://www.12x75.com/champagne-production-falls/
27. France 3 – 2026 yield: https://france3-regions.franceinfo.fr/grand-est/marne/epernay/vendanges-2026-en-champagne-le-rendement-commercialisable-fixe-a-8800-kg-de-raisin-a-l-hectare-a-nouveau-en-baisse-3390265.html
28. Economie Matin – 15% alcohol derogation: https://www.economiematin.fr/champagne-autorisation-exceptionnelle-commercialiser-jusqu-15-alcool
29. Lanson-BCC 2025 results: https://www.boursedirect.fr/fr/actualites/categorie/actualites-financieres/lanson-bcc-a-realise-un-resultat-net-de-16-2-meur-en-2025-zone-bourse-c20b79cb5c0b07c1195d5ca9809e918d7eec931e ; AMF filing https://echanges.dila.gouv.fr/OPENDATA/AMF/ECO/2026/03/FCECO081216_20260311.pdf
30. Maison Pommery 2025: https://www.boursedirect.fr/fr/actualites/categorie/chiffre-d-affaires/maison-pommery-une-activite-2025-en-leger-retrait-boursier-38fc547ac38c5b27322c6419aeccc7fe89e4bb3b
31. Laurent-Perrier FY25-26: https://www.optionfinance.fr/info-financiere-en-continu/d/2026-05-29-laurent-perrier-accroit-legerement-son-resultat-net-annuel.html
32. La Libre – Heidsieck & Co sale: https://www.lalibre.be/economie/entreprises-startup/2025/09/25/vranken-pommery-vend-heidsieck-co-a-lanson-bcc-YYPTV3DRD5CRDILYAQOSA74EL4/
33. LSA – TEVC 2024: https://www.lsa-conso.fr/champagne-tevc-nicolas-feuillatte-affichent-une-activite-en-croissance,461245
34. FoodBusinessMEA – LVMH 22% share: https://www.foodbusinessmea.com/lvmh-wine-and-spirits-revenue-falls-5-in-2025-as-champagne-shows-resilience/
35. inside.beer – Moët Hennessy cuts: https://www.inside.beer/news/detail/france-moet-hennessy-to-cut-10-of-global-workforce
36. Pleinchamp – US 15% tariff: https://www.pleinchamp.com/actualite/droits-de-douane-americains-sur-le-vin-le-taux-de-15-confirme-la-filiere-decue-mais-pas-resignee
37. IÉSEG – export price drop: https://insights.ieseg.fr/wp-content/uploads/2026/03/Forte-baisse-des-prix-de-depart-en-euros-du-Champagne-Cognac-et-vins-exportes-par-la-France-vers-les-Etats-Unis-en-2025-a-cause-des-droits-de-douane-1.pdf
38. Assemblée nationale QE 12362 (tariffs, Aube): https://www.assemblee-nationale.fr/dyn/17/questions/QANR5L17QE12362
39. Réussir – SGV commercial support / EU excise: https://www.reussir.fr/vigne/le-syndicat-general-des-vignerons-de-champagne-plaide-pour-des-mesures-daccompagnement-commercial
40. Réussir – low prices in GD: https://www.reussir.fr/les-prix-bas-du-champagne-font-debat
41. Economie Matin – Christmas 2025 prices: https://www.economiematin.fr/?p=175195
42. Vinexposium – Wine Paris 2026 results: https://www.vinexposium.com/wp-content/uploads/2026/02/CP_WINE-PARIS-2026_BILAN_FR.pdf
43. Vitisoft – GAMMA 2: https://vitisoft.fr/blog/gamma-2-circulation-vins-dae-daes/
44. Wineriz – GAMMA2 / DRM guides: https://www.wineriz.com/gamma2-douane-domaine-viticole-guide/ ; https://www.wineriz.com/drm-vin-guide-complet-declaration-recapitulative-mensuelle/
45. Vitisphere – compte unique viticole: https://www.vitisphere.com/actualite-105631-ladministration-travaille-au-compte-unique-viticole-entre-la-complexification-mvv-gamma-2-et-vendanges-et-la-fusion-du-dai-de-la-declaration-de-stock-et-de-la-drm-daout.html
46. Douane – VENDANGES service (CIVC exception): https://www.douane.gouv.fr/fiche/informations-sur-le-service-en-ligne-vendanges
47. Douane – simplification / CRD: https://www.douane.gouv.fr/actualites/simplification-administrative-pour-les-professionnels-du-vin
48. Réussir – Baqio Champagne module: https://www.reussir.fr/vigne/baqio-adapte-son-logiciel-aux-vignerons-champenois
49. Arcanes – Sage X3 wine customs: https://www.arcanes.info/2026/06/26/declarations-douanieres-vin-sage-x3/
50. Le Temps – harvest labour / 120k pickers: https://www.letemps.ch/economie/apres-quatre-morts-et-des-soupcons-de-traite-d-etres-humains-les-vendanges-sous-haute-surveillance-en-champagne
51. La Libre / Brut – trafficking trial: https://www.lalibre.be/economie/emploi/2025/06/18/vendanges-en-champagne-un-proces-pour-traite-detre-humain-souvre-ce-jeudi-QO7B2EKMQJFD7OPOIKF3W3XSYE/ ; https://www.brut.media/fr/articles/france/justice-faits-divers/vendanges-en-champagne-prison-ferme-pour-traite-detres-humains
52. Pleinchamp 2018 – succession tax: https://www.pleinchamp.com/actualite/vigne-vin~champagne-trop-taxes-certains-petits-vignerons-renoncent-a-vendre-des-bouteilles
53. La Champagne Viticole – 2025 Finance Law transmission: https://lachampagneviticole.fr/en/loi-de-finances-pour-2025-une-avancee-majeure-pour-la-transmission-des-exploitations-viticoles/
54. Wine Business International – grower share: https://www.wine-business-international.com/wine/insights-wine/grower-champagne-success-story-never-happened
55. Persée 1999 – grower structure: https://www.persee.fr/doc/rgpso_1276-4930_1999_num_6_1_2715
56. Autorité de la concurrence 96-D-59: https://www.autoritedelaconcurrence.fr/sites/default/files/commitments/96d59.pdf
57. Assises Oenotourisme 2025 PR: https://extranet.aube-champagne.com/assets/uploads/sites/34/2025/03/COMMUNIQUE-DE-PRESSE-2e-Assisses-de-lOenotourisme-en-Champagne.pdf
58. Vignobles & Découvertes observatory: https://tourisme-en-champagne.com/assets/uploads/2025/07/chiffres-de-loenotourisme-enquete-vd-2019-2020-pour-diffusion.pdf
59. TradingSat – Lanson Q4 seasonality: https://www.tradingsat.com/lanson-bcc-FR0004027068/actualites/lanson-bcc-les-ventes-de-lanson-ont-grimpe-de-82-au-4e-trimestre-503943.html
60. EC state aid – CIVC parafiscal tax: https://ec.europa.eu/competition/state_aid/cases/137103/137103_451315_4_2.pdf
61. Agra – CNAOC simplification: https://www.agra.fr/vin-la-cnaoc-appelle-poursuivre-le-choc-de-simplification-administrative
62. INSEE – houses bought 59.2% of crop (2014): https://www.insee.fr/fr/statistiques/2018375

**Open questions for follow-up** (search budget exhausted):
- the current CIVC contribution rates (2026 arrêté)
- the broker commission %
- the exact grape payment schedule under Decision 196
- the 2025 SPCVC mercuriale
- how many RMs use a wine ERP
- time spent on admin per domaine (worth asking in interviews)
- 2026 grape prices after the short crop
- TEVC 2025 figures
