# 03 — Champagne logistics & transport: who moves the bottles, how orders are placed, where automation fits

*Research date: 2026-10-07. Scope: France / Champagne region (Marne: Reims, Épernay, Aÿ, Châlons; Aube: Côte des Bar / Troyes).*

> **Method and limits.** Two hard limits applied to this research:
> 1. **No direct page fetching was possible.** The sandbox egress proxy refused connections to every transporter website I tried (WebFetch failed on DNS; curl got a 403 on CONNECT for viticolis.fr, hillebrandgori.com, laposte.fr, geodis.com, kuehne-nagel.com, douane.gouv.fr and others). So the booking UX described below comes from **search-engine extracts of those sites**: product pages, help-centre pages, plugin listings and trade press. Nobody actually clicked through a quote form. Treat the UX descriptions as "what the vendor documents publicly", not as observed behaviour.
> 2. **The shared web-search budget ran out** before I could verify every regional haulier. Unverified names are flagged as such.
>
> About 45 distinct sources are cited inline and listed at the end.

---

## 1. Executive summary

- **The market has three layers.** (a) Global wine-and-spirits forwarders do export: Hillebrand Gori (DHL), Kuehne+Nagel VinLog, Dachser, Geodis, DB Schenker. They have mature portals, instant quotes, EDI and tracking. (b) Regional hauliers and general messagerie networks in the Marne and Aube move domestic pallets. Most look like **phone, email or quote-form businesses** with little self-service. (c) Parcel and DTC shipping uses Chronopost Chrono Viti, Colissimo, Hillebrand Gori eShipping (formerly VignoblExport), Iziwine and Eurosender. Big parcel aggregators (Packlink PRO) often **ban alcohol outright**.
- **The paperwork is the real friction, not the truck.** Every B2B movement needs an excise document. That is a **DAE** (duty suspended) or **DSA** (duty paid, domestic), created in the customs portal **GAMMA**, or an **e-DSA (DAES)** via GAMMA 2 for duty-paid intra-EU B2B since 13 Feb 2023. The **shipper** creates it, not the transporter. GAMMA accepts **XML import**, so software can pre-fill it. Domestic B2C shipments are exempt (an invoice is enough). Cross-border B2C inside the EU needs a **fiscal representative in each destination country**, which parliamentary questions say makes many growers refuse EU consumer orders.
- **Small growers rekey the same order data 4 to 6 times**: order or invoice, then the carrier booking (a portal or a phone call), then the GAMMA DAE/DSA, then customs export docs, then tracking emails to the customer, then POD and invoice reconciliation. No source showed a grower-grade tool that links an ERP or vineyard software to carrier booking and GAMMA end to end. The big forwarders link these steps only for big shippers.
- **Seasonality is extreme.** Volumes peak in Nov–Dec. DHL opened a dedicated depot at Cormontreuil (Reims) specifically to handle champagne before Christmas ([CEP Research](https://www.cep-research.com/?p=41200)). Breakage and heat (shipping in a dry container in summer) are the two quality risks, and insurers dispute claims.
- **Opportunity for a small agency:** a "shipping desk" layer for growers and small houses. Inputs are the order (email, PDF, WooCommerce or Shopify), a vineyard ERP export, or a spreadsheet. Outputs are a carrier booking, GAMMA XML, labels, a pro-forma or commercial invoice, customer tracking notifications, POD capture and claims files. Section 8 lists the full set.

---

## 2. Who moves champagne

### 2.1 Global wine & spirits forwarders (export, FCL/LCL, bonded)

| Player | Champagne relevance (sourced) |
|---|---|
| **Hillebrand Gori (a DHL company)** | The leading wine and spirits forwarder, formed when DHL bought Hillebrand on 23 Mar 2022 and merged it with Gori ([DHL press PDF](https://group.dhl.com/content/dam/deutschepostdhl/en/media-relations/press-releases/2022/pr-hillebrand-20220323.pdf); [Wikipedia](https://en.wikipedia.org/wiki/Hillebrand_Gori)). The French entity, Hillebrand Gori France (formerly JF Hillebrand France), is registered in **Beaune** ([LEI record](https://lei.bloomberg.com/leis/view/969500GF5NNED2E5X989)). I found **no evidence of a Reims office**. Trade press says about 95% of French revenue is export, with sites in Beaune, Bordeaux and Cognac ([Le Moci](https://lemoci.com/?p=27181)). It offers reefers and insulation liners ([refrigerated containers](https://www.hillebrandgori.com/services/cased-goods/temperature-controlled-transport/refrigerated-containers); [insulation liners](https://www.hillebrandgori.com/services/cased-goods/temperature-controlled-transport/insulation-liners)). |
| **Kuehne+Nagel VinLog / Drinks Logistics** | Dedicated drinks unit. It picks up loose or palletised goods at the producer, handles customs, consolidates LCL into FCL, and offers flexitanks, temperature data loggers and integrated insurance. It also runs a reefer-LCL service to Japan (Blue Anchor Line) that names France as an origin ([K+N VinLog](https://home.kuehne-nagel.com/-/services/wine-logistics); [K+N France drinks](https://fr.kuehne-nagel.com/en/-/drinks); [newsroom](https://newsroom.kuehne-nagel.com/kuehne--nagel-expands-activities-in-the-niche-market-of-wine--spirits-logistics/)). |
| **Dachser** | **Has a logistics hub in Reims.** It planned an 18,000 m² platform there, 6,000 m² of it temperature-controlled. Louis Roederer was a historic client from 2003. It reportedly trucks about 30,000 pallets a year of Moët & Chandon, Veuve Clicquot, Dom Pérignon and Hennessy from the Reims suburbs to Nuremberg ([Le Moci](https://www.lemoci.com/?p=25642); [Grande Consumo](https://grandeconsumo.com/en/?p=128062)). The platform's current status is unverified. |
| **Geodis** | Its brochure advertises "transport sécurisé de vins & spiritueux" plus help with tax declarations. There is a "GEODIS D&E Champagne-Ardenne" listing in Épernay, a general road and warehouse operation ([Geodis brochure PDF](https://geodis.com/sites/default/files/2020-02/GEODIS_SITE%20WEB_Vos%20options%20sur%20demande_oct%202019_FR.pdf); [Kompass Épernay](https://fr.kompass.com/s/transports-et-logistique/10/v/epernay/fr_21_51_51230/)). Calberson now trades as Geodis ([Packlink blog](https://www.packlink.com/fr-FR/blog/suivi-geodis/)). |
| **DB Schenker** | Runs "connect 4.0" online land booking with real-time quotes ([DB Schenker FR](https://www.dbschenker.com/fr-en/connect/connect-4-0)). I found no champagne-specific offer. |
| **MSC** (ocean carrier) | Has a "France wines & spirits" local page ([MSC](https://www.msc.com/fr/local-information/europe/france/france-wines-and-spirits)). |
| **DocShipper** | Digital forwarder and customs broker that markets a Reims presence ([DocShipper](https://docshipper.fr/?p=4175)). Self-description only. |

### 2.2 Regional transporters (Marne / Aube): status after verification

| Name | Location | What I could verify | Confidence |
|---|---|---|---|
| **Les Transports Lebrun** | Épernay | 50 staff, €11M revenue in 2024. Works with "several large champagne houses". Switched 10+ trucks to B100 rapeseed biofuel under pressure from the houses' decarbonisation goals ([Le Journal des Entreprises](https://www.lejournaldesentreprises.com/breve/les-transports-lebrun-receptionnent-5-tracteurs-alimentes-lhuile-de-colza-2144859); [Journal du Poids Lourd](https://journaldupoidslourd.com/transport/transports-lebrun-du-b100-pour-des-vins-de-champagne/)) | **Verified** (press) |
| **LTD** (ltd-51.fr) | Reims | Its own site describes it as a champagne transport specialist and "preferred partner of champagne houses since 2007", doing dedicated deliveries to Paris / Île-de-France ([ltd-51.fr transport dédié](https://www.ltd-51.fr/transports-dedie.php); [ltd-51.fr champagne](https://www.ltd-51.fr/transport-de-champagne-dans-la-marne-51.php)) | Pages indexed but **not fetchable**. Company details unverified |
| **Viticolis** | Champagne flows (Épernay, Côte des Bar) | Indexed page says it is a wine-specialist carrier: collects 5 days a week, delivers in 24h in France, serves growers, négociants, cavistes and co-ops ([viticolis.fr](https://viticolis.fr/secteurs/transport-de-vin-champagne/)) | Page indexed but **not fetchable**. A second search returned nothing, so details are unverified |
| **Transfret Champagne** | Reims (rue Robert Fulton) | Small road transport firm with 1–2 employees ([PagesJaunes](https://www.pagesjaunes.fr/pros/57665355)) | Directory only |
| **Mazet Champagne** | Reims | Directory lists groupage, chartering and international work ([PagesJaunes](https://www.pagesjaunes.fr/pros/08520898)). The Mazet group itself is based in Aubenas ([Xerfi](https://www.xerfi.com/etudes-par-entreprise/mazet-messagerie_492486402)) | Directory only |
| **Foselev Champagne** | Reims | Road transport company listing ([transporteur.tel](https://transporteur.tel/51-marne/reims/societe-de-transport-routier/19682-foselev-champagne.html)) | Directory only |
| **Veolog** (Le Roy Logistique since 2024) | Châlons-en-Champagne | Warehousing, order prep and co-packing for Marne companies. Lists wine and spirits among its sectors ([Veolog Châlons](https://www.veolog.fr/agences/plateforme-logistique-chalons-en-champagne/); [CB Insights](https://www.cbinsights.com/company/veolog)) | Company pages |
| **Stralog Transports** | Lavau (Aube, near Troyes) | Kompass describes it as an order-prep and **bonded (sous accise) warehouse specialist in wines and spirits** (via the [Kompass search](https://fr.kompass.com/a/services-de-gestion-logistique/7594025/r/champagne-ardenne/fr_21/)) | Directory only. A follow-up search found nothing |
| **HBL Logistique (Logivin)** | Épernay | Appears in a directory list only | **Unverified** |
| **FM Logistic, OC Logistique** | St-Martin-sur-le-Pré, Caurel | General warehousing and order prep | Directory only |
| **Champagne Emballage** | Épernay | Packaging supplier ([e-pro](https://grossiste.e-pro.fr/marne/champagne-emballage_f635941)) | Directory only |
| **Groupe Mauffrey** | National (founded 1964, 50+ subsidiaries) | A 118712 directory entry lists "transport de champagne / vin" among its services ([118712](https://www.118712.fr/professionnels/X0VRW1NcGgI)) | Weak. Branch shown is in Val-de-Marne, not the Marne |
| **Transports Jacquemin, Transports Gaudillat, "TSE"** | — | **No evidence found.** Do not use these names | Not verified |

Context: Épernay Agglo says more than half of the ~1,300 champagne-related businesses (including logistics suppliers) sit in the agglomeration ([Épernay Agglo](https://epernay-agglo.fr/print/pdf/node/9546)). Logistics and messagerie firms cluster near the A4/A34 interchange (P.A. Terres Rouges, Val de Champagne, Z.A. Les Forges) ([unemplacement](https://unemplacement.com/entrepots/marne-51/epernay-51200)). Big houses run their own platforms; for example, Perrier-Jouët has a listed "plateforme logistique" ([Usine Nouvelle](https://industrie.usinenouvelle.com/fiche/etablissement/champagne-perrier-jouet-43676884)). Maison Burtin (Épernay) uses Zetes for identification and order picking. **This is a meaningful gap: I could not build an exhaustive list of champagne-specialist hauliers.** A Pappers or SIRENE extraction (NAF 49.41A/B, 52.10B, 52.29B in départements 51 and 10) would be the right next step and is itself scrapable.

### 2.3 Parcel / DTC / small-quantity specialists

| Player | Model |
|---|---|
| **Chronopost Chrono Viti** | Created in 2009 for small wine volumes to businesses and consumers. Branded packaging for 1, 2, 3 or 6 bottles and magnums. A dedicated export phone and email line helps with customs documents. Shippers print their own labels, and scheduled pickup is free. Pricing depends on volume and is negotiated with interprofessions (CAVB in Burgundy, Corsica). Insurance is contractual liability plus optional ad valorem ([Chronopost Chrono Viti](https://www.chronopost.fr/en/delivery/our-offers/chrono-viti); [brochure PDF](https://www.chronopost.fr/sites/default/files/chronoviti.pdf); [export guide PDF](https://www.chronopost.fr/sites/default/files/atoms/files/guide-export-chronoviti.pdf); [macommune.info](https://www.macommune.info/chrono-viti-une-nouvelle-solution-pour-lenvoi-des-bouteille-de-bourgogne-dans-le-monde-entier)). Bordeaux City Bond plus Chrono Viti averaged **under €15 per bottle** internationally (c. 2016–17) ([Journal des Entreprises](https://www.lejournaldesentreprises.com/article/bordeaux-city-bond-et-chronopost-deploient-chronoviti-95222)). I found **no evidence of a Champagne interprofession deal**. |
| **Colissimo (La Poste)** | Bottle packaging is sold in the La Poste shop. Loss and breakage compensation is included, but forum reports say refunds come by weight without an invoice. Many countries are banned (Saudi Arabia, Brazil, NZ, UAE…). Max 30 kg (Switzerland) ([La Poste vin](https://www.laposte.fr/envoyer/envoyer-bouteilles-vin); [La Poste pro étranger](https://www.laposte.fr/professionnel/expedier/livrer-bouteilles-vin-etranger); [La Poste Suisse](https://www.laposte.fr/professionnel/expedier/expedier-vin-suisse); [emballages](https://www.laposte.fr/boutique/c/emballagespourbouteilles)). |
| **Hillebrand Gori eShipping** (ex-**VignoblExport**, Orléans, founded 2011; Hillebrand took 70% in 2021) | Self-service web platform for small alcohol shipments, with about 3,000 clients (growers, négociants, co-ops) in 2021. Compare carriers, rates and transit times; book; arrange pickup; track. Customs is handled by the platform ([eShipping](https://eshipping.hillebrandgori.com/); [Le Moci](https://www.lemoci.com/?p=142814); [HG article](https://www-ifte.hillebrandgori.com/media/publication/international-alcohol-shipping)). A **WooCommerce plugin** exists for HG clients only, with fewer than 10 active installs ([WordPress.org](https://wordpress.org/plugins/hillebrand-gori-eshipping/); [xpay directory](https://www.xpay.sh/directory/woocommerce/plugins/hillebrand-gori-eshipping/)). I found no Shopify app. |
| **Iziwine** (South-West) | Online wine shipping. The grower enters the **number of cases plus the customer's postcode, gets an instant price**, pays online, and Iziwine sends a carrier. Claims 3 days to Europe, 5 days to the US, 130 countries. **The grower stays responsible for tax compliance.** Competitor named: Wine Shipper (Brittany) ([Réussir Vigne](https://www.reussir.fr/vigne/node/2838)). |
| **Eurosender** | Aggregator with a champagne page. It says many carriers ban alcohol and that businesses ship under a carrier contract. Offers a pro account and pallet/FTL quotes ([Eurosender champagne](https://www.eurosender.com/fr/envoyer-emballer/alcool/champagne); [Eurosender vin](https://www.eurosender.com/fr/envoyer-emballer/vin)). |
| **UPS / DHL Express** | Accept wine only from **licensed shippers who sign an alcohol agreement**; consultation and paperwork are required ([UPS wine FR](https://ups.com/fr/en/support/shipping-support/shipping-special-care-regulated-items/prohibited-items/wine); [UPS wine addendum](https://muat2.ups.com/assets/resources/webcontent/en_US/wine_addendum.pdf); [DHL alcohol guidelines](https://mydhl.express.dhl/us/en/help-and-support/customs-clearance-advice/alcoholic-beverages.html); [DHL agreement PDF](https://mydhl.express.dhl/content/dam/downloads/us/en/agreement-to-transport-alcoholic-beverages/dhl_express_agreement_to_transport_alcoholic_beverages_us_en.pdf.coredownload.pdf)). These are mostly US-side docs; the French origin terms are unverified. DHL Express opened a 650 m², 300-parcels-a-day automated depot at **Cormontreuil** for champagne before Christmas ([CEP Research](https://www.cep-research.com/?p=41200)). |
| **Wine logistics / 3PL for e-commerce** | Winetailors (Tesson group; multi-grower mixed orders), Dartess (Gironde; last-mile hub in Paris), Vinéolis (Var; bottling, storage, shipping), the 2LR group (Languedoc; bonded storage, bottle-to-pallet picking) ([motherbase](https://my.motherbase.ai/startup/114223-winetailors); [Journal des Entreprises – Dartess](https://www.lejournaldesentreprises.com/article/grace-au-e-commerce-dartess-voit-la-logistique-en-rose-129331); [Journal des Entreprises – Vinéolis](https://www.lejournaldesentreprises.com/article/vineolis-investit-dans-un-service-logistique-pour-ses-clients-vignerons-et-negociants-1532285); [Réussir – délégation](https://www.reussir.fr/delegue-le-stockage-et-lexpedition-de-nos-vins-de-negoce-parce-que-lon-confiance); [2LR brochure](https://www.vitisphere.com/upload/images/Image/Plaquette%202LR.pdf)). B2LOG advertises bonded e-commerce logistics for wine ([B2LOG](https://www.b2log.fr/)). **I found no Champagne-based wine DTC 3PL**, which is a possible gap in the market and worth verifying. |

### 2.4 Digital freight platforms

| Platform | Relevance to wine |
|---|---|
| **Packlink PRO** | **Alcohol is prohibited** ("any liquid containing alcohol") ([Packlink PRO help](https://support-pro.packlink.com/hc/en-gb/articles/210236985)). The consumer site is more nuanced ([Packlink vin](https://www.packlink.com/fr-FR/envoyer-du-vin/)). |
| **Sendcloud** | Connects Colissimo, Chronopost, DHL, DPD, GLS and UPS, but publishes no alcohol policy ([Sendcloud France guide](https://www.sendcloud.com/blog/shipping-to-france/); [Sendcloud Colissimo](https://www.sendcloud.com/carriers/colissimo/)). Growers would have to bring their own carrier contracts. |
| **Boxtal** | An SMB parcel aggregator. Pallets, B2B and complex international shipments are "not its core" ([lafabriquedunet](https://www.lafabriquedunet.fr/logiciels/alternatives/alternative-boxtal)). Its alcohol policy is unverified. |
| **Cargoboard** | Digital pallet forwarder for B2B only. Instant price, then a 4-step online booking ([cargoboard.com](https://cargoboard.com)). Wine acceptance is unverified. |
| **Upply** (Geodis spin-off, 2018) | Freight marketplace plus rate benchmarks. Shippers post loads and carriers respond ([FreightWaves](https://www.freightwaves.com/news/technology-geodis-launches-upply-freight-marketplace); [Upply FAQ](https://www.upply.com/en/faq)). |
| **Ovrsea, Sennder, Shippeo, Fretlink** | **Nothing found** linking them to wine or champagne in the time available. |

**Takeaway:** the cheap generic parcel tools that SMB e-commerce relies on either exclude alcohol or leave compliance to the shipper. That pushes growers back to Chrono Viti contracts, wine-specific platforms (eShipping, Iziwine) or phone-based hauliers.

---

## 3. How do you actually order? Booking UX by transporter

(Based on publicly indexed pages and documentation; the pages could not be fetched or clicked, see the method note.)

| # | Transporter | Quote | Booking | Tracking | Integration | Notes |
|---|---|---|---|---|---|---|
| 1 | **Hillebrand Gori – myHillebrandGori** | Online quote request ("6 questions"); compare quotes in the portal | Portal | Live map, per-milestone notifications | Invoices, documents, SKU and warehouse inventory views, CO₂ per leg, container slots, D&D monitoring | Sign-up at my.hillebrandgori.com ([myHG](https://www-ifte.hillebrandgori.com/support/myhillebrandgori); [FAQ](https://www.hillebrandgori.com/faq/myhillebrand); [Drinks Business 2018](https://www.thedrinksbusiness.com/2018/10/jf-hillebrand-launches-milestone-digital-platform/)) |
| 2 | **Hillebrand Gori eShipping** | Instant multi-carrier rates | Self-service, pickup booking | Yes | WooCommerce plugin | Small alcohol parcels; customs handled ([eShipping](https://eshipping.hillebrandgori.com/)) |
| 3 | **Kuehne+Nagel myKN** | **Instant quote** (LCL valid 30 days); verified account needed for FCL | Book online from the quote | Dashboard | API/EDI for large accounts (not detailed) | Needs origin, destination, volume and Incoterm ([myKN how to quote](https://th.kuehne-nagel.com/en/-/knowledge/how-to-get-a-quote); [myKN](https://us.kuehne-nagel.com/en/-/services/solutions/mykn); [K+N LCL](https://us.kuehne-nagel.com/-/services/sea-freight/lcl)) |
| 4 | **DB Schenker connect 4.0** | **Real-time land quote**, spot offer without registration | Online booking, templates, address book | Yes | eServices: invoices, claims, emissions | ([DB Schenker FR](https://www.dbschenker.com/fr-en/connect/connect-4-0); [eServices](https://www.dbschenker.com/it-en/business/services/eservices); [trans.info](https://trans.info/en/db-schenker-has-launched-a-platform-for-its-clients-not-just-for-placing-orders-and-asking-quotes-164985)) |
| 5 | **Dachser eLogistics** | Instant pricing not confirmed; likely through a sales contact | eLogistics ordering | shipmentcontrol | EDI | ([Dachser LCL](https://www.dachser.co.uk/en/lcl-services-1082)) |
| 6 | **Geodis (messagerie)** | No public instant quote found; agency or sales | "Espace client" to prepare shipments | Real-time tracking; delivery instructions online | Invoices in the portal | ([Geodis brochure](https://geodis.com/sites/default/files/2020-02/GEODIS_SITE%20WEB_Vos%20options%20sur%20demande_oct%202019_FR.pdf)) |
| 7 | **Heppner** | No public instant quote found | EDI or account | IFTSTA status files | **EDI: IFTMIN D01B by SFTP; IFTSTA back** (AEB carrier-connect doc) | ([AEB Heppner](https://rz3.aeb.de/docudata/system-descriptions/carrier-connect/sd-carrierconnect-carrieroverview/en-US/821884555821895051.html)) |
| 8 | **France Express** | **Contact your département's agency** for a quote | Agency | Tracking number on the website | — | ([Packlink blog](https://www.packlink.com/fr-FR/blog/france-express/); [Eurosender](https://www.eurosender.com/fr/societes-transport/france-express)) |
| 9 | **Chronopost Chrono Viti** | Negotiated contract tariff | Self-printed labels; scheduled pickup | Yes | Chronopost web/API (generic) | Export support by phone and email ([Chrono Viti](https://www.chronopost.fr/en/delivery/our-offers/chrono-viti)) |
| 10 | **Iziwine** | **Instant** (cases plus postcode) | Pay online; carrier dispatched | Not documented | — | ([Réussir](https://www.reussir.fr/vigne/node/2838)) |
| 11 | **Cargoboard** | **Instant pallet price** | 4-step online booking | Yes | — | B2B only ([cargoboard](https://cargoboard.com)) |
| 12 | **Regional hauliers** (LTD, Lebrun, Viticolis, Transfret…) | Phone, email, website contact form (inferred; sites could not be opened) | Phone or email | Unknown, probably phone calls plus a POD photo or scan | None found | **Assumed manual, not verified** |

**Pattern:** self-service and APIs exist at the top of the market and in parcel tools. The regional pallet hauliers that do most domestic B2B champagne moves almost certainly still run on phone calls, emails and contact forms. I'm inferring that from the absence of any portal or API mention, because I couldn't open their sites.

---

## 4. How a grower or small house ships today: four scenarios

### A. Domestic B2B pallet to a caviste or restaurant (duty paid)
1. **Quote.** Call or email the regular haulier or messagerie agency, or use an online quote (Cargoboard, Schenker spot). Pallet dims and weight: 600 bottles is roughly 900+ kg, at about 1.5 kg per bottle ([La Poste](https://www.laposte.fr/envoyer/envoyer-bouteilles-vin)).
2. **Booking.** Phone or email, or a portal for messagerie accounts.
3. **Excise document.** For professionals, a **CRD capsule or a DSA is mandatory** (duty paid), or a **DAE** if duty suspended. The DSA must name the shipper, consignee and **transporter** and is issued in **GAMMA**; periodic summary returns are required ([douane – formalités vin en bouteilles](https://www.douane.gouv.fr/formalites-la-circulation-pour-le-vin-en-bouteilles); [douane – simplification 2018](https://www.douane.gouv.fr/actualites/simplification-administrative-pour-les-professionnels-du-vin)). CRD has been **optional since 1 June 2019** for containers of 3 L or less ([douane](https://www.douane.gouv.fr/en/node/1283)).
4. **Labels and delivery note.** Produced by the grower's software or Word or Excel.
5. **Tracking, POD, invoice.** Usually by phone, or a scanned POD emailed back. Invoices are reconciled by hand.

### B. A few cartons to a private client in France
- Since **1 Jan 2020** there are **no circulation formalities** for duty-paid sales to private individuals without CRD. The buyer just needs the invoice ([douane](https://www.douane.gouv.fr/formalites-la-circulation-pour-le-vin-en-bouteilles)).
- Typical channels: Colissimo or Chronopost (Chrono Viti packaging), Iziwine or eShipping, or a regional "messagerie vin" for multi-case home deliveries. Forum users complain about **express carriers refusing wine, breakage, and low refunds without an invoice** ([La Passion du Vin – transport](https://www.lapassionduvin.com/autour-du-vin/20978-question-de-transport); [La Passion du Vin – transporteurs](https://www.lapassionduvin.com/de-la-terre-au-verre/36108-les-transporteurs-la-logistique-du-vin)). These threads are old (2009–2016).

### C. Private client elsewhere in the EU (Belgium, Germany…)
- Under **distance-selling rules**, excise is due in the **destination** country, and the **seller must appoint a fiscal representative** there (CGI art. 302 U and 302 V bis; Directive 2008/118 art. 36, now 2020/262 art. 44). French MPs and the Vignerons Indépendants say this makes many growers **refuse EU consumer orders**. The government says France cannot simplify this unilaterally ([AN question 26452](https://questions.assemblee-nationale.fr/dyn/14/questions/QANR5L14QE26452.pdf); [AN question 30729](https://questions.assemblee-nationale.fr/dyn/14/questions/QANR5L14QE30729.pdf); [Sénat 2013](https://www.senat.fr/questions/base/2013/qSEQ130506603.html); [VSNews reform proposals PDF](https://www.vsnews.fr/images/Le_commerce_intracommunautaire_des_vins_a_destination_des_particuliers_-_Propositions_de_reforme.pdf)).
- Germany (per a vendor): a registered representative, a guarantee, monthly declarations, no OSS for excise, and German VAT from the first sale ([Eurofiscalis DE](https://www.eurofiscalis.com/accises-allemagne/); [Eurofiscalis FR](https://www.eurofiscalis.com/accises-france/)).
- If the checks fail, liability falls on the shipper ([Le Moci](https://www.lemoci.com/?p=142814)). Fiscal-rep and compliance outsourcing (Eurofiscalis-type services) is its own small market.

### D. Export pallet or container to an importer (USA, UK, Japan…)
1. Quote from a forwarder: a myKN or myHG portal, or an email RFQ. Choose the Incoterm (usually **EXW or FCA cellar**; wine FOB pricing is an ex-cellar concept) ([winewithseth FOB](https://www.winewithseth.com/winewiki/fob-free-on-board/)).
2. Pickup at the cellar, often groupage at the forwarder's hub, then Le Havre or Antwerp. Reefer or **insulation liner** for summer and hot routes.
3. **Excise:** the goods leave under a **DAE** from the entrepositaire agréé. The DAE is discharged on export.
4. **Customs:** an export declaration (EX-A / DELTA) by the forwarder acting as customs broker. **K+N states its teams handle alcohol export documentation per destination rules** ([K+N FR](https://fr.kuehne-nagel.com/en/-/drinks)). China historically also required AUBETTE certification ([douane Aubette PDF](https://Douane.gouv.fr/sites/default/files/2019-02/exportez-des-vins-et-spiritueux-en-chine-en-toute-securite-aubette.pdf)). Export certificates through the DGCCRF platform **Télécertex**, paper only exceptionally since Feb 2020 ([DREETS PDF](https://nouvelle-aquitaine.dreets.gouv.fr/sites/nouvelle-aquitaine.dreets.gouv.fr/IMG/pdf/cybertex_06_01_2022.pdf)).
5. **USA:** the **three-tier system** means a US importer (tier 1, with a federal importer permit) sells to a distributor, who sells to a retailer or restaurant. Illustrative markups: distributor 25–33% on FOB, retailer 30–50% ([VinePair explainer](https://vinepair.com/articles/three-tier-system-explainer/); [Joshua London substack](https://joshuaelondon.substack.com/p/this-wine-costs-what); [three-tier precis PDF](https://marketingwine.nfshost.com/wp-content/uploads/2020/06/tt-precis-of-us-wine-market-and-three-tier-sales-channel.pdf)). An old example deck puts ocean freight at about $4.50 per 12-bottle case ([Puglia 2015 deck](https://www.slideshare.net/slideshow/puglia-2015/48723853)). A glossary claims a 10% "Section 122" tariff on all imported wine since March 2026 ([winewithseth](https://www.winewithseth.com/winewiki/fob-free-on-board/)). **That is unverified; check with CBP.** FEVS reports French wine and spirits exports fell 7.9% to €14.3bn in 2025 on US tariffs and Chinese anti-dumping duties ([Pleinchamp](https://www.pleinchamp.com/actualite/en-2025-les-exportations-de-vins-et-spiritueux-en-recul-de-7-9-a-14-3-milliards-d-euros)). Direct-to-consumer from France to the US is effectively not possible for growers.
6. Docs to the importer: commercial invoice, packing list, certificate of origin, health and analysis certificates where required, BL. Mostly PDF by email.
7. Big houses have in-house "régie douanes et transport" roles (for example a Bollinger profile) ([LinkedIn/Malt profile](https://www.malt.fr/profile/catherinebrochard)). Small growers depend on their forwarder.

---

## 5. Excise & customs coupling: who produces which document

| Document | When | Who creates it | System |
|---|---|---|---|
| **DAE** (e-AD) | Movement **under duty suspension** (between bonded warehouses, to export, intra-EU B2B in suspension) | **Shipper**: an entrepositaire agréé or registered consignor. **Never the consignee**, who must confirm receipt within 5 working days | **GAMMA** (French EMCS) via the Prodouane portal ([douane – suspension](https://www.douane.gouv.fr/demarche/echanger-des-produits-soumis-accise-en-regime-de-suspension-des-droits); [GAMMA/EMCS presentation](https://www.douane.gouv.fr/GammaFormation/res/presentation_GAMMA_EMCS_operateur.pdf); [GAMMA documentation PDF](https://moa.douane.gouv.fr/sites/default/files/documentation/pdf/gamma-gestion-de-l-accompagnement-des-mouvements-de-marchandises-soumises-a-accise.pdf)) |
| **DSA** | Domestic movement **duty paid** to a professional when there is no CRD | Shipper | GAMMA |
| **e-DSA / DAES** | Intra-EU **B2B duty paid**, mandatory since **13 Feb 2023** (Directive 2020/262; certified consignor and consignee roles) | Certified consignor | **GAMMA 2** ([douane – droits acquittés](https://www.douane.gouv.fr/demarche/echanger-des-produits-soumis-accise-en-regime-droits-acquittes); [Malta customs explainer](https://customs.gov.mt/mc/other-pages/new-newsresult2/2023/01/26/changes-to-the-movement-of-duty-paid-harmonised-excise-items-as-established-by-the-new-eu-excise-directive-(2020-262)); [Directive art. 36](https://legislation.gov.uk/eudr/2020/262/article/36?view=plain)) |
| **Export declaration (EX-A)** | Non-EU | Usually the **forwarder or customs broker** | DELTA (French customs) |
| **CRD capsule** | Optional since 2019; still a valid domestic movement title | Producer | — |

Key automation facts:
- **GAMMA supports `.xml` import** of DAE and DSA through "Créer DAE → importer un fichier .xml" (DTI+ format), plus brouillon (draft) mode ([GAMMA DTI+ user guide PDF](https://form.douane.gouv.fr/sites/default/files/2021-05/07/guide_utilisateur_gamma_dtiplus_v2.0.pdf)). So a script can generate the XML from the order data and the user imports it. That cuts rekeying without needing API access to customs.
- Vineyard software already exposes this. **Wineriz** has a help article on creating and sending a DAE from Wineriz ([Wineriz help](https://intercom.help/wineriz/fr/articles/13940285-creer-et-envoyer-un-dae-depuis-wineriz)). Other vineyard ERPs probably do too (not researched here). An agency would **integrate with these tools rather than compete with them**.
- If GAMMA is down there is a backup procedure, **GPS** (paper DAA with a generated number), which has to be regularised afterwards ([GAMMA exercise PDF](https://douane.gouv.fr/GammaFormation/res/corrige_gamma_n10_GPS_attention.pdf)).
- The transporter's legal role is just to **carry the ARC code or a printout** ([TradeHub – art. 20](https://www.thetradehub.eu/de/reglementation/france/eu/excise-2020-262/article/20)). In practice, forwarders (Geodis "aide aux déclarations fiscales", K+N, HG) sell document preparation as a service.
- Négociants who collect bulk wine can issue an **incomplete DAE** in GAMM@ and complete quantities by hand on paper copies after loading ([TradeHub DA 18-006](https://www.thetradehub.eu/en/reglementation/france/doctrine/decisions-administratives/da-18-006)). The rules themselves bake in manual steps.

---

## 6. Breakage, insurance, temperature, peak season, costs

- **Breakage and insurance.** Parcel compensation is often **by weight unless an invoice proves value**. Wooden cases have been refused or excluded by La Poste. Many express carriers refuse wine without a contract ([La Passion du Vin](https://www.lapassionduvin.com/autour-du-vin/20978-question-de-transport)). Chrono Viti offers contractual liability plus optional ad valorem. Forwarders sell door-to-door cargo insurance (K+N VinLog). Packaging advice: double-wall cartons or molded inserts, bottles kept from touching ([La Poste](https://www.laposte.fr/envoyer/envoyer-bouteilles-vin); [Eurosender](https://www.eurosender.com/fr/envoyer-emballer/alcool/champagne)). A driver's view: France's main problem is how many different companies a parcel passes through ([La Passion du Vin](https://www.lapassionduvin.com/autour-du-vin/20978-question-de-transport)).
- **Temperature.** The wine comfort zone is 10–20°C. Above 21°C for a prolonged period alters the wine; freezing is around -5°C. An uninsulated container can reach 60°C inside when it is 40°C outside. Reefers cost **up to 3 times** a dry container, so most wine ships dry, often with **thermal liners** ([Hillebrand wine temperature](https://hillebrand.com/media/publication/wine-temperature-how-to-protect-your-wines-from-shipping-damage); [Hillebrand insulated container](https://hillebrand.com/media/publication/insulated-container-what-it-is-and-why-you-need-it); [Hull study](https://hull-repository.worktribe.com/OutputFile/4872083)). Jancis Robinson documented a shipment containing champagne that was **booked as reefer but shipped dry**, arrived at 32–35°C, and **the insurer disputed the claim** ([JancisRobinson.com](https://jancisrobinson.com/zh-hans/articles/what-happens-when-wine-gets-hot)). Booking verification and logger data matter.
- **Peak season.** Q4 gifting drives the parcel peak. DHL's Cormontreuil depot exists specifically for the pre-Christmas champagne surge ([CEP Research](https://www.cep-research.com/?p=41200)). I found no hard data on Champagne Q4 delays; a dedicated search ran out of budget.
- **Costs (sparse, indicative only).**
  - International parcel, per bottle: **under €15** on average (Chrono Viti / Bordeaux, c. 2016–17).
  - Ocean freight USA: about **$4.50 per 12-bottle case** in an old example deck.
  - Reefer: up to **3 times** a dry container.
  - Upply marketplace fee: reported **2.5%** per side (undated).
  - Domestic pallet rates: **I found no published Champagne figure.** Every source says to "ask for a quote". The lack of transparent pallet pricing is itself a finding.

---

## 7. Pain points (synthesised; strength of evidence noted)

| Pain point | Evidence |
|---|---|
| **Paperwork and multiple systems** (order → booking → GAMMA DAE/DSA → export docs) | Strong. Official procedures (sections 4–5). Software vendors such as Wineriz build DAE features because of it. |
| **EU B2C cross-border is effectively blocked** by the fiscal-rep requirement | Strong (Assemblée nationale, Sénat, FNVI). |
| **Carriers refusing alcohol / aggregator bans** | Strong (Packlink PRO ban, UPS/DHL licensing, Eurosender). |
| **Breakage and poor compensation** | Medium (forums, old). |
| **Heat damage and disputed insurance claims** | Medium (Jancis Robinson case, Hull study, Hillebrand). |
| **Opaque pallet pricing; quotes by phone or email** | Medium (no public grids; regional hauliers apparently without self-service). |
| **Compliance responsibility stays with the grower even with platforms** | Strong (Réussir on Iziwine; Le Moci on destination taxes). |
| **No ERP ↔ carrier integration for small producers** | Inferred. Integrations found only for big-forwarder EDI (Heppner IFTMIN, myKN, myHG) and one niche WooCommerce plugin with fewer than 10 installs. |
| **Q4 peak congestion** | Weak/indirect (DHL depot opened for it). |
| **Decarbonisation pressure from houses onto hauliers** | Verified (Transports Lebrun B100). Houses will increasingly ask hauliers for CO₂ reporting per shipment, which is a reporting and automation need. |

---

## 8. Where automation and AI could plug in

Ranked by fit for a small agency that already builds CRMs, agents, workflow automation and scrapers.

1. **"Shipping desk" agent for growers and small houses (highest fit)**
   - Reads incoming orders (email, PDF purchase orders, WooCommerce/Shopify, the vineyard ERP export, spreadsheets) and pulls out consignee, cases, bottles, value and destination.
   - Decides the scenario (FR B2C, FR B2B duty paid, EU B2B, EU B2C, export) and builds the right checklist: no document needed, DSA, DAE, e-DSA, export docs, fiscal rep.
   - Generates the **GAMMA XML (DTI+)** for DAE or DSA import, cutting rekeying. GAMMA explicitly supports XML import.
   - Books the carrier: an API where one exists (Chronopost, Schenker, K+N, eShipping), an **auto-generated, pre-filled email or web form for regional hauliers**, and Heppner-style IFTMIN EDI if relevant.
   - Produces labels, delivery notes, pro-forma and commercial invoices, and packing lists.
   - Pushes tracking to the end customer, captures POD, and reconciles carrier invoices against bookings.
2. **Quote aggregation for pallets.** One request goes to 3–5 regional hauliers and messageries by email or form. An agent parses the PDF or email replies into a comparison table. This matters because the market has no public pallet pricing.
3. **Peak-season (Nov–Dec) ops automation.** Batch label printing, proactive delay alerts, a customer-service bot that answers "where is my order?" from tracking data, and automated breakage claims. A claim needs photos, invoice value and the carrier claim form, sent within the carrier's deadlines; without an invoice, compensation drops to weight-based.
4. **Export document pack generator.** From the order and product master data (alcohol %, volume, HS 2204.10 for sparkling wine, lot numbers), generate commercial invoice, packing list, CoO request data and importer-specific requirements. US importers need label/COLA references and FDA prior notice data. Hand the pack to the forwarder by email or portal upload.
5. **Temperature and insurance guardrail.** Check that a "reefer" booking matches the arrival notice (the Jancis Robinson failure mode), flag summer or hot routes for liners or loggers, and store logger data with the shipment for claims.
6. **Carrier CRM / transport-procurement database for the agency itself.** **Scrape SIRENE/Pappers** for NAF transport and warehousing codes in départements 51 and 10, plus their websites, to map which hauliers serve champagne and how they take orders. This fills the gap this report could not close and doubles as a lead list for selling *to transporters*: small regional hauliers like LTD, Viticolis or Transfret probably have no customer portal, and the agency could build them a simple online order form, booking CRM, tracking page and POD app.
7. **EU B2C compliance workflow.** Partner with a fiscal-representation provider. Automate excise calculation per country, monthly declaration data and the e-commerce checkout rules. This could re-open the EU consumer orders growers currently refuse. It is complex, so position it as integrating with a fiscal rep, never replacing one.
8. **CO₂ reporting for haulier ↔ house relations.** Houses push decarbonisation (the Lebrun case). Automated per-shipment emissions reports from km, load and fuel type (B100 vs diesel) for regional hauliers selling to big houses.

**Integration targets to research next:** vineyard ERPs (Wineriz, and others not covered here), GAMMA XML schema (DTI+), Chronopost and Colissimo APIs, Hillebrand eShipping (is there an API?), myKN API, DB Schenker API, and Heppner/Geodis EDI.

---

## 9. Open questions / not verified
- The exact booking UX on regional haulier sites (LTD, Viticolis, Lebrun): pages could not be fetched.
- Whether Hillebrand Gori, Kuehne+Nagel, Heppner, Ziegler or DB Schenker have branches in Reims. Only Dachser's hub and the DHL Express Cormontreuil depot are sourced.
- Whether Transports Mauffrey has a champagne activity in the Marne, and whether "Transports Jacquemin", "Transports Gaudillat" or "TSE" exist at all (no evidence found).
- Current domestic pallet prices; a Champagne-specific Chrono Viti or interprofession deal; current Q4 delay data.
- Whether Boxtal, Sendcloud or Cargoboard accept wine; whether Ovrsea or Sennder have wine customers.
- The US "Section 122" 10% tariff claim.

---

## 10. Sources

1. https://en.wikipedia.org/wiki/Hillebrand_Gori
2. https://group.dhl.com/content/dam/deutschepostdhl/en/media-relations/press-releases/2022/pr-hillebrand-20220323.pdf
3. https://lei.bloomberg.com/leis/view/969500GF5NNED2E5X989
4. https://www-ifte.hillebrandgori.com/support/myhillebrandgori
5. https://www.hillebrandgori.com/faq/myhillebrand
6. https://eshipping.hillebrandgori.com/
7. https://www-ifte.hillebrandgori.com/media/publication/international-alcohol-shipping
8. https://wordpress.org/plugins/hillebrand-gori-eshipping/
9. https://www.thedrinksbusiness.com/2018/10/jf-hillebrand-launches-milestone-digital-platform/
10. https://www.hillebrandgori.com/services/cased-goods/temperature-controlled-transport/refrigerated-containers
11. https://www.hillebrandgori.com/services/cased-goods/temperature-controlled-transport/insulation-liners
12. https://hillebrand.com/media/publication/wine-temperature-how-to-protect-your-wines-from-shipping-damage
13. https://hillebrand.com/media/publication/insulated-container-what-it-is-and-why-you-need-it
14. https://home.kuehne-nagel.com/-/services/wine-logistics
15. https://fr.kuehne-nagel.com/en/-/drinks
16. https://newsroom.kuehne-nagel.com/kuehne--nagel-expands-activities-in-the-niche-market-of-wine--spirits-logistics/
17. https://th.kuehne-nagel.com/en/-/knowledge/how-to-get-a-quote
18. https://us.kuehne-nagel.com/en/-/services/solutions/mykn
19. https://us.kuehne-nagel.com/-/services/sea-freight/lcl
20. https://www.lemoci.com/?p=25642 (Dachser Reims)
21. https://grandeconsumo.com/en/?p=128062 (Dachser 30,000 pallets)
22. https://www.dachser.co.uk/en/lcl-services-1082
23. https://www.dbschenker.com/fr-en/connect/connect-4-0
24. https://www.dbschenker.com/it-en/business/services/eservices
25. https://trans.info/en/db-schenker-has-launched-a-platform-for-its-clients-not-just-for-placing-orders-and-asking-quotes-164985
26. https://geodis.com/sites/default/files/2020-02/GEODIS_SITE%20WEB_Vos%20options%20sur%20demande_oct%202019_FR.pdf
27. https://www.packlink.com/fr-FR/blog/suivi-geodis/
28. https://rz3.aeb.de/docudata/system-descriptions/carrier-connect/sd-carrierconnect-carrieroverview/en-US/821884555821895051.html (Heppner EDI)
29. https://www.packlink.com/fr-FR/blog/france-express/
30. https://www.eurosender.com/fr/societes-transport/france-express
31. https://www.cep-research.com/?p=41200 (DHL Cormontreuil)
32. https://www.lejournaldesentreprises.com/breve/les-transports-lebrun-receptionnent-5-tracteurs-alimentes-lhuile-de-colza-2144859
33. https://journaldupoidslourd.com/transport/transports-lebrun-du-b100-pour-des-vins-de-champagne/
34. https://www.ltd-51.fr/transports-dedie.php ; https://www.ltd-51.fr/transport-de-champagne-dans-la-marne-51.php
35. https://viticolis.fr/secteurs/transport-de-vin-champagne/
36. https://www.pagesjaunes.fr/pros/57665355 (Transfret Champagne) ; https://www.pagesjaunes.fr/pros/08520898 (Mazet Champagne)
37. https://transporteur.tel/51-marne/reims/societe-de-transport-routier/19682-foselev-champagne.html
38. https://www.veolog.fr/agences/plateforme-logistique-chalons-en-champagne/
39. https://fr.kompass.com/s/transports-et-logistique/10/v/epernay/fr_21_51_51230/ ; https://fr.kompass.com/a/services-de-gestion-logistique/7594025/r/champagne-ardenne/fr_21/
40. https://www.118712.fr/professionnels/X0VRW1NcGgI (Mauffrey)
41. https://epernay-agglo.fr/print/pdf/node/9546
42. https://unemplacement.com/entrepots/marne-51/epernay-51200
43. https://industrie.usinenouvelle.com/fiche/etablissement/champagne-perrier-jouet-43676884
44. https://www.chronopost.fr/en/delivery/our-offers/chrono-viti ; https://www.chronopost.fr/sites/default/files/chronoviti.pdf ; https://www.chronopost.fr/sites/default/files/atoms/files/guide-export-chronoviti.pdf
45. https://www.lejournaldesentreprises.com/article/bordeaux-city-bond-et-chronopost-deploient-chronoviti-95222
46. https://www.macommune.info/chrono-viti-une-nouvelle-solution-pour-lenvoi-des-bouteille-de-bourgogne-dans-le-monde-entier
47. https://www.laposte.fr/envoyer/envoyer-bouteilles-vin ; https://www.laposte.fr/professionnel/expedier/livrer-bouteilles-vin-etranger ; https://www.laposte.fr/professionnel/expedier/expedier-vin-suisse
48. https://ups.com/fr/en/support/shipping-support/shipping-special-care-regulated-items/prohibited-items/wine ; https://muat2.ups.com/assets/resources/webcontent/en_US/wine_addendum.pdf
49. https://mydhl.express.dhl/us/en/help-and-support/customs-clearance-advice/alcoholic-beverages.html
50. https://www.eurosender.com/fr/envoyer-emballer/alcool/champagne ; https://www.eurosender.com/fr/envoyer-emballer/vin
51. https://www.reussir.fr/vigne/node/2838 (Iziwine, Wine Shipper)
52. https://www.reussir.fr/delegue-le-stockage-et-lexpedition-de-nos-vins-de-negoce-parce-que-lon-confiance ; https://www.reussir.fr/vigne/transport
53. https://www.lemoci.com/?p=142814 (VignoblExport / Hillebrand)
54. https://lemoci.com/?p=27181 (JF Hillebrand France)
55. https://www.lejournaldesentreprises.com/article/vineolis-investit-dans-un-service-logistique-pour-ses-clients-vignerons-et-negociants-1532285
56. https://www.lejournaldesentreprises.com/article/grace-au-e-commerce-dartess-voit-la-logistique-en-rose-129331
57. https://www.vitisphere.com/upload/images/Image/Plaquette%202LR.pdf
58. https://my.motherbase.ai/startup/114223-winetailors
59. https://www.b2log.fr/
60. https://support-pro.packlink.com/hc/en-gb/articles/210236985 ; https://www.packlink.com/fr-FR/envoyer-du-vin/
61. https://www.sendcloud.com/blog/shipping-to-france/
62. https://www.lafabriquedunet.fr/logiciels/alternatives/alternative-boxtal
63. https://cargoboard.com
64. https://www.freightwaves.com/news/technology-geodis-launches-upply-freight-marketplace ; https://www.upply.com/en/faq
65. https://docshipper.fr/?p=4175
66. https://www.douane.gouv.fr/demarche/echanger-des-produits-soumis-accise-en-regime-de-suspension-des-droits
67. https://www.douane.gouv.fr/demarche/echanger-des-produits-soumis-accise-en-regime-droits-acquittes
68. https://www.douane.gouv.fr/formalites-la-circulation-pour-le-vin-en-bouteilles
69. https://www.douane.gouv.fr/actualites/simplification-administrative-pour-les-professionnels-du-vin
70. https://form.douane.gouv.fr/sites/default/files/2021-05/07/guide_utilisateur_gamma_dtiplus_v2.0.pdf
71. https://www.douane.gouv.fr/GammaFormation/res/presentation_GAMMA_EMCS_operateur.pdf
72. https://moa.douane.gouv.fr/sites/default/files/documentation/pdf/gamma-gestion-de-l-accompagnement-des-mouvements-de-marchandises-soumises-a-accise.pdf
73. https://www.thetradehub.eu/en/reglementation/france/doctrine/decisions-administratives/da-18-006
74. https://www.thetradehub.eu/de/reglementation/france/eu/excise-2020-262/article/20
75. https://intercom.help/wineriz/fr/articles/13940285-creer-et-envoyer-un-dae-depuis-wineriz
76. https://customs.gov.mt/mc/other-pages/new-newsresult2/2023/01/26/changes-to-the-movement-of-duty-paid-harmonised-excise-items-as-established-by-the-new-eu-excise-directive-(2020-262)
77. https://legislation.gov.uk/eudr/2020/262/article/36?view=plain
78. https://questions.assemblee-nationale.fr/dyn/14/questions/QANR5L14QE26452.pdf ; https://questions.assemblee-nationale.fr/dyn/14/questions/QANR5L14QE30729.pdf
79. https://www.senat.fr/questions/base/2013/qSEQ130506603.html
80. https://www.vsnews.fr/images/Le_commerce_intracommunautaire_des_vins_a_destination_des_particuliers_-_Propositions_de_reforme.pdf
81. https://www.eurofiscalis.com/accises-france/ ; https://www.eurofiscalis.com/accises-allemagne/
82. https://Douane.gouv.fr/sites/default/files/2019-02/exportez-des-vins-et-spiritueux-en-chine-en-toute-securite-aubette.pdf
83. https://nouvelle-aquitaine.dreets.gouv.fr/sites/nouvelle-aquitaine.dreets.gouv.fr/IMG/pdf/cybertex_06_01_2022.pdf
84. https://vinepair.com/articles/three-tier-system-explainer/ ; https://joshuaelondon.substack.com/p/this-wine-costs-what ; https://www.winewithseth.com/winewiki/fob-free-on-board/
85. https://www.pleinchamp.com/actualite/en-2025-les-exportations-de-vins-et-spiritueux-en-recul-de-7-9-a-14-3-milliards-d-euros
86. https://jancisrobinson.com/zh-hans/articles/what-happens-when-wine-gets-hot
87. https://hull-repository.worktribe.com/OutputFile/4872083
88. https://www.lapassionduvin.com/autour-du-vin/20978-question-de-transport ; https://www.lapassionduvin.com/de-la-terre-au-verre/36108-les-transporteurs-la-logistique-du-vin
89. https://www.msc.com/fr/local-information/europe/france/france-wines-and-spirits
90. https://www.malt.fr/profile/catherinebrochard (in-house customs/transport role at a champagne house)
