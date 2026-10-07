# 02 — Software, CRM & Automation Landscape in Champagne

*Research date: 7 Oct 2026. Author: research agent (software/CRM focus).*

> **Method & limitations (read first).** WebFetch was blocked in this environment (DNS/egress policy denied every vendor domain: baqio.com, reussir.fr, douane.gouv.fr, capterra.fr…). Partway through, the team's shared WebSearch budget also ran out. So **every finding below comes from search-engine result summaries** (~35 queries, ~60 distinct URLs surfaced), not from pages I read in full. Vendor claims are self-reported marketing. Where sources conflict, I say so. Before anyone builds a sales pitch on a specific figure, open the cited URL and check it. Some vendor names in the brief **could not be verified** and are listed in §1.6.

---

## 0. Executive summary

- **Champagne has its own small software ecosystem.** Its production workflow (vins clairs → tirage → latte → pointe → dégorgement → dosage, the -15/+15 month aging moves) and its double declaration route (Comité Champagne extranet → douane CIEL) push growers toward local or "Champagne-mode" tools. The named players: **TER'Informatique** (Pierry, near Épernay), **Baqio Bulles**, **Vrille** (made by Egram, a Champagne web agency), **Wineriz** (800+ estates, Champagne clients, bought by Visma/Inqom in Sept 2026), **Vitisoft** (~2,000 grower customers nationally), **Gaïana/iD Systèmes** (now Orisha: iDViniStoria, ex-PAC Informatique with Roederer and Vranken-Pommery as historic clients) and **Isagri/Isavigne**. Big houses run SAP (Moët Hennessy is on S/4HANA with Salesforce around it).
- **Small-grower tools cost about €55–140/month** (Vrille €55–98, Baqio €790–1,090/yr, or €109–139/mo for Bulles, Wineriz from €129/feature/mo). Mid-market ERPs (Infologic Copilote, iDErp on Sage X3, Cap Vignes on Dynamics BC, Process2Wine) are quote-only.
- **Compliance is only half-automated.** Software can generate the e-DRM file, but the grower still uploads it to the Comité Champagne extranet and then **validates it manually on CIEL**. The DAE/DSA moved to **GAMMA2 on 25–26 June 2025**, with a REST/JSON API for registered EDI partners. Cellar registers (registres de cave) remain mandatory even with the e-DRM.
- **Digitisation is middling.** The 2022 Vin & Société barometer gave the sector a digital score of **47/100** (commercialisation 48/100). "Lack of time" was the top barrier, and about 25% of respondents see no point in digital. One (vendor-blog) source says **fewer than 10% of growers run their own e-shop**.
- **AI is just arriving, and only as bolt-ons.** Vitisoft's "Vinca" AI writes prospecting messages (10–15% of its ~2,000 users adopted it within months). Vrille ships a "Champagne AI assistant". Cap Vignes pitches Microsoft Copilot. Kavo claims MCP integration with Claude, ChatGPT and Mistral. None of them does end-to-end order-email → ERP → transport → customs automation, lead generation, or importer/CHR prospecting.
- **The opening for an automation agency:** integration and "glue" work (e-shop ↔ ERP ↔ carrier ↔ DAE), inbox and order automation, trade-show lead capture → CRM → follow-up sequences, B2B importer prospecting with scrapers, and AI copilots over the data growers already hold. All of this sits on top of the vertical tools rather than competing with them.

---

## 1. Wine and Champagne management software (ERP, cellar, sales)

### 1.1 Champagne-native or Champagne-adapted tools (small growers / RM-RC)

**TER'Informatique (Pierry, Épernay area)**: the incumbent local publisher.
- Products: **TER'Viti** (sales management for wine and Champagne, France and export), a **Champagne comptabilité-matières module that generates the e-DRM file** for upload to the Comité Champagne extranet, **TER'Registre** in three editions (Récoltant, Coopérative, Négociant) with automatic links and consistency checks between registers, and **PRESTA** for Champagne cooperatives ([ter-informatique.com](https://ter-informatique.com/); [registres 2023](https://ter-informatique.com/2023/01/17/registres-de-cave-champenois/); [TER'Registre](https://ter-informatique.com/produit/registre-de-cave-ter-registre/)).
- TER'Registre handles the déclarations préalables (tirage, enrichissement, acidification) and automates moves such as bottles passing from "-15 mois" to "+15 mois" ([search result summary of the product page](https://ter-informatique.com/produit/registre-de-cave-ter-registre/)).
- In 2018 it was waiting for the Comité Champagne specifications before building e-DRM integration ([Entre TER' et Ciel](https://ter-informatique.com/2018/12/entre-ter-et-ciel/)).
- No public price and no client list. It looks like on-premise/desktop heritage software (not verified).

**Baqio / Baqio Bulles (Dijon)**: a SaaS sales-management tool for wine, with a Champagne edition launched in **June 2023** ([Baqio blog](https://blog.baqio.com/2023/06/12/baqio-bulles-le-nouveau-logiciel-de-gestion-commerciale-dedie-aux-specificites-champenoises/); [Réussir](https://www.reussir.fr/vigne/baqio-adapte-son-logiciel-aux-vignerons-champenois)).
- Champagne features: entry of vins clairs and sugars, tirage and dosage liqueurs, tirages, stock "sur latte" and "sur pointe", <15 / >15 month wines, auto-generated CIVC declarations (sales by country/quality, DRM), DAE generation, English invoices and non-euro currencies. Champagne cellar registers are an optional module.
- Price: official page shows **Standard €790/yr and Plus €1,090/yr** (annual billing); a third party quotes **Bulles €109/mo (Standard) and €139/mo (Plus)** ([baqio.com/pricing](https://www.baqio.com/pricing); [lebonlogiciel](https://lebonlogiciel.com/organisation-facturation-et-planification-gestion-commerciale-erp-gpao/baqio/1987)). The allocation/primeur module costs +€200/yr ([Réussir](https://www.reussir.fr/articles/baqio-lance-un-module-pour-gerer-les-ventes-de-vin-par-allocation)).
- Champagne testimonials named on its site: **Champagne Berthelot-Piot, Delavenne, Cuillier** ([baqio.com](https://www.baqio.com/)). Sparkling News calls it one of the cheapest options on the market ([sparkling-news](https://www.sparkling-news.com/articles/564b673c-1dc6-f011-8195-000d3a2226fe/baqio-bulles-an-ally-to-sell-and-manage-champagne-stocks-even-faster-)).
- Integrations and API: **not verified** (my search returned nothing on Baqio connectors).

**Vrille (vrille.io / vrille.fr)**: an all-in-one app "built by Champagne winegrowers", published by **Egram**, a Champagne web agency.
- 11 modules: vineyard, harvest, cuverie, tirage, dégorgement, habillage, stock, AOC-compliant cellar register, and more. Includes a **"Champagne-specialised AI assistant"**. Data hosted on the publisher's own servers ([vrille.io](https://www.vrille.io/); [vrille.fr](https://www.vrille.fr/); [egram.fr](https://www.egram.fr/)).
- Price: **€89/mo annual or €98/mo monthly, +€20 per extra user**. The first year was free for beta users. One page shows **€55/mo**, so the price is inconsistent ([pressurage page](https://www.vrille.io/encyclopedie/pressurage)).
- Relevance: proof that a *local web agency* can launch a vertical SaaS in Champagne. Egram is a direct competitor or partner model for this agency.

**Wineriz (ex-LiveMarket, Bordeaux, founded 2020)**: an all-in-one tool covering POS, e-commerce site, invoicing, customs, CRM, agents/commissions and GAMMA2.
- Claims **800+ estates** and markets itself to "maisons de Champagne" ([wineriz.com](https://www.wineriz.com/); [clients](https://www.wineriz.com/clients/)). Champagne case study: **Champagne de Sousa (Avize)** replaced an "aging tool". Gains claimed: automated exports and invoicing, agent-commission handling, admin time saved ([case study, Aug 2025](https://www.wineriz.com/cas-client-champagne-de-sousa-logiciel-gestion-viticole-champagne/)). There is also a Champagne Camille Marcel storefront on app.wineriz.com ([link](https://app.wineriz.com/champagnecamillemarcel)).
- Price: **from €129 per feature per month**, with 0 reviews on Capterra and GetApp ([Capterra](https://www.capterra.com/p/10036667/Wineriz/); [GetApp](https://www.getapp.co.uk/software/2084116/wineriz)).
- **Acquired by Visma via its French subsidiary Inqom (accounting automation) in Sept 2026** ([CB Insights](https://www.cbinsights.com/company/wineriz)). Expect accounting automation to be bundled in. Exhibiting at **Viti Vini 2026 (Épernay, 13–16 Oct 2026)** ([wineriz.com](https://www.wineriz.com/salon-viti-vini-2026/)).

### 1.2 National grower and SME tools that are also used in Champagne

| Vendor / product | Notes |
|---|---|
| **Vitisoft / Vinca by Vitisoft** (Solumatic, Tours/Nantes) | Sales management plus integrated CRM: segmenting by show attended, product bought or revenue, email/SMS campaigns with open and click stats, mailings, event mini-sites, DRM/DMS ([Appvizer](https://www.appvizer.fr/operations/erp/vitisoft); [motherbase](https://beta.motherbase.ai/startup/150889-solumatic-vitisoft-padawine-viticode)). **About 2,000 grower customers.** AI module launched about early 2026; **10–15% adopted it within months**. It answers business questions and drafts prospecting messages ([Vitisphere via search summary](https://www.vitisphere.com/actualite-106400-une-intelligence-artificielle-developpee-sur-mesure-pour-la-filiere-vin.html)). Price on request. No Champagne-specific reference found. |
| **Isagri: Isavigne** (Beauvais) | The giant of French farm software. Isavigne is "the reference for commercial and regulatory management": entry/exit registers, bottling, capsules (CRD), DRM/DAE/DAI ([logiciels.pro](https://www.logiciels.pro/isavigne/); [comparateur](https://www.logiciels.pro/comparateur-logiciels-pour-lexploitation-de-vignoble/)). Bought **Wino** (wine-shop POS, 450 clients) and Spain's **Bacosoft** ([independant.io](https://independant.io/logiciel-de-caisse-isagri-met-la-main-sur-wino/); [La Gazette France](https://www.lagazettefrance.fr/article/isagri-acquiert-le-logiciel-espagnol-bacosoft)). Price on quote. No Champagne references confirmed. |
| **Gaïana / iD Systèmes → Orisha Agrifood** | Founded 1987, renamed Gaïana Feb 2023, Orisha took majority control May 2024. **2,000+ clients and 15,000 users** in wine and spirits, including "maisons de Champagne" ([idsystemes.com](https://www.idsystemes.com/); [perelafouine](https://perelafouine.com/groupe-id-systemes-devient-le-groupe-gaiana/); [CB Insights](https://www.cbinsights.com/company/id-systemes)). Products: **iDViniStoria** (sales management for SMEs, 3–15 seats, [page](https://idsystemes.com/progiciel-gestion-vin/idvinistoria)), **iDErp** (Sage X3-based), Bacchus (bought 2019), Asape (2021), **PAC Informatique** (sparkling specialist since 1981, products **Viti-PAC and Vino'Tech**, clients **Roederer and Vranken-Pommery**) ([Fusacq](https://www.fusacq.com/buzz/gaiana-rachete-le-logiciel-viti-vinicole-pac-informatique-a239077_fr_)), and Lavilog (2024, Gironde-focused) ([Fusacq](https://www.fusacq.com/buzz/l-editeur-de-solutions-verticalisees-gaiana-met-la-main-sur-lavilog-a246682_fr_)). **This is the strongest documented supplier to mid-size and large Champagne houses after SAP.** |
| **Wine'r** (Gomboc Solutions) | Traceability from vine to sale with integrated POS, highly configurable; described as "complete and affordable" ([Réussir](https://www.reussir.fr/vigne/winer-un-logiciel-complet-et-abordable)). Price not verified. |
| **Process2Wine** (distributed via Groupe Perret / Racine) | Web-based vine-to-bottling traceability. Explicitly targets **"Négociants, Maisons de Champagne"** ([brochure](https://racine.groupeperret.fr/files/users/fouzia/ficheprocess2wineBD.pdf)). Reportedly popular with Bordeaux and Champagne estates ([logiciels.pro comparateur](https://www.logiciels.pro/comparateur-logiciels-pour-lexploitation-de-vignoble/)). Capterra 4.4/5 on 5 reviews: good reporting, "vast and sometimes unwieldy" ([Capterra](https://www.capterra.fr/software/167549/process2wine)). |
| **agreo / Smag** | Vine and cellar technical traceability, used by cooperatives ([Smag ITW PDF](https://smag.tech/app/uploads/2018/04/ITW_VigneronsCreateurs.pdf)). Matters because the **phytosanitary register must be digital from 1 Jan 2027** ([Réussir via search](https://www.reussir.fr/vigne%2F/logiciel)). |

### 1.3 Mid-market ERPs (larger houses, négociants, cooperatives)

- **Infologic Copilote**: an agrifood ERP with a dedicated **"logiciel Champagne"** page. Covers plots, grape intake, cuverie, sparkling stock, mandatory documents, customs declarations, excise numbers, and **EDI to GAMMA for DAE/DSA**. Has 300–500 client references (figures vary). Named case: cooperative **AGAMY** ([infologic-copilote.fr/…/logiciel-champagne](https://www.infologic-copilote.fr/erp-agroalimentaire/logiciel-champagne/); [vin/alcools page](https://www.infologic-copilote.fr/erp-agroalimentaire/logiciel-vin-boissons-et-alcools/)). One search summary said its site lists Pol Roger, Champagne Pierre and Barons de Rothschild as clients, but a follow-up search **could not confirm this. Treat it as unverified.**
- **Orisha iDErp (on Sage X3)**: Orisha is hiring "Sage X3 Wine & Spirits" consultants for an unnamed "global W&S player" ([Orisha careers](https://careers.orisha.com/jobs/8082549-consultant-production-sage-x3-vins-spiritueux-h-f)). Absys Cyborg also pitches Sage X3 to Champagne houses ([Absys Cyborg](https://absyscyborg.com/fr/actualites/sage-x3-l-erp-ideal-pour-piloter-votre-maison-de-champagne)). Sage X3 case in sparkling wine: CFGV, 20M bottles, non-Champagne ([Sage](https://www.sage.com/fr-fr/blog/la-cfgv-sappuie-sur-un-erp-temoignage/)).
- **Cap Vignes**: a wine ERP on **Microsoft Dynamics 365 Business Central** with **Copilot AI** (sales forecasting, stock optimisation, drafting offers) ([cap-vignes.vin](https://cap-vignes.vin/); [producteurs/effervescents](https://cap-vignes.vin/producteurs-de-vins-et-spiritueux/)).
- **Winepilot** (bulk-to-bottle ERP, [winepilot.fr](https://winepilot.fr/actualites/erp-metiers-vin-winepilot/)), **SparkWine** by Greenspark (négoce and cooperatives, [greenspark.fr](https://greenspark.fr/sparkwine-negoce/)), **Isatech** wine ERP ([isatech.fr](https://www.isatech.fr/erp-vins-spiritueux/)), Digitalsace ([digitalsace.fr](https://digitalsace.fr/erp-specialise-vin)), Cerealog ([blog](https://www.cerealog.fr/blog/erp-vin-une-solution-adaptee-pour-les-professionnels-du-vin.html)). No Champagne references verified for any of them.
- **Odoo**: there is **no off-the-shelf French wine-excise (DRM/DAE) module.** Businesses commission custom DRM exports from freelancers ([Codeur.com project](https://www.codeur.com/projects/312470-developpement-odoo)). This is a clear niche for an integrator.
- **Divalto, Cegid**: no wine or Champagne evidence found.

### 1.4 The giants

- **Moët Hennessy (LVMH)** consolidated several SAP ECC instances into **one SAP S/4HANA** ("smart brownfield"), integrated with **Salesforce and Google Cloud**. It had to map **800+ applications** using LeanIX ([LeanIX blog](https://leanix.net/en/blog/moët-smart-brownfield); [IDC paper](https://www.leanix.net/en/download/moet-hennessy-using-ea-to-de-risk-sap-s4hana-transformation)). Other large groups (Lanson-BCC, Vranken-Pommery, Laurent-Perrier, Roederer) were **not verified** beyond the PAC Informatique link above. Giants are not a target for a small agency.

### 1.5 International wine software seen in French directories

vintrace, InnoVint, Ekos, VinSight, VineSpring, Commerce7/WineDirect (WineDirect Classic sunsets **31 Dec 2026**) ([Appvizer](https://www.appvizer.fr/loisirs/vignoble); [GetApp](https://www.getapp.fr/software/130551/winedirect)). They don't handle French DRM, CIVC or GAMMA, so they are rarely relevant for Champagne growers.

### 1.6 Names from the brief that I could NOT verify

- **Siwine, Inovin, Logivitis**: no software found. Likely confusions are InnoVint (US) and SOWINE (a wine-preservation gadget).
- **"Vinistoria"**: exists as **iDViniStoria** (Gaïana).
- **"Vinotec"**: probably **Vino'Tech** (PAC Informatique / Gaïana).
- **Oenoview**: exists, but it is **satellite vineyard monitoring** (ICV + TerraNIS), not an ERP.
- Mes Parcelles: exists (Chambres d'agriculture, [mesparcelles.fr](https://mesparcelles.fr/actualites/toutes-les-actualites/detail-de-lactualite/le-digital-a-la-conquete-de-nos-vignobles-1)). Not researched further.
- Geoviti, Cultivision, Vinsoft, Agrosoft, eVineyard: **not researched** (search budget ran out). Treat them as unverified.

---

## 2. Compliance stack: what is digital and what is still manual

| Obligation | System | Automation level |
|---|---|---|
| **DRM** (monthly stock/excise return) | Champagne: **e-DRM entered or uploaded on the Comité Champagne extranet** (extranet.comitechampagne.fr), signed there, sent instantly to **CIEL**. The operator then **logs into ProDouane and validates it manually** ([CIVC eDRM PDF 2017](https://www.union-champagne.fr/content/106/documents/CIVC%20pr%C3%A9sentation%20et%20d%C3%A9monstration%20de%20l'eDRM.pdf); [TER guide 2022](https://ter-informatique.com/2022/09/29/e-drm-champenoise-recoltant-et-negociant/)). Due by the 10th of the following month. | **Semi-automated.** Software (TER, Baqio, Isavigne, Vitisoft) generates the file. There is always a human upload-and-validate step. I found no public DRM API. Other regions use the same pattern through Declarvins ([Côtes-du-Rhône](https://www.syndicat-cotesdurhone.com/upload/article/file/dsdai-68bee7db913b1.pdf)). CIEL has a "CIEL2" version ([douane](https://www.douane.gouv.fr/service-en-ligne/declaration-fiscale-sur-les-vins-et-alcools-ciel)). |
| **DAE / DSA / MVV** (movement documents) | **GAMMA2.** GAMMA Legacy and MVV were shut down on **25 June 2025**, with a big-bang switch to GAMMA2 on 26 June. Wine-specific change: X000/X001 entries moved to MVV codes M001/M009. The **MAREVA interface was replaced by a REST API, and messages moved from XML to JSON**. Customs ran e-learning from April 2025 ([douane news](https://www.douane.gouv.fr/actualites/circulation-des-produits-soumis-accises-lancement-dune-e-formation-pour-anticiper-la); [EDI presentation](https://douane.gouv.fr/sites/default/files/2024-08/13/DGDDI_GAMMA2_MigrationDAE_DSA_Pr%C3%A9sentation%20EDI.pdf); [Q&A](https://douane.gouv.fr/sites/default/files/2024-08/13/QuestionsReponsesGAMMA2_MigrationDAEDSA.pdf); [Réussir](https://www.reussir.fr/douanes-anticipez-la-bascule-du-25-juin-sur-gamma2-pour-vos-mouvements-de-vin); [Wineriz guide](https://www.wineriz.com/gamma2-douane-domaine-viticole-guide/)). | **API exists, but only for registered EDI operators.** Joining requires the software publisher's name and version and the EDI provider's SIRET ([GAMMA2 adhesion form](https://www.douane.gouv.fr/sites/default/files/2025-06/27/Formulaire%20d%27adh%C3%A9sion%20GAMMA2.pdf)). Most small growers type documents into the GAMMA2 web interface. Its new "favourites" feature is the closest thing to templates. |
| **Registres de cave** (tirage, assemblage, dégorgement, acidity) | Paper or software. **Still mandatory despite the e-DRM** and checked at inspections ([TER](https://ter-informatique.com/2023/01/17/registres-de-cave-champenois/)). | Software-assisted (TER'Registre, Baqio Bulles option, Vrille). Many small growers likely still keep paper (inferred, not measured). |
| **Déclaration de récolte, DMS, eCO, CVI** | Comité Champagne extranet plus douane portals. Harvest declaration due early November ([union-champagne vendange PDF](https://www.union-champagne.fr/content/106/documents/Partie%204%20-%20Vendange.pdf)). | Web forms. No evidence of APIs. Training is sold for the extranet itself ([SC Conseil](https://www.scconseil.fr/se-former-a-lusage-de-lextranet-du-civc/)), which is itself a sign of friction. |
| **Upcoming** | Digital phytosanitary register (1 Jan 2027); **e-invoicing reform** (Wineriz blog on electronic invoicing for growers, [link](https://www.wineriz.com/facture-electronique-reglementation-viticulteurs/)); smart wine labelling, 2025 ([Wineriz](https://www.wineriz.com/etiquetage-intelligent-vin/)). | Each deadline drives software purchases and creates "panic demand". |

The AI angle has already started here. The **"Lucien"** assistant (WineTech / Vigne Libre) explains how to fill **box 11 bis of the DSA** ([Vitisphere](https://www.vitisphere.com/actualite-106400-une-intelligence-artificielle-developpee-sur-mesure-pour-la-filiere-vin.html)). Regulatory Q&A is a recognised pain point.

---

## 3. CRM and sales tools

- **Do small growers use a CRM?** No Champagne-specific measurement was found.
  - The 2017 Nantes barometer reported **77% with a "CRM"**, 72% with a website and 23% with an online shop. But that covers about 100 Muscadet producers, and "CRM" most likely means a customer file in their management software ([Ixarys / Vin & Société summaries](https://www.ixarys.fr/l-usage-du-numerique-dans-la-filiere-viticole-ou-en-est-on-b50.php); [TEMA](https://www.tema-agriculture-terroirs.fr/mon-viti/actualites/les-vignerons-sont-ils-connectes-858040.php)).
  - **In practice, the "CRM" of most growers is the customer module of their sales/DRM software** (Vitisoft, Baqio, Isavigne, TER'Viti). Those modules hold customer files, price lists, show tags, email/SMS campaigns and order entry. **Generic CRMs (HubSpot, Pipedrive, Sellsy, Axonaut, Zoho): no evidence of meaningful adoption by Champagne growers was found.**
  - Excel and Gmail remain the default for prospecting and importer follow-up. That is inferred from vendor messaging (Pipedrive and independant.io Excel-CRM templates target exactly this group) and from the "lack of time" barrier.
- **Field sales and agents:** Wineriz handles agent commissions ([de Sousa case](https://www.wineriz.com/cas-client-champagne-de-sousa-logiciel-gestion-viticole-champagne/)). Moovago targets wine and spirits sales reps ([moovago](https://moovago.com/en/use-cases/crm-software-for-wine-and-spirits-sales-representatives/)).
- **B2B ordering and trade marketplaces (France):**
  - **WineSitting**, a Mirakl-based CHR marketplace launched Dec 2021 ([Mirakl](https://www.mirakl.com/fr-FR/news/winesitting-marketplace-mirakl-vin-spiritueux-professionnels-restauration-distribution)).
  - **We Are Wine**, caviste purchasing collective ([Réussir](https://www.reussir.fr/vigne/trouvez-vos-clients-cavistes-sur-we-are-wine)).
  - **Bottl**, producer ↔ caviste platform at €89 / €189 / €339 per month ([Maddyness](https://www.maddyness.com/2022/02/17/bottl-lien-cavistes-producteurs-francais/)).
  - **Les Grappes Pro** ([motherbase](https://my.motherbase.ai/startup/9683-les-grappes)) and **Safetee.io**, B2B catalogue and orders ([Appvizer](https://www.appvizer.fr/loisirs/vignoble/safetee)).
  - "Sowine", "Vinatis Pro", "Wine Platform" and "Vinsdesvignerons" as B2B portals: **not found**.
- **Consumer marketplaces where growers sell:**
  - **Twil** (since 2014, grower-direct), **Les Grappes** (about 1,200 growers), **Avenue des Vins**, **Vinatis** (online retailer, not a marketplace) and **Champmarket** (Champagne-specific, e-commerce plus social marketing for houses and growers) ([gust Champmarket](https://gust.com/companies/champmarket); [Twil](https://2050analytics.com/fr/org/100791.twil-the-wine-i-love); [Réussir e-commerce](https://www.reussir.fr/vigne/quelle-plate-forme-de-e-commerce-choisir)).
  - Marketplace model: the grower lists, ships and invoices, and pays a commission plus an optional subscription.

## 4. E-commerce, DTC and wine tourism

- **E-shops:** growers use generic **WooCommerce, Shopify and Wix**, local agency sites (e.g. **echampagne.pro**, **Egram**), or the e-shop built into their management software (Wineriz, Gaïana's e-commerce platform).
  - Shopify's French blog says online wine sales are 9–11% of the market but **fewer than 10% of growers have their own online shop**. This is a vendor blog, so treat it with caution ([Shopify](https://www.shopify.com/fr/blog/vente-vin-en-ligne)).
  - Shipping goes through La Poste/Colissimo, Chronopost, Packlink and Sendcloud. Export excise and duty-paid shipping uses specialists such as **Iziwine** ([forum/Réussir summaries](https://www.reussir.fr/vigne/node/2838); [Packlink](https://www.packlink.com/fr-FR/envoyer-du-vin/)).
  - Connectors: Sendcloud and Colis Privé plug into Shopify, Woo and PrestaShop ([Sendcloud](https://www.sendcloud.com/fr-be/integrations/)), but **none of them connects to the DRM/DAE side.** The e-shop → stock → DRM sync is the integration gap.
- **Wine clubs / subscriptions:** **no French equivalent of Commerce7 or WineDirect was found.** Growers improvise with WooCommerce Subscriptions or "allocation" modules (Baqio's +€200/yr). Commerce7 runs about $299/user/month ([toolradar](https://toolradar.com/alternatives/commerce7)).
- **Wine tourism booking:**
  - **Winalist**: French, founded 2017, 2,050+ wineries listed, 11 languages, free listing plus back-office. A big Champagne house tasting shows €80 for 2 with 4.74/5 from 3,666 reviews ([winalist.fr](https://www.winalist.fr/); [hosts](https://www.winalist.fr/s/hosts)).
  - **WineTourBooking**: founded 2012, Bordeaux-centric, current status unclear ([DigitalFoodLab](https://digitalfoodlab.com/en/foodtech-database/wine-tour-booking)).
  - Plus tourist-office listings (Épernay, Châlons) and Winedering.
  - Most small growers likely take bookings by phone or email (inferred). Generic tools (Rezdy, Regiondo) were not verified for Champagne.

## 5. Digital maturity data

- **Vin & Société barometer 2022** (first edition, 1,000+ respondents, 90% wine estates):
  - Overall digital score **47/100**: viticulture 40, equipment and logistics 52, **commercialisation 48**, communication 47, training 55.
  - 52% use connected tools in plots and 26% use disease-detection tools. 60% are *interested* in traceability software.
  - Barriers: **lack of time** (first at every stage), then money. **About 25% see no point in digital.** The next edition was promised "in ~4 years" (about 2026). I did not check whether it has been published.
  - Sources: [vinetsociete.fr](https://www.vinetsociete.fr/etude/barometre-usages-numeriques-filiere-vin/); [mon-viti](https://mon-viti.com/filinfo/vie-de-filiere/le-digital-penetre-progressivement-le-quotidien-des-viticulteurs); [Lab Alimentation NA](https://www.lab-alimentation-nouvelle-aquitaine.fr/actualites/barometre-2022-des-usages-du-numerique-pour-la-filiere-viti-vinicole).
- **Agreste RA2020:** 24% of conventional specialised vineyards sell through short circuits, vs 62% of organic ones. 82% of those use on-farm sales. No national figure on online sales ([Agreste](https://agreste.agriculture.gouv.fr/agreste-web/download/publication/publie/Pri2305/Primeur2023-5_CircuitCourt-RA2020.pdf)).
- **Adoption signals from vendors:** Vitisoft about 2,000 growers, Wineriz 800+ estates, Gaïana 2,000+ clients, Winalist 2,050+ wineries.
- **La WineTech association:** founded late 2019, 110–130+ startups, backed by LVMH, Crédit Agricole and **Bollinger** ([Maddyness](https://www.maddyness.com/?p=1345964); [JDN](https://www.journaldunet.com/retail/1499559-laurent-david-winetech/)).
- Average admin hours per grower: **not found.**

## 6. Comparison table

| Tool | Type | Target size | Champagne customers? | Price (public) | API / integrations | AI features |
|---|---|---|---|---|---|---|
| TER'Informatique (TER'Viti, TER'Registre, PRESTA) | Sales + registers + e-DRM | RM/RC, cooperatives, small négoce | **Yes**, Champagne-native (no names public) | Quote | e-DRM file export to CIVC; no API seen | None found |
| Baqio Bulles | SaaS sales + Champagne production + DRM/DAE | Small growers | **Yes**: Berthelot-Piot, Delavenne, Cuillier | €790–1,090/yr; Bulles about €109–139/mo; +€200 allocations | Not verified | None found |
| Vrille (Egram) | All-in-one Champagne app | Small growers | **Yes**, built by Champagne growers | €89–98/mo (+€20/user); €55 also shown | Not verified | **Yes**, Champagne AI assistant |
| Wineriz (Visma/Inqom) | POS + e-shop + invoicing + customs + CRM | Small/mid estates | **Yes**: Champagne de Sousa, Camille Marcel | From €129/feature/mo | GAMMA2 support; accounting via Inqom likely | Not verified |
| Vitisoft / Vinca | Sales mgmt + CRM + DRM | Growers, négoce, cavistes | Not confirmed | Quote | Not verified | **Yes**: Q&A + prospecting drafts (10–15% adoption) |
| Isagri Isavigne | Sales + regulatory (DRM/DAE/CRD) | Growers to mid | Not confirmed | Quote ("from €0" on listing) | Isagri ecosystem (accounting) | Not found |
| Gaïana/Orisha (iDViniStoria, iDErp, Viti-PAC, Vino'Tech) | Sales mgmt / ERP / regulatory / e-commerce | SME to large | **Yes**: Roederer, Vranken-Pommery (via PAC, historic) | Quote | Sage X3 ecosystem | Not found |
| Infologic Copilote | Agrifood ERP with Champagne vertical | Mid/large houses, cooperatives | Champagne page; AGAMY cooperative; others unverified | Quote | **EDI to GAMMA (DAE/DSA)** | Not found |
| Cap Vignes | ERP on Dynamics 365 BC | Négoce, mid | Not confirmed (targets sparkling) | Quote | Microsoft stack | **Yes**, Copilot |
| Process2Wine | Vine-to-bottling traceability | Estates, négoce, Champagne houses | Targeted; popularity claim unverified | Quote | Not verified | Not found |
| SAP S/4HANA + Salesforce | Enterprise ERP/CRM | Giants (Moët Hennessy) | **Yes**: MH | Enterprise | Full | Vendor-native |
| Kavo | Wine management software | Small/mid | Not confirmed | Not verified | **Claims MCP** (Claude, ChatGPT, Mistral) | Yes (claimed) |
| Winalist | Wine tourism booking marketplace | All | **Yes**, Champagne listings | Free listing; commission model (not verified) | Not verified | No |
| Bottl / WineSitting / We Are Wine | B2B trade marketplaces | Small/mid producers | Not confirmed | Bottl €89–339/mo; WAW revenue-based | Mirakl (WineSitting) | No |

---

## 7. Gaps and automation opportunities (for an AI/automation agency)

**What the vertical tools do NOT do (based on everything above):**

1. **No end-to-end order automation.** Orders still arrive by email, phone, PDF purchase order, WhatsApp or importer spreadsheets and are retyped into Baqio, Isavigne or TER. No vendor showed inbox parsing or AI order capture.
2. **The compliance chain is broken at the human-validation step.** The e-DRM is generated, then uploaded to the CIVC extranet, then validated on CIEL. DAEs are typed into the GAMMA2 web UI unless the grower uses a costly EDI partner. There is no CIEL API, and the GAMMA2 REST API requires EDI accreditation.
3. **Poor integration between ERP, e-shop, carrier and customs.** Shopify/Woo plugins handle shipping labels but not excise, and none sync back to the DRM. Odoo has no French wine-excise module. Each grower patches this together by hand.
4. **No lead generation or prospecting.**
   - Vendor CRM modules manage *existing* customers (segments, mailings).
   - None of them finds new **importers, cavistes, CHR or corporate-gift buyers**, enriches contacts, or runs follow-up sequences.
   - Vitisoft's AI only *drafts* prospecting messages.
   - Trade-show lead capture (Viti Vini, Wine Paris, ProWein, Vinexpo) is still business cards and Excel.
5. **No AI over their own data, beyond first steps.** Vrille, Vitisoft/Vinca, Cap Vignes Copilot and Kavo MCP are early. The market is clearly *receptive* (10–15% adoption in months), but the features are shallow.
6. **No wine-club/DTC retention tooling** comparable to Commerce7 (subscriptions, allocations, churn, birthday or reorder triggers).
7. **Wine tourism:** booking marketplaces exist, but there is no CRM capture of visitors → newsletter → reorder.
8. **Interprofessional and regulatory deadline anxiety.** GAMMA2, the e-invoicing reform, the digital phyto register (2027) and smart labels are recurring triggers that vendors use in content marketing (Wineriz's blog) and that an agency can ride.

**Concrete offers that fit a small agency (complementing the vertical tools, not replacing them):**

- **"Bulles Inbox Agent":** AI parsing of order emails and importer purchase orders → draft order in Baqio, Wineriz or Isavigne (or a Google Sheet) → pro-forma invoice and DAE draft checklist → confirmation email. Feasibility depends on each vendor's API, which is **unverified**. The fallback is RPA or browser automation, or CSV import.
- **E-shop ↔ cellar sync:** Shopify/WooCommerce orders → stock decrement and DRM-ready monthly movement export (the CSV format TER, Baqio or the CIVC expects) plus carrier label (Sendcloud).
- **Lead-gen engine for export:** scrapers of importer and distributor lists (customs data, trade-fair exhibitor lists, Wine-Searcher merchant listings, LinkedIn) → enriched CRM (HubSpot free or Pipedrive) → personalised sequences in French and English → meeting booking. Champagne growers are export-hungry, and no vendor sells this.
- **Trade-show kit:** QR/badge lead capture at Viti Vini, Wine Paris and ProWein → CRM → 3-step follow-up → sample-order workflow.
- **Wine-tourism CRM:** Winalist and website bookings → visitor CRM → post-visit email with reorder link, plus a club or allocation programme.
- **Compliance copilot:** a RAG assistant over douane, CIVC and AOC rules (like Lucien, but private to the grower), plus monthly reminders and a pre-filled DRM checklist.
- **Custom Odoo or Airtable "light ERP"** with DRM/registre exports for mid-size growers and négociants outgrowing Excel who find SAP or iDErp overkill.

**Risks and competition:**
- Vertical vendors are adding AI quickly: Visma now owns Wineriz, and Orisha/Gaïana is consolidating.
- Local agencies already in place: Egram/Vrille and echampagne.pro.
- Customs and CIVC portals have no public APIs, so the last mile of compliance stays manual or semi-automatic.
- Growers often cite lack of time and see no ROI (about 25% see no point in digital), so offers must be packaged as done-for-you with clear time savings.

---

## 8. Sources (surfaced and used; content taken from search summaries, not full-page reads)

1. https://ter-informatique.com/
2. https://ter-informatique.com/2023/01/17/registres-de-cave-champenois/
3. https://ter-informatique.com/produit/registre-de-cave-ter-registre/
4. https://ter-informatique.com/2022/09/29/e-drm-champenoise-recoltant-et-negociant/
5. https://ter-informatique.com/2018/12/entre-ter-et-ciel/
6. https://blog.baqio.com/2023/06/12/baqio-bulles-le-nouveau-logiciel-de-gestion-commerciale-dedie-aux-specificites-champenoises/
7. https://www.baqio.com/pricing, https://www.baqio.com/baqio-bulles, https://www.baqio.com/
8. https://lebonlogiciel.com/organisation-facturation-et-planification-gestion-commerciale-erp-gpao/baqio/1987
9. https://www.reussir.fr/vigne/baqio-adapte-son-logiciel-aux-vignerons-champenois
10. https://www.reussir.fr/articles/baqio-lance-un-module-pour-gerer-les-ventes-de-vin-par-allocation
11. https://www.sparkling-news.com/articles/564b673c-1dc6-f011-8195-000d3a2226fe/baqio-bulles-an-ally-to-sell-and-manage-champagne-stocks-even-faster-
12. https://www.vrille.io/, https://www.vrille.fr/, https://www.vrille.io/encyclopedie/pressurage, https://www.egram.fr/
13. https://www.wineriz.com/, https://www.wineriz.com/clients/, https://www.wineriz.com/cas-client-champagne-de-sousa-logiciel-gestion-viticole-champagne/, https://www.wineriz.com/gamma2-douane-domaine-viticole-guide/, https://www.wineriz.com/salon-viti-vini-2026/, https://www.wineriz.com/facture-electronique-reglementation-viticulteurs/
14. https://www.capterra.com/p/10036667/Wineriz/ ; https://www.getapp.co.uk/software/2084116/wineriz ; https://www.cbinsights.com/company/wineriz ; https://www.cfnews.net/L-actualite/Capital-innovation-developpement/Operations/Amorcage/Wineriz-trinque-avec-un-FO-et-des-BA-489972
15. https://www.appvizer.fr/operations/erp/vitisoft ; https://beta.motherbase.ai/startup/150889-solumatic-vitisoft-padawine-viticode
16. https://www.vitisphere.com/actualite-106400-une-intelligence-artificielle-developpee-sur-mesure-pour-la-filiere-vin.html
17. https://www.logiciels.pro/isavigne/ ; https://www.logiciels.pro/comparateur-logiciels-pour-lexploitation-de-vignoble/
18. https://independant.io/logiciel-de-caisse-isagri-met-la-main-sur-wino/ ; https://www.lagazettefrance.fr/article/isagri-acquiert-le-logiciel-espagnol-bacosoft
19. https://www.idsystemes.com/ ; https://idsystemes.com/progiciel-gestion-vin/idvinistoria ; https://perelafouine.com/groupe-id-systemes-devient-le-groupe-gaiana/ ; https://www.cbinsights.com/company/id-systemes
20. https://www.fusacq.com/buzz/gaiana-rachete-le-logiciel-viti-vinicole-pac-informatique-a239077_fr_ ; https://www.fusacq.com/buzz/l-editeur-de-solutions-verticalisees-gaiana-met-la-main-sur-lavilog-a246682_fr_
21. https://careers.orisha.com/jobs/8082549-consultant-production-sage-x3-vins-spiritueux-h-f ; https://absyscyborg.com/fr/actualites/sage-x3-l-erp-ideal-pour-piloter-votre-maison-de-champagne ; https://www.sage.com/fr-fr/blog/la-cfgv-sappuie-sur-un-erp-temoignage/
22. https://www.infologic-copilote.fr/erp-agroalimentaire/logiciel-champagne/ ; https://www.infologic-copilote.fr/erp-agroalimentaire/logiciel-vin-boissons-et-alcools/
23. https://cap-vignes.vin/ ; https://winepilot.fr/actualites/erp-metiers-vin-winepilot/ ; https://greenspark.fr/sparkwine-negoce/ ; https://www.isatech.fr/erp-vins-spiritueux/
24. https://racine.groupeperret.fr/files/users/fouzia/ficheprocess2wineBD.pdf ; https://www.capterra.fr/software/167549/process2wine
25. https://www.reussir.fr/vigne/winer-un-logiciel-complet-et-abordable ; https://smag.tech/app/uploads/2018/04/ITW_VigneronsCreateurs.pdf
26. https://leanix.net/en/blog/moët-smart-brownfield ; https://www.leanix.net/en/download/moet-hennessy-using-ea-to-de-risk-sap-s4hana-transformation
27. https://www.douane.gouv.fr/actualites/circulation-des-produits-soumis-accises-lancement-dune-e-formation-pour-anticiper-la ; https://douane.gouv.fr/sites/default/files/2024-08/13/DGDDI_GAMMA2_MigrationDAE_DSA_Pr%C3%A9sentation%20EDI.pdf ; https://douane.gouv.fr/sites/default/files/2024-08/13/QuestionsReponsesGAMMA2_MigrationDAEDSA.pdf ; https://www.douane.gouv.fr/sites/default/files/2025-06/27/Formulaire%20d%27adh%C3%A9sion%20GAMMA2.pdf ; https://www.plus.transformation.gouv.fr/experiences/6219949_mail-surrealiste
28. https://www.reussir.fr/douanes-anticipez-la-bascule-du-25-juin-sur-gamma2-pour-vos-mouvements-de-vin
29. https://www.douane.gouv.fr/service-en-ligne/declaration-fiscale-sur-les-vins-et-alcools-ciel ; https://www.syndicat-cotesdurhone.com/upload/article/file/dsdai-68bee7db913b1.pdf
30. https://www.union-champagne.fr/content/106/documents/CIVC%20pr%C3%A9sentation%20et%20d%C3%A9monstration%20de%20l'eDRM.pdf ; https://www.union-champagne.fr/content/106/documents/Partie%204%20-%20Vendange.pdf ; https://www.scconseil.fr/se-former-a-lusage-de-lextranet-du-civc/
31. https://www.vinetsociete.fr/etude/barometre-usages-numeriques-filiere-vin/ ; https://mon-viti.com/filinfo/vie-de-filiere/le-digital-penetre-progressivement-le-quotidien-des-viticulteurs ; https://www.lab-alimentation-nouvelle-aquitaine.fr/actualites/barometre-2022-des-usages-du-numerique-pour-la-filiere-viti-vinicole ; https://www.ixarys.fr/l-usage-du-numerique-dans-la-filiere-viticole-ou-en-est-on-b50.php
32. https://agreste.agriculture.gouv.fr/agreste-web/download/publication/publie/Pri2305/Primeur2023-5_CircuitCourt-RA2020.pdf
33. https://www.shopify.com/fr/blog/vente-vin-en-ligne ; https://www.reussir.fr/vigne/quelle-plate-forme-de-e-commerce-choisir ; https://gust.com/companies/champmarket ; https://2050analytics.com/fr/org/100791.twil-the-wine-i-love
34. https://www.mirakl.com/fr-FR/news/winesitting-marketplace-mirakl-vin-spiritueux-professionnels-restauration-distribution ; https://www.reussir.fr/vigne/trouvez-vos-clients-cavistes-sur-we-are-wine ; https://www.maddyness.com/2022/02/17/bottl-lien-cavistes-producteurs-francais/ ; https://www.appvizer.fr/loisirs/vignoble/safetee
35. https://www.winalist.fr/ ; https://www.winalist.fr/s/hosts ; https://digitalfoodlab.com/en/foodtech-database/wine-tour-booking
36. https://toolradar.com/alternatives/commerce7 ; https://www.getapp.fr/software/130551/winedirect
37. https://www.maddyness.com/?p=1345964 ; https://www.journaldunet.com/retail/1499559-laurent-david-winetech/
38. https://www.sendcloud.com/fr-be/integrations/ ; https://www.packlink.com/fr-FR/envoyer-du-vin/
39. https://www.codeur.com/projects/312470-developpement-odoo
40. https://www.vinabox.fr/actu/filiere-business/vinitech-2026-innovations-ia-assemblage-drone-cuves-palmares/ ; https://www.lekavo.com/articles/fonctionnalites-logiciel-viticole

**Open questions for a follow-up pass (needs working WebFetch or more search budget):** Baqio, Wineriz and Isavigne API docs; a TER'Informatique client count; Vin & Société barometer 2026 edition; Capterra and Facebook-group complaints; Geoviti, Cultivision, Vinsoft and Agrosoft existence; Champagne-specific share of growers with an e-shop.
