# 04 — Small champagne producers: commercial and operational reality, digital maturity, competitors and go-to-market

*Research agent 04, 2026-10-07. Scope: récoltants-manipulants (RM), small co-ops, family maisons.*

> **Method and limitations (read first).** In this environment the WebFetch tool could not resolve any domain (DNS `ENOTFOUND` on every site, including champagne.fr and lsa-conso.fr), and direct `curl` was blocked by the proxy. All evidence therefore comes from **web-search result extracts** (about 45 searches in French and English) until the team's shared search budget ran out. The consequences:
> - I could not open producers' HTML, so **platform detection (Shopify, Woo, Wix and so on) is mostly inferred** from URL patterns (`/wp-content/` means WordPress; `...-pages-...-fr-0-261-26.html` matches the Enovanet/eChampagne CMS; `Fichier.ashx?SITE=` is a hosted vendor CMS). Treat it as indicative.
> - The search budget ran out before I covered **international wine-tech (Bottlebooks, Preferabli, SevenFifty/Provi, Commerce7)**, **salons**, **Instagram usage** and the **Village by CA, Lycée d'Avize and CCI** ecosystem. Those items are marked *[background knowledge, not verified]* or *[to verify]*.
> - Every claim tagged **(V)** is verified by the cited source. Claims tagged **(E)** are my estimates or inferences.

---

## 1. Executive summary

1. **The market is under pressure, and that creates the need for new customers.** Champagne shipments fell for a third year in a row in 2025, to 266M bottles (−1.8%), after −8.2% in 2023 and −9.2% in 2024 (V, [LSA](https://www.lsa-conso.fr/champagne-pour-la-troisieme-annee-consecutive-les-ventes-sont-en-baisse-en-2025,464047); [Pleinchamp](https://www.pleinchamp.com/actualite/les-ventes-de-champagne-en-baisse-pour-la-3eme-annee-consecutive)). Growers shipped 53.6M bottles in 2024 (19.7% of the total, −5.5%). They were still −4.5% year to date at end-November 2025 (V, [Sophie Claeys](https://lachampagnedesophieclaeys.fr/maisons-vignerons-cooperatives-analyse-detaille-des-chiffres-des-expeditions-de-champagne-2024/); [Claeys Nov 2025](https://lachampagnedesophieclaeys.fr/les-expeditions-de-champagne-chiffres-et-tendances-a-fin-novembre-2025/)). Stocks are estimated at about 1.28bn bottles, roughly 4.7 years of sales. US tariffs rose to 15% from 7 August 2025 (V, [linfodurable](https://www.linfodurable.fr/champagne-une-vendange-2025-de-qualite-mais-des-vignerons-tres-inquiets-53102)). The 2026 recovery is driven by export: France −3%, export +7.5% to end-August 2026, and growers' exports +5.1% (6.2M bottles) (V, Claeys). **Growers need export and new direct customers. Their traditional French private clientele is ageing and shrinking.**
2. **Ordering is still largely analogue.** Nationally, 79% of winegrowers have a website, but only **21% sell through their own e-commerce site** (V, Afnic survey Dec 2025 via [Pleinchamp](https://www.pleinchamp.com/actualite/les-vignerons-a-la-vigne-a-la-cave-sur-les-salons-et-sur-le-web)). The Vin & Société 2024 barometer gives 82% with a website and 40% with e-commerce, with "lack of time" as the main barrier (V, [Vin & Société](https://www.vinetsociete.fr/etude/barometre-usages-numeriques-filiere-vin/)). In my 25-producer sample, about **70% of producers whose ordering method I could identify still rely on a PDF or paper *bon de commande*, phone, email, cheque or bank transfer** (E, sample biased; see section 2).
3. **A champagne-specific digital supply already exists, but it is thin.** It covers e-commerce (Shop&Champ', eChampagne/Enovanet), regulatory and cellar software (Vrille, Isagri, Vitisoft, iDSystèmes), booking marketplaces (Winalist, Rue des Vignerons) and, since 2025–26, **several Reims/Épernay "AI agencies"** (Zaplo Studio, Mankova Consulting, A2Z Automation, Juwa, IA Agency, Watizi). **Nobody visible yet sells a packaged, grower-specific "back office plus customer reactivation plus export prospecting" automation.** Most AI-agency pages are SEO landing pages with no named champagne references.
4. **The best wedges for a small AI agency (E):**
   - (a) turn the bon de commande into a digital order flow connected to a CRM;
   - (b) reactivate the existing client file, with automated Q4 mailings and reorder reminders;
   - (c) prospect export importers and French cavistes/CHR (cavistes are moving to growers and co-ops; V, [Vitisphere](https://www.vitisphere.com/actualite-100898-faute-de-grandes-maisons-de-plus-en-plus-de-cavistes-vont-vers-les-champagnes-de-vignerons-et-de-cooperatives.html));
   - (d) a multilingual email and visit-booking assistant;
   - (e) automate invoices, payment chasing and shipping labels.
   
   Timing matters: **avoid mid-August to end-September (harvest) and November–December (gifting crunch)** for delivery projects (V, [Juwa](https://juwa.co/blog/actualites-tendances-ia/pme-reims-automatisation-ia/)).

---

## 2. Ground truth: a sample of 25 producers

Below is how a sample of small producers sell, as visible in search extracts. "Ordering mode" is the main way a private customer orders.

| # | Producer (village, area) | Website / platform clue | Ordering mode | Price list / bon de commande | Other digital signals | Source |
|---|---|---|---|---|---|---|
| 1 | Jean-Guy Viot (Marne) | Yes, **WordPress** (`/wp-content/`) (V) | **Download the PDF, return it by post or email.** Shipping cost is quoted afterwards | 2026 PDF bon de commande; Brut Tradition €17 | Order page about 233 days old | [PDF](https://www.jean-guy-viot.fr/wp-content/uploads/2026/02/Bon-commande-JG-Viot-2026.pdf), [page](https://www.jean-guy-viot.fr/commande/) |
| 2 | Champagne Labbé (Montagne de Reims) | Yes, plain http site | **PDF plus cheque to accompany the order** | PDF valid 25/09/2025–02/08/2026; Brut €15, BdB €18; shipping scale by bottle count | — | [PDF](http://www.champagne-labbe.fr/bon_de_commande.pdf) |
| 3 | Baudot Père & Fils | Yes, hosted vendor CMS (`Fichier.ashx?SITE=5031`) (E) | **PDF by post or email; cheque or transfer** | Still a **2023** form online (stale) | — | [PDF](http://www.champagnebaudot.fr/Fichier.ashx?SITE=5031&FILE=bon+de+commande+2023c.pdf) |
| 4 | Alain Bedel (Vallée de la Marne) | Yes, URL pattern of the **Enovanet/eChampagne CMS** (E) | Bon de commande page; **bank details emailed with confirmation**; goods ship once payment arrives | Yes | — | [page](https://www.champagne-bedel.com/vin-de-champagne-pages-Bon-de-commande-fr-0-261-26.html) |
| 5 | De Rekeneire | Yes, same Enovanet-type pattern (E) | Order form; cheque or transfer, RIB sent by email | Yes | — | [page](https://www.champagne-de-rekeneire.fr/producteur-champagne-page-Commander-fr-0-10-0.html) |
| 6 | Trichet-Lorain | Yes (`/bon-de-commande/`, probably WordPress) (E) | Bon de commande; **pay by cheque or transfer on receipt of invoice** | Yes | — | [page](https://www.champagnetrichet-lorain.fr/bon-de-commande/) |
| 7 | Arthoine | Yes | Terms say: **"print your bon de commande and send it with your cheque"** | Yes | — | [CGV](https://www.champagne-arthoine.com/cgv.html) |
| 8 | Poinsot Frères (Loches-sur-Ource, Aube) | Yes | **Phone or email to a named family member**; full prepayment | PDF tariff made for **members of a trade association (CAPEB Aube)**, i.e. an association/CE channel | Inconsistent validity dates in the PDF | [PDF](https://www.capeb.fr/www/capeb/media//aube/document/Tarif%20fin%202025%20Adhérents%20CAPEB%20-%20Champagne%20Poinsot%20Frères.pdf) |
| 9 | Yveline Prat (Vert-Toulon, Marne) | Yes, custom PHP | **Online order page with automatic shipping calculation**; ships in 3–5 days; phone line Mon–Sat | Public price list valid to 31/10/2026; Brut €17.30 | — | [order](https://www.champagneprat.com/commander/commander.php), [prices](https://www.champagneprat.com/commander/champagne-prix.php) |
| 10 | Yves Barbaray (Soilly-Dormans) | Yes | Public prices; **customer-service phone line** | Prices on site (Prestige €17) | Gîte on the estate | [site](https://www.yvesbarbaray.com/) |
| 11 | Cornevin (Côte des Bar) | Yes (`tarifs-bons-de-commande.html`) | **Bon de commande**, with delivered-price grids | €28 single bottle, €22 per 6–12, €17.50 ex-cellar | — | [page](https://www.champagne-cornevin.fr/tarifs-bons-de-commande.html) |
| 12 | René Jolly (Landreville, Aube), about 14 ha, ≤35k bottles | Yes (jollychamp.com) | **Email or phone**; ships to mainland France only | — | **More than 50% exported**; UK agent; Waitrose listing; exhibitor at London Wine Fair (on Bottlebooks) | [site](https://www.jollychamp.com/), [Hachette](https://www.hachette-vins.com/guide-vins/producteurs/6426/champagne-rene-jolly/), [LWF](https://bottlebooks.londonwinefair.com/producers/5558a429cbf8c2aeb644f741) |
| 13 | François Girard (Le Mesnil-sur-Oger) | Yes | **Online cart and checkout** | — | — | [site](https://www.champagne-francois-girard.com/) |
| 14 | Claude Cazals (Le Mesnil-sur-Oger) | Yes (FR/EN) | No e-shop visible; on-site sales and visits | Not found | Sold via Swiss retailers | [site](https://www.champagne-cazals.fr/), [G&M](https://fr.gaultmillau.com/en/wineries/claude-cazals/carte-or-bsa) |
| 15 | Denis Frézier (Monthelon), 5.6 ha | Yes | **Online shop ("Mon Panier")** | — | HVE/VDC certified | [cart](https://www.champagne-frezier.com/Mon-Panier) |
| 16 | Météyer Père & Fils (Trélou-sur-Marne) | Yes (`index.php`) | Unclear. A visitor review *"hopes to order online in future"*; another praises order handling | — | Visits and B2B experiences sold via winetourism.com; closed weekends | [site](https://www.champagne-meteyer.com/index.php), [winetourism](https://www.winetourism.com/fr/experience/dans-champagne-b2b/) |
| 17 | Yves Meunier & Fils (Châtillon-sur-Marne) | Yes | **Call us for prices and delivery** | No public price list | — | [page](https://www.champagne-yves-meunier-fils.com/notre-culture-4) |
| 18 | R. Gerbaux (Vallée de la Marne) | Yes, URL pattern resembles PrestaShop (E) | Online product pages with prices | Yes | — | [page](https://www.champagne-gerbaux.com/fr/10-vente-directe-de-champagne-dans-la-vallee-de-la-marne) |
| 19 | Bourcier (Marne) | Yes | Online and at the estate; **mobile numbers as main contact** | — | Tasting every day | (search extract, Vallée de la Marne query) |
| 20 | Tarlant (Œuilly) | Yes (tarlant.com, unconfirmed) | No own e-shop surfaced; **sold through about 6 online retailers** (Plus de Bulles, La Champagnerie and others) | — | Visits by reservation, €15/€25, booked through the departmental tourism site; harvest-period appointments | [tourisme](https://www.tourisme-en-champagne.com/champagne-tarlant/oeuilly/deg0000000000209), [Plus de Bulles](https://www.plus-de-bulles.com/fr/147-champagne-tarlant) |
| 21 | André Chemin (Sacy, Montagne de Reims) | — | Sold via **Champagne Terroir** grower marketplace (free shipping from 6 bottles) | — | — | [Champagne Terroir](https://www.champagne-terroir.fr/andre-chemin/178-champagne-andre-chemin-brut-tradition.html) |
| 22 | Guy Charbaut (Mareuil-sur-Aÿ) | Yes | — | — | **Visits bookable on Winalist** (instant confirmation, €17–29) | [Rue des Vignerons](https://www.ruedesvignerons.com/en/domaine/457/champagne-guy-charbaut) |
| 23 | Larmandier-Bernier (Vertus), 18 ha | Yes | No own shop surfaced; partner retailer Comptoir des Millésimes sells "direct from the estate" | — | Strong export and critic scores | [CdM](https://www.comptoirdesmillesimes.com/larmandier-bernier/terre-de-vertus-1er-cru-brut-nature-2018-larmandier-bernier.html) |
| 24 | Pierre Gimonnet & Fils (Cuis) | Yes | On-site sales; phone | No public FR price found | Heavy export (Canada, Australia) | [Hachette](https://www.hachette-vins.com/guide-vins/producteurs/3286/pierre-gimonnet-et-fils) |
| 25 | Fleury (Courteron, Côte des Bar), 15 ha | Yes | On-site sales; accommodation | — | 4th generation | [G&M](https://fr.gaultmillau.com/wineries/fleury) |

**Reading the sample.**
- **Ordering mode identifiable for 19 of 25.**
  - **Offline (PDF or paper form, phone, email, post, cheque or transfer): 13–14** (Viot, Labbé, Baudot, Bedel, Rekeneire, Trichet-Lorain, Arthoine, Poinsot, Barbaray, Cornevin, Jolly, Meunier, Cazals, probably Météyer). That is **about 70%**.
  - **Real online cart: 5** (Prat, Girard, Frézier, Gerbaux, Bourcier), about 26%.
  - Several better-known growers (Tarlant, Larmandier-Bernier, Gimonnet) push online sales to **retailers** rather than running their own shop.
- **Bias warning (E).** Several searches targeted the phrase "bon de commande", which over-samples offline sellers. Combining the sample with the Afnic national figure (21% with own e-commerce) and the Vin & Société figure (40% e-commerce, all wine actors), I estimate **65–80% of champagne RMs still take most private orders via bon de commande, phone or email**. Even those with a cart typically handle CE, caviste and export orders by email and invoice.
- **Recurring pain signals (V):**
  - stale forms left online (Baudot's 2023 form);
  - inconsistent validity dates (Poinsot);
  - shipping "quoted afterwards" (Viot);
  - "bank details sent by email" (Bedel, Rekeneire);
  - payment chased by cheque on receipt of invoice (Trichet-Lorain).
  
  Each is a manual step: re-keying, a quote email, payment matching, then the shipment.
- **Price points (V):** Brut Tradition sells at **€15–17.50 ex-cellar** (Labbé, Viot, Prat, Barbaray, Cornevin), and €22–28 delivered. Average private orders are therefore small (E: about €150–400 per order of 6–24 bottles). This is one reason growers are price-sensitive about software. **Sell on time saved and orders recovered, not on technology.**
- **Platforms (E):** a patchwork of WordPress, custom PHP, local-agency CMSs (Enovanet/eChampagne URL patterns appear at least 2–3 times), PrestaShop-like stores and hosted vendor CMSs. No Shopify store was observed in the sample. Local agencies quote €999–€4,500 for a site (section 6).
- **Visits.** Booking is increasingly outsourced to **Winalist, Rue des Vignerons, winetourism.com and the departmental tourism site** (V, rows 16, 20, 22). Few small growers run their own booking engine.

---

## 3. Customer base and prospecting of a typical grower

**Verified:**
- **Volume split.** Of 271.4M bottles in 2024, maisons shipped 194M (71.5%), growers 53.6M (19.7%) and co-ops 23.8M. The French market is 118.2M (−7.2%), and export is 56.4% of volume and about 64% of value (V, [Claeys](https://lachampagnedesophieclaeys.fr/maisons-vignerons-cooperatives-analyse-detaille-des-chiffres-des-expeditions-de-champagne-2024/)). In 2025 France accounted for about 114M bottles (V, [LSA](https://www.lsa-conso.fr/champagne-pour-la-troisieme-annee-consecutive-les-ventes-sont-en-baisse-en-2025,464047)). Growers are historically much more France-centric than maisons, and their growth in 2026 comes from export (+5.1%).
- **Ageing clientele.** The Chambre d'agriculture says growers develop oenotourism partly *"to renew an ageing clientele"* and gain visibility (V, [La Champagne Viticole](https://lachampagneviticole.fr/oenotourisme-les-chambres-dagriculture-accompagnent-les-vignerons-de-lidee-au-projet/)).
- **Cavistes are switching.** *"For lack of big-house allocations, more and more cavistes are turning to growers' and co-op champagnes"* (V, [Vitisphere](https://www.vitisphere.com/actualite-100898-faute-de-grandes-maisons-de-plus-en-plus-de-cavistes-vont-vers-les-champagnes-de-vignerons-et-de-cooperatives.html)). The Cavistes de France federation held its congress in Champagne (V, [Claeys](https://lachampagnedesophieclaeys.fr/les-cavistes-de-france-en-champagne-le-13-et-14-septembre-etat-des-lieux-prospective-et-chiffres/)).
- **Associations and CE.** Poinsot Frères publishes a dedicated tariff for members of the Aube building-artisans federation (CAPEB) (V, row 8). This is typical of the *comité d'entreprise / association* channel.
- **Export through agents and fairs.** René Jolly exports more than half its output, has a UK agency, a Waitrose listing and a London Wine Fair stand (V, row 12). Shop&Champ's guide stresses retaining *"known customers, occasional or long-standing"* and following up even 1–2-bottle buyers *"year after year by email or paper mailing"* (V, [Shop&Champ guide](https://shopandchamp.fr/guide-e-commerce-vigneron-champagne)).
- **Co-op group example.** Terroirs & Vignerons de Champagne grew 3% in 2024, driven by on-trade (CHR and wholesalers), while cavistes and B2B were difficult (V, [Claeys](https://lachampagnedesophieclaeys.fr/terroirs-vignerons-de-champagne-croissance-de-3-en-2024-malgre-un-marche-mondial-en-recul/); [Agra](https://www.agra.fr/articles/champagne-les-ventes-de-tevc-ont-resiste-en-2024-grace-des-leviers-de-croissance)).
- **Online intermediaries:** grower marketplaces (Champagne Terroir, the Vignerons Indépendants shop fulfilled by Les Grappes Services, La Vignery, Vignartea) and online cavistes (Plus de Bulles, La Champagnerie, Vinatis) (V, [Champagne Terroir](https://www.champagne-terroir.fr/); [VI boutique](https://boutique.vignerons-independants.com/vin-champagne/region-5)).

**Estimates (E), from industry knowledge and needing validation in interviews:**
- **Channel mix.** For a typical 5–10 ha RM selling 30–80k bottles: private French clients 40–60% (a file of 500–3,000 households, many reordering yearly in Q4, some in Belgium), CE and associations 5–15%, cavistes and restaurants 10–25%, export via 1–5 importers 10–40%. Prestige growers are often export-majority.
- **Prospecting** relies on salons. Expected list *[not verified in this run]*: Wine Paris (February), Salon des Vignerons Indépendants (Paris, Lille, Strasbourg and others), Le Printemps des Champagnes and Terres et Vins de Champagne (April, Reims/Épernay), ProWein, plus local Christmas markets. Other routes: commission-based *agents commerciaux* and importer visits. Little systematic outbound prospecting is done. **This gap is a clear opportunity for scraped caviste, restaurant and importer lead lists plus personalised email sequences.**

---

## 4. Marketing reality

- **Web and social (V).** 79% of winegrowers have a website and 92% are on social networks, versus 27% and 65% for agriculture overall (Afnic Dec 2025 via [Pleinchamp](https://www.pleinchamp.com/actualite/les-vignerons-a-la-vigne-a-la-cave-sur-les-salons-et-sur-le-web)). The Vin & Société 2024 barometer gives an overall digital maturity score of **47/100**; the main barriers are lack of time, then lack of money (V, [Vin & Société](https://www.vinetsociete.fr/etude/barometre-usages-numeriques-filiere-vin/)).
- **Social-media workload (V).** Keeping two networks alive needs a *"realistic minimum of 3–5 hours a week"* ([Farman](https://www.farman-communication.com/community-management-pour-vignerons-en-2026-quel-reseau-social-choisir-selon-votre-cible/)). A generalist agency posting package costs about €490/month excluding VAT (V, search extract). All communication must follow the **loi Évin**, which local agency Ampelios explicitly highlights (V, [Ampelios](https://ampelios.com/agence-de-communication-vin-champagne/)). An AI content pipeline must build in Évin-compliant guardrails.
- **Collective brand (V).** "Champagne de Vignerons", created in 2001 by the SGV, runs a site with a search by name, village or region and an **interactive map of cellars, tastings and shops** ([champagnedevignerons.fr](https://www.champagnedevignerons.fr/vignerons/cote-des-bar/), [.com](https://www.champagnedevignerons.com/)). See also the 2001 creation note in [this hospitality-school document](https://hotellerie-restauration.ac-normandie.fr/IMG/pdf/partenariat_champagnes_de_vignerons-enjeux_et_mode_d_emploi.pdf).
- **Oenotourism (V).**
  - Visits for small houses cost €13–50 per person on Winalist and Rue des Vignerons (Hautvillers, Aÿ and Mareuil listings).
  - The Chambres d'agriculture run a support programme for growers' tourism projects ([La Champagne Viticole](https://lachampagneviticole.fr/oenotourisme-les-chambres-dagriculture-accompagnent-les-vignerons-de-lidee-au-projet/)).
  - Rue des Vignerons charges about **€15 excluding VAT per booking**; payment is made at the estate ([affi.io](https://affi.io/m/rue-des-vignerons), pre-2021 data).
  - Atout France runs an annual oenotourism barometer with Rue des Vignerons ([Tourmag](https://www.tourmag.com/Futuroscopie-Le-marche-de-l-oenotourisme-en-mouvement-ABO_a126159.html)).
  - Wine Paris 2025 ran a session titled *"CRM, POS, social networks: digital is the armed wing of wine tourism and direct sales"* ([Wine Paris](https://wineparis.com/newfront/sessions/14278)). That shows the topic is mainstream with buyers.
- **Languages (E).** Export-oriented growers have FR/EN sites. One local agency explicitly sells FR/EN/DE/JA sites to champagne clients (V, [Zaplo](https://zaplostudio.com/implantations/agence-ia-epernay)). Watizi pitches agents for *"export clients writing in several languages"* (V). That suggests multilingual inbound email is a recognised pain. Chinese and Japanese demand was not verified in this run.

---

## 5. Admin and back office: who does the work

**Verified signals of manual work:**
- Payment flows are by cheque with the order, transfer with RIB sent by email, or cheque on receipt of invoice (rows 2–7).
- Shipping is quoted manually (row 1). Forms go stale (row 3).
- Contacts are named family members' phones and emails (rows 8, 12, 19).
- Estates close at weekends (row 16). Visits are by appointment only during harvest, 1 September to 17 December 2026 for Tarlant (row 20).
- Juwa's sector guide for Reims SMEs lists **export and customs documents, customer payment chasing and allocations** as the champagne automation targets. It warns: **never during mid-August to end-September, never in November–December** (V, [Juwa](https://juwa.co/blog/actualites-tendances-ia/pme-reims-automatisation-ia/)).
- **The e-invoicing mandate 2026–27** is pushing software upgrades. Vitisoft markets e-invoicing readiness (V, [Vitisoft](https://vitisoft.fr/)). This is a compliance trigger an agency can use.
- Champagne-specific regulatory admin includes the cellar register (*registre de cave*), the DRM and harvest declarations. It is handled by Isagri Isavigne, Vrille, Vitisoft and others (V, [Isagri](https://www.isagri.fr/solutions/de-la-tracabilite-des-vignes-a-la-commercialisation-de-vos-vins); [Vrille](https://www.vrille.io/)). **This is not the agency's battleground. Integrate with these tools; do not compete with them.**

**Estimates (E):**
- A typical RM runs on **2–5 family members plus 1–3 employees**. Back office (orders, invoices, shipping, payment chasing, emails) usually falls on one person, often the spouse or the next-generation family member, at **10–20 h/week, spiking to 30–50 h/week in October–December**. Q4 gifting represents roughly **35–50% of private-client annual volume**. Harvest (late August to September) freezes everything else.
- Customer files are typically in Isagri or Vitisoft (invoicing), plus an Excel/Outlook address book, plus paper. Segmentation is rare: no RFM, no lapsed-client reactivation.

---

## 6. Competitors and existing offers

### 6a. Competitor table

| Player | Type | Offer relevant to growers | Price (as published) | Evidence / notes |
|---|---|---|---|---|
| **Shop&Champ'** (Bezannes/Reims, since 2018) | Champagne-specific e-commerce | **Digitises the bon de commande**: public or hidden prices, minimum/maximum thresholds, mixed cases, volume pricing; plugs into existing invoicing ("no double invoicing"); Stripe / CA e-Transactions | Not published; **no commission on sales** | [home](https://shopandchamp.fr/), [solution](https://shopandchamp.fr/solution), [LinkedIn](https://www.linkedin.com/showcase/shop-and-champ). **Closest direct competitor for order digitisation** |
| **eChampagne.pro** (Formalog/Enovanet, Château-Thierry) | Champagne site builder | Site, admin, e-commerce adapted to champagne (multi-tariff, public or private order forms, shipping calculation), e-mailing module | "Price of a classic site" | [echampagne.pro](https://www.echampagne.pro/), [Enovanet](https://www.enovanet.fr/cms-creation-site-internet-web-design-chateau-thierry-produits-Site-internet-eChampagne-fr-10.html). Its URL pattern appears on several grower sites |
| **Vrille** | Champagne all-in-one SaaS (vineyard, harvest, cellar, AOC register) | Admin automation and document generation; CRM/invoicing not confirmed | €89–98/month, no commitment | [vrille.io](https://www.vrille.io/) |
| **Isagri Isavigne** | Wine management and invoicing; champagne specifics (register, RM/RC status) | Invoicing, stock, e-DRM | About €80–150/month (unsourced blog) | [Isagri](https://www.isagri.fr/solutions/de-la-tracabilite-des-vignes-a-la-commercialisation-de-vos-vins) |
| **Vitisoft** (Tours) | Commercial management; 2,000+ estates; CRM; e-invoicing | Invoices, stock, DRM | From €39/month plus €600 licence (excl. VAT) | [vitisoft.fr](https://vitisoft.fr/); about $1.1M raised in 2023 ([vcbacked](https://www.vcbacked.co/company/vitisoft)) |
| **iDSystèmes** (iDVinistoria, iDCrmPro) | ERP/CRM for maisons and co-ops; 450+ clients | Grape intake, harvest declarations | On quote | [idsystemes](https://www.idsystemes.com/logiciel-metier/maisons-champagne/) |
| **Cap Vignes** (on MS Dynamics BC) | ERP for maisons and négoce | CRM, pricing, Power BI | On quote | [cap-vignes.vin](https://cap-vignes.vin/) |
| **NSI-Sadimo Vinéa** | Commercial management | Invoicing, DRM/CRD | On quote | [nsi-sadimo](https://www.nsi-sadimo.com/logiciel-viticulture/vinea/gestion-commerciale-viticole.html) |
| **Wineriz** (Paris/Bordeaux, since 2020) | All-in-one commercial app with CRM | Sales, CRM | — | $2.1M seed (June 2024; SideAngels, Evolem) ([vcbacked](https://www.vcbacked.co/company/wineriz)); "fait un carton" ([Vitisphere](https://www.vitisphere.com/actualite-102229-lapplication-de-gestion-commerciale-wineriz-fait-un-carton.html)) |
| **Winalist** (founded in Aÿ-Champagne) | Oenotourism booking marketplace | 1,700+ partners, 10 countries | Commission | €0.5M (2019), about €1.3M (with Bpifrance, Grand-Est region, the Cointreau family), **€1M June 2025** for Portugal ([Drinks Business](https://www.thedrinksbusiness.com/2025/06/french-wine-tourism-firm-secures-e1m-in-funding/), [UPTEC](https://uptec.up.pt/uptec-startup-raises-e1-million-to-boost-wine-tourism-in-portugal/)) |
| **Rue des Vignerons** | Oenotourism booking | 300+ estates | About €15 excl. VAT per booking | [affi.io](https://affi.io/m/rue-des-vignerons) |
| **Champagne Terroir; VI boutique / Les Grappes; La Vignery; Vignartea** | Grower marketplaces | Online sales for growers without their own shop | Margin or commission | [Champagne Terroir](https://www.champagne-terroir.fr/), [VI](https://boutique.vignerons-independants.com/vin-champagne/region-5) |
| **ID Design** (Reims) | Web agency | Vitrine from €1,350; e-commerce €1,200–2,350 (Colissimo, stock, invoicing) | Published | [iddesign](https://iddesign.pro/creation-de-site-internet-pour-les-vignerons-de-champagne) |
| **Webchampagne; Nity Pro; CP Création (Épernay, since 1993); Vroska; Be Web Form&Com** | Local web agencies | Grower sites | Webchampagne €999/€1,799; Nity from €59/month | [webchampagne](https://webchampagne.fr/), [nity](https://nity.pro/champagne), [cpcreation](https://www.cpcreation.fr/), [vroska](https://agence-vroska.fr/agence-web-a-epernay), [beweb](https://beweb-formcom.com/creation-sites-web/) (clients include G. Mahé and Caillot-Thibault) |
| **Zaplo Studio** (Épernay/Reims, two sole traders) | **"AI & web agency"** | Multilingual sites, direct e-commerce, **client allocations**, AI automation for RMs, co-ops and maisons | Vitrine from €4,500; e-commerce plus allocations plus 4 languages €8–18k; AI from €2,500 | [zaplostudio](https://zaplostudio.com/implantations/agence-ia-epernay). **Most direct positioning overlap**; no named references |
| **Mankova Consulting** (Reims) | AI consulting for champagne and agri-food | Multilingual chatbots, smart visit booking, dynamic pricing; free diagnostic | — | [mankova](https://mankova-consulting.com/ia-automatisation-agence-reims) |
| **A2Z Automation** (Reims) | n8n/Make/Zapier automation | Lists **maisons de champagne among its most active sectors**; lead-qualification agents | — | [a2z](https://a2z-automation.com/agence-automatisation-a-reims/) |
| **Juwa; IA Agency; Watizi; Britweb; Pulsi; Impaakt** | Generalist AI/web agencies in Reims | Chatbots, agents. Impaakt did a CSGV (SGV co-op) vineyard geolocation project | — | [juwa](https://juwa.co/blog/actualites-tendances-ia/pme-reims-automatisation-ia/), [ia.agency](https://ia.agency/agence-ia-reims/), [watizi](https://watizi.com/agence-ia-reims), [britweb](https://britweb.fr/agence-ia-reims/), [impaakt](https://impaakt.fr/intelligence-artificielle-reims/) |
| **Freelance AI engineers** (for example Mehdi Challakh) | Freelance | Benchmark prices: targeted automation €2.5–15k; AI agent €6–25k | Published | [mehdichallakh](https://www.mehdichallakh.com/freelance-ia/reims/) |
| **Ampelios** (Reims); **e-CVB**; **Agence Marketing Vins Champagne**; **Hachetag** | Wine/champagne communication agencies | Social media (Évin-compliant), oenotourism training | About €490/month for posting packages (generic) | [ampelios](https://ampelios.com/), [e-cvb](https://e-cvb.com/) |
| International: **Bottlebooks** | Trade-fair and tech-sheet data platform | Used by the London Wine Fair for producer listings (V) | — | [LWF on Bottlebooks](https://bottlebooks.londonwinefair.com/producers/5558a429cbf8c2aeb644f741) |
| International *[background knowledge, not verified]* | — | SevenFifty (US trade marketplace, acquired by Provi in 2022); Preferabli (AI wine recommendation); Commerce7 and WineDirect (US DTC/club platforms); Vivino; Winerim (wine-list intelligence, joined La WineTech, V via [lawinetech.com](https://www.lawinetech.com/)) | — | Re-verify before citing |

### 6b. Competitive read (E)
- **Software vendors** (Isagri, Vitisoft, Vrille) own the system of record. They are integration targets, not rivals. **Shop&Champ' and eChampagne** own "digital bon de commande" e-commerce but not CRM intelligence, outbound prospecting or AI email handling.
- **A new crop of Reims "AI agencies" appeared in 2025–26.** Most are SEO-driven landing pages (many city pages, same template), with **no public champagne case studies**. A newcomer that arrives with 2–3 real grower case studies, champagne-specific templates (bon de commande parser, Q4 reactivation, importer prospecting, Évin-safe content) and **fixed-price packages** could differentiate quickly.
- **Price anchors in the region:** a site costs €1–4.5k; an AI automation €2.5k–15k; an agent €6–25k; SaaS €39–98/month. For a grower with €500k–1.5M in revenue (E), a credible offer is **€1.5–5k setup plus €150–400/month**. Pitch it against the cost of one seasonal admin hire or the margin on 300–500 extra bottles.

---

## 7. Ecosystem and go-to-market channels

### Verified institutions
- **SGV (Syndicat Général des Vignerons de la Champagne)**, 17 avenue de Champagne, Épernay. It has about 16,000 members, covering more than 99% of growers (figure from a third-party profile; the UMC says "over 15,000") ([UMC](https://maisons-champagne.com/en/industry/organisation/champagne-growers-and-houses/article/champagne-growers-union)). It owns the **Champagne de Vignerons** brand (2001) and the magazine **La Champagne Viticole** ([lachampagneviticole.fr](https://lachampagneviticole.fr/)).
- **Co-operatives:** about 14,174 growers are co-op members, around 70% of harvest declarants (secondary source, [geocaching page citing co-op data](https://www.geocaching.com/geocache/GCA6JQX_cooperative-de-chavot-courcourt); verify with the FCVC). **CSGV** is the SGV's co-op (it has already used Impaakt for a vineyard project). Groups such as **Terroirs & Vignerons de Champagne** and the Colombé-le-Sec co-op (59 growers, 110 ha; [G&M](https://fr.gaultmillau.com/fr/wineries/charles-clement)) market brands while serving thousands of members.
- **Comité Champagne:** shipment statistics and the magazine *Le Vigneron Champenois* ([subscription](https://levigneronchampenois.comitechampagne.fr/abonnement)).
- **Chambres d'agriculture (Marne/Aube):** an oenotourism support programme ([La Champagne Viticole](https://lachampagneviticole.fr/oenotourisme-les-chambres-dagriculture-accompagnent-les-vignerons-de-lidee-au-projet/)).
- **Vignerons Indépendants:** a federation with its own marketplace ([boutique](https://boutique.vignerons-independants.com/vin-champagne/region-5)).
- **La WineTech:** 98+ active members, 4 countries, 24 events/year ([lawinetech.com](https://www.lawinetech.com/); [Usine Digitale](https://www.usine-digitale.fr/article/food-tech-35-start-up-du-vin-se-federent-autour-de-la-winetech.N927174)).
- **Grand-Est Region and Bpifrance** co-invested in Winalist, so regional innovation money exists for wine-tech. Several Reims agencies mention public AI-adoption funding (not verified).
- **Trade press for visibility:** La Champagne Viticole, *Le Vigneron Champenois*, *La Champagne de Sophie Claeys* (blog), Vitisphere, Réussir Vigne.

### To verify (not covered in this run)
Le Village by CA Champagne-Bourgogne, Lycée viticole d'Avize (CFPPA training), CCI Marne digital programmes, the Bioeconomy cluster, the champagne vigneron Facebook groups, and the exact dates of salons (Printemps des Champagnes, Terres et Vins, Wine Paris).

### Go-to-market channels (ranked, E)
1. **Direct, local, relationship-led outreach** to 5–10 *jeune génération* growers (30–40-year-olds taking over), found through Instagram, Champagne de Vignerons map listings and salon exhibitor lists. Offer a fixed-price "bon de commande to online order plus CRM" pilot. **Sell from January to June**; never pitch in September or December.
2. **Partner with existing tool vendors and web agencies** (Shop&Champ', eChampagne/Enovanet, ID Design, CP Création, Vrille). They have the clients but no AI. White-label the automation layer: CRM sync, email agents, reactivation, prospecting.
3. **Co-ops and the SGV/CSGV as channels.** A single co-op deal (a member-facing order portal, or shared lead-gen for member brands) reaches hundreds of growers. Offer a talk or workshop on "AI for growers" through the SGV, the Chambre d'agriculture or the Avize training centre.
4. **Content and proof.** Publish a "Champagne grower digital barometer" built from a scrape of about 1,000 grower sites. This is exactly the analysis in section 2, done at scale, and is the agency's own scraping skill turned into marketing. Pitch it to La Champagne Viticole and Vitisphere.
5. **Salons as prospecting grounds.** At Wine Paris, Printemps des Champagnes and Terres et Vins, walk the grower aisles. These are also the events whose exhibitor lists feed an importer and caviste lead-gen service for growers.
6. **Hooks:** the 2026–27 e-invoicing mandate, the export pivot (the US at 15% tariffs, so diversify to new markets), and the caviste opportunity (cavistes are moving away from big-house allocations).

---

## 8. Opportunity map for an AI/automation agency (E)

| Pain (evidence) | Productised offer | Price idea |
|---|---|---|
| PDF bon de commande, cheque or transfer, manual shipping quotes (rows 1–8) | Online order form that writes into a CRM: auto shipping calculation, payment link, invoice pushed to Isagri/Vitisoft, Colissimo label | €2–4k setup plus €100–200/month |
| Ageing private-client file, Q4 dependency (Chambre d'agri; Shop&Champ) | **Client reactivation engine**: clean and segment the file, personalised autumn mailings and SMS, reorder reminders, lapsed-client win-back | €1.5–3k plus €150/month |
| Need for export and caviste/CHR customers (Claeys 2026; Vitisphere) | **Lead-gen**: scrape importers, cavistes and restaurants by country, enrich them, run personalised sequences in EN/DE/JA | €500–1,500 per campaign or monthly retainer |
| Multilingual inbound emails and visit requests, closed at weekends (rows 16, 20; Watizi) | Email and booking AI agent (FR/EN/DE) that drafts replies, books visits and answers price-list questions | €150–300/month |
| Payment chasing, export documents (Juwa) | Automated dunning plus document generation | Add-on |
| Évin-constrained content, 3–5 h/week of social media (Farman, Ampelios) | Content pipeline: harvest, cellar and tasting media turned into Évin-checked posts, newsletters and translated product sheets | €300–600/month |

---

## Sources (cited above)
1. https://www.lsa-conso.fr/champagne-pour-la-troisieme-annee-consecutive-les-ventes-sont-en-baisse-en-2025,464047
2. https://www.pleinchamp.com/actualite/les-ventes-de-champagne-en-baisse-pour-la-3eme-annee-consecutive
3. https://www.linfodurable.fr/champagne-une-vendange-2025-de-qualite-mais-des-vignerons-tres-inquiets-53102
4. https://www.pleinchamp.com/actualite/le-rendement-commercialisable-du-champagne-fixe-a-9000-kg-ha-en-2025-en-baisse-pour-la-3eme-annee-consecutive
5. https://www.vinetur.com/fr/amp/20260828106310/champagne-producers-set-2026-yield-cap-at-a-modern-era-low.html
6. https://lachampagnedesophieclaeys.fr/maisons-vignerons-cooperatives-analyse-detaille-des-chiffres-des-expeditions-de-champagne-2024/
7. https://lachampagnedesophieclaeys.fr/les-expeditions-de-champagne-chiffres-et-tendances-a-fin-novembre-2025/
8. https://lachampagnedesophieclaeys.fr/terroirs-vignerons-de-champagne-croissance-de-3-en-2024-malgre-un-marche-mondial-en-recul/
9. https://lachampagnedesophieclaeys.fr/les-cavistes-de-france-en-champagne-le-13-et-14-septembre-etat-des-lieux-prospective-et-chiffres/
10. https://www.agra.fr/articles/champagne-les-ventes-de-tevc-ont-resiste-en-2024-grace-des-leviers-de-croissance
11. https://www.vitisphere.com/actualite-100898-faute-de-grandes-maisons-de-plus-en-plus-de-cavistes-vont-vers-les-champagnes-de-vignerons-et-de-cooperatives.html
12. https://www.pleinchamp.com/actualite/les-vignerons-a-la-vigne-a-la-cave-sur-les-salons-et-sur-le-web (Afnic survey, Dec 2025)
13. https://www.vinetsociete.fr/etude/barometre-usages-numeriques-filiere-vin/
14. https://lachampagneviticole.fr/oenotourisme-les-chambres-dagriculture-accompagnent-les-vignerons-de-lidee-au-projet/
15. https://www.jean-guy-viot.fr/commande/ and https://www.jean-guy-viot.fr/wp-content/uploads/2026/02/Bon-commande-JG-Viot-2026.pdf
16. http://www.champagne-labbe.fr/bon_de_commande.pdf
17. http://www.champagnebaudot.fr/Fichier.ashx?SITE=5031&FILE=bon+de+commande+2023c.pdf
18. https://www.champagne-bedel.com/vin-de-champagne-pages-Bon-de-commande-fr-0-261-26.html
19. https://www.champagne-de-rekeneire.fr/producteur-champagne-page-Commander-fr-0-10-0.html
20. https://www.champagnetrichet-lorain.fr/bon-de-commande/
21. https://www.champagne-arthoine.com/cgv.html
22. https://www.capeb.fr/www/capeb/media//aube/document/Tarif%20fin%202025%20Adhérents%20CAPEB%20-%20Champagne%20Poinsot%20Frères.pdf
23. https://www.champagneprat.com/commander/commander.php
24. https://www.yvesbarbaray.com/
25. https://www.champagne-cornevin.fr/tarifs-bons-de-commande.html
26. https://www.jollychamp.com/ ; https://www.hachette-vins.com/guide-vins/producteurs/6426/champagne-rene-jolly/
27. https://www.champagne-francois-girard.com/
28. https://www.champagne-cazals.fr/
29. https://www.champagne-frezier.com/Mon-Panier
30. https://www.champagne-meteyer.com/index.php ; https://www.winetourism.com/fr/experience/dans-champagne-b2b/
31. https://www.champagne-yves-meunier-fils.com/notre-culture-4
32. https://www.champagne-gerbaux.com/fr/10-vente-directe-de-champagne-dans-la-vallee-de-la-marne
33. https://www.tourisme-en-champagne.com/champagne-tarlant/oeuilly/deg0000000000209
34. https://www.champagne-terroir.fr/
35. https://www.ruedesvignerons.com/en/domaine/457/champagne-guy-charbaut
36. https://www.comptoirdesmillesimes.com/larmandier-bernier/terre-de-vertus-1er-cru-brut-nature-2018-larmandier-bernier.html
37. https://www.hachette-vins.com/guide-vins/producteurs/3286/pierre-gimonnet-et-fils
38. https://fr.gaultmillau.com/wineries/fleury
39. https://shopandchamp.fr/ ; https://shopandchamp.fr/solution ; https://shopandchamp.fr/guide-e-commerce-vigneron-champagne
40. https://www.echampagne.pro/ ; https://www.enovanet.fr/cms-creation-site-internet-web-design-chateau-thierry-produits-Site-internet-eChampagne-fr-10.html
41. https://www.vrille.io/
42. https://vitisoft.fr/ ; https://www.vcbacked.co/company/vitisoft
43. https://www.isagri.fr/solutions/de-la-tracabilite-des-vignes-a-la-commercialisation-de-vos-vins
44. https://www.idsystemes.com/logiciel-metier/maisons-champagne/
45. https://cap-vignes.vin/
46. https://www.vcbacked.co/company/wineriz ; https://www.vitisphere.com/actualite-102229-lapplication-de-gestion-commerciale-wineriz-fait-un-carton.html
47. https://www.thedrinksbusiness.com/2025/06/french-wine-tourism-firm-secures-e1m-in-funding/ ; https://uptec.up.pt/uptec-startup-raises-e1-million-to-boost-wine-tourism-in-portugal/
48. https://affi.io/m/rue-des-vignerons ; https://www.tourmag.com/Futuroscopie-Le-marche-de-l-oenotourisme-en-mouvement-ABO_a126159.html
49. https://iddesign.pro/creation-de-site-internet-pour-les-vignerons-de-champagne ; https://webchampagne.fr/ ; https://nity.pro/champagne ; https://www.cpcreation.fr/ ; https://agence-vroska.fr/agence-web-a-epernay ; https://beweb-formcom.com/creation-sites-web/
50. https://zaplostudio.com/implantations/agence-ia-epernay
51. https://mankova-consulting.com/ia-automatisation-agence-reims ; https://a2z-automation.com/agence-automatisation-a-reims/ ; https://juwa.co/blog/actualites-tendances-ia/pme-reims-automatisation-ia/ ; https://ia.agency/agence-ia-reims/ ; https://watizi.com/agence-ia-reims ; https://britweb.fr/agence-ia-reims/ ; https://impaakt.fr/intelligence-artificielle-reims/ ; https://www.mehdichallakh.com/freelance-ia/reims/
52. https://ampelios.com/agence-de-communication-vin-champagne/ ; https://e-cvb.com/ ; https://www.farman-communication.com/community-management-pour-vignerons-en-2026-quel-reseau-social-choisir-selon-votre-cible/
53. https://www.champagnedevignerons.fr/vignerons/cote-des-bar/ ; https://www.champagnedevignerons.com/
54. https://maisons-champagne.com/en/industry/organisation/champagne-growers-and-houses/article/champagne-growers-union
55. https://www.lawinetech.com/ ; https://www.usine-digitale.fr/article/food-tech-35-start-up-du-vin-se-federent-autour-de-la-winetech.N927174
56. https://wineparis.com/newfront/sessions/14278
57. https://bottlebooks.londonwinefair.com/producers/5558a429cbf8c2aeb644f741
58. https://boutique.vignerons-independants.com/vin-champagne/region-5
59. https://levigneronchampenois.comitechampagne.fr/abonnement
