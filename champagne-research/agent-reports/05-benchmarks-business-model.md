# 05 — Benchmarks & Business-Model Evidence for a Champagne AI/Automation Play

*Research date: 2026-10-07. Scope: what wine-tech/automation products have proven they can sell, what agencies charge, how NextAutomation's real-estate playbook translates, legal risks (Loi Évin, GDPR, cold-calling, AI Act), and sizing. Excludes champagne market structure, the French wine software landscape in depth, logistics and digital maturity (covered by other agents).*

**Method note / limitations.** About 45 web searches were run. WebFetch failed (DNS errors) for most domains, so most figures come from search-result summaries of the cited pages. The shared web-search budget ran out before I could check three things: the exact wording of the Loi Évin article L3323-4 list, 2024 champagne shipments by category of operator, and the details of the 2024 Bertrand/Anna Rvr judgment. Those points are marked **[from general knowledge — verify]**. Figures marked **(F)** are sourced facts. Figures marked **(E)** are my estimates.

---

## 1. Executive summary

1. **Wine-tech that sells is boring infrastructure with clear ROI, priced by revenue tier.** DTC/club platforms (Commerce7, WineDirect, eCellar, Vinoshipper), production/compliance tools (InnoVint, vintrace, Ekos) and B2B marketplaces (Provi/SevenFifty) all scaled. They charge **$59–$1,250/month** plus transaction fees, tiered by the winery's DTC revenue. None of them scaled on "AI".
2. **The sector is consolidating.** Fullsteam (owner of Commerce7) bought WineDirect's SaaS arm in Jan 2025. Encompass bought vintrace (2022), Andavi bought GreatVines (2021), Provi merged with SevenFifty (2022) and Next Glass bought Ekos (Oct 2025). Platforms are converging, which leaves room for a **service and integration layer** on top of them.
3. **AI-native wine products are early, vendor-claimed and mostly US-based.** Examples: WineSpeak.ai concierges, The Wine Agent (from $69/mo), RedChirp SMS (it claims $50.6M of attributed sales), vinSUITE "Ask Vinny" (Sept 2026), COLAClear label pre-screening (beta May 2026), and Vinte/BestWineImporters for importer prospecting. I found **no independent ROI case study**.
4. **France has software but almost no wine-specialised automation agency.** France has ERP/commercial tools (Baqio, including "Baqio Bulles" for champagne; Solumatic Vitisoft with its "Vinca" conversational AI), marketing agencies (SOWINE, whose clients include Bollinger, Mumm and Philipponnat) and marketplaces (Winalist, Vinexposium Connect). I found **no agency that sells done-for-you AI and automation to wine estates**. That is the white space.
5. **Agency pricing in France (F):** monthly retainers of €300–900 HT. A simple workflow costs €800–2,000 from a freelancer and €5,000–15,000 from an established agency. A custom system costs €4–6k to set up plus €50–100/mo to run.
6. **Legal risk is real but manageable, and it shapes the product.** The Loi Évin is a "permitted unless listed" regime: content must stick to objective information, terroir and heritage, and carry the health warning. Influencer-style "lifestyle" content has been sanctioned in court. Since **11 Aug 2026**, B2C phone canvassing in France needs **opt-in consent**, which kills outbound voice AI to consumers. Since **2 Aug 2026**, the EU AI Act Art. 50 requires voice and chat agents to disclose that they are AI. The safest products are **inbound, B2B and back-office**.
7. **Sizing (E).** Champagne SAM is about €10–15M/yr (≈1,500 serious growers plus ≈150 mid maisons). A France-wide wine and spirits TAM is about €60–90M/yr at agency price points. A realistic 3-year target for one agency is €0.5–1M ARR.

---

## 2. Benchmark table: international wine-tech that has proven it sells

| Company (country) | Category / pain solved | Pricing (F unless noted) | Scale / funding (F) | M&A / status | In France? |
|---|---|---|---|---|---|
| **Commerce7** (CA/US) | DTC e-commerce, club, POS, CRM | Lite $59/mo (0% fee, <$100k DTC); Basic $149 + 1.5%; Pro $399 + 1% ($600k–4M); Experience $1,249 + 0.75% ($4–6M); Enterprise custom ([pricing](https://salessite-v3.commerce7.com/pricing/)) | "3,500 wineries" vs 1,700+ in 2023 and 750+ in 2021 ([commerce7.com/pricing](https://commerce7.com/pricing)) | Owned by Fullsteam, which acquired WineDirect SaaS in Jan 2025 | Some international clients; no French localisation found |
| **WineDirect** (US) | DTC/club platform plus fulfilment | Revenue-based (not public) | 1,800+ wineries at sale ([Houlihan Lokey](https://hl.com/about-us/transactions/winedirect-fullsteam/)) | SaaS sold to Fullsteam, closed 21 Jan 2025; fulfilment stayed separate and became Commerce7's preferred partner ([WIA](https://wineindustryadvisor.com/2025/01/16/afternoon-brief-2783/)) | No |
| **eCellar** (US) | DTC/club | Pro $450/mo (<$500k DTC); Estate $850 ($0.5–2M); Enterprise $1,250 ($2–5M); commission-free ([FitGap](https://us.fitgap.com/products/035033/ecellar)) | n/a | — | No |
| **OrderPort** (US) | POS, e-com, club, reservations, CRM, email/SMS | Listed "from $149/mo" (unverified) ([SourceForge](https://sourceforge.net/software/product/eCellar/alternatives)) | n/a | — | No |
| **Vinoshipper** (US) | DTC plus compliance-as-a-service (licences, excise, TTB labels) | No monthly fee; 1.85% + $0.75/item shipped plus 2.9% processing; POS 1.25% ([pricing](https://www.vinoshipper.com/pricing)) | "2,000+ wineries"; compliance services added Nov 2024 ([WIA](https://wineindustryadvisor.com/2024/11/12/the-us-wine-industry-welcomes-third-major-compliance-partner/)) | — | No |
| **InnoVint** (US) | Production/cellar operations, compliance records | Quote only | Bootstrapped; about $3.1M revenue, ~4,100 customers (Latka estimate) ([Latka](https://getlatka.com/companies/innovint)); Duckhorn chose it in Mar 2026 | — | No |
| **vintrace** (AU/US) | Production/compliance | From ~$95/mo ([GetApp](https://www.getapp.com/winery-software/a/vintrace)) | — | Acquired by Encompass Technologies in Jun 2022 ([BizWest](https://bizwest.com/2022/06/23/encompass-technologies-acquires-wine-software-company-vintrace/)) | Has some EU users; no French focus found |
| **Ekos** (US) | Inventory/production/accounting for craft beverage | Quote | Raised $29M (Series A $8M 2019, Series B $21M 2021); 17,000+ users ([CB Insights](https://www.cbinsights.com/company/ekos-1/financials), [Dealroom](https://dealroom.co/companies/ekos/)) | Acquired by Next Glass in Oct 2025 | No |
| **Provi + SevenFifty** (US) | B2B ordering marketplace for distributors and on/off-premise buyers | Free for buyers; distributor-paid | $125M raised, $750M valuation; 1,200+ distributor portfolios, 700k products; ~10% of US licensed retailers ([Provi](https://provi.com/company-news/provi-and-sevenfifty-complete-integration-creating-single-best-in-class-ecommerce-marketplace-for-wholesale-buyers)) | Merged Jan 2022 ([Shanken](https://www.shankennewsdaily.com/2022/01/26/30318/provi-and-sevenfifty-announce-partnership-creating-expanded-b2b-e-commerce-player/)) | No (US three-tier specific) |
| **GreatVines / Andavi** (US) | Supplier sales execution, trade-spend CRM (on Salesforce) | Quote | PE-backed (Endeavour Capital) | Andavi bought GreatVines in 2021, then Tradeparency, Business Impact and Digitalrep in 2022 ([Madison Park](https://www.madisonparkgrp.com/transactions/andavi-solutions-acquires-greatvines/)) | No |
| **Bottlebooks** (DE) | Product-data and trade-tasting catalogues for fairs (London Wine Fair, ProWein) | 2016: £77/yr; catalogue £135 ([Drinks Int.](https://drinksint.com/news/fullstory.php/aid/6050/.html)) | 1,707 businesses and 5,015 wines in 2016 | Independent | Used by producers exhibiting at ProWein |
| **RedChirp** (US) | 2-way SMS/webchat for wineries, Tock integration | Not public | Claims $50.6M of non-club sales within 14 days of texts across 174 wineries in 2023 (attribution, not causation) ([WIA](https://wineindustryadvisor.com/2025/11/07/from-text-to-sale-elevate-your-winerys-customer-experience-with-redchirp-2/)) | — | No |
| **WineSpeak.ai** (Napa) | AI web concierge: books tastings, recommends clubs; RAG; Commerce7 integration | Not public | Deployments at Jessup, Goosecross, Valle della Pace ([PR](https://www.prnewswire.com/news-releases/valle-della-pace-and-winespeakai-announce-commerce7-integration-into-sophia-the-virtual-concierge-and-wine-curator-at-valle-della-pace-302643229.html)) | — | No |
| **The Wine Agent** | AI tourism concierge on WhatsApp, Instagram and web; books tastings | From $69/mo (marketplace listing) ([WIN](https://marketplace.wineindustrynetwork.com/listing/ai-powered-winery-concierge-delivers-24-7-hospitality-to-sell-more-wine/)) | n/a | — | Multilingual pitch; unclear |
| **vinSUITE "Ask Vinny"** (US) | AI Q&A over the winery's own sales and club data | Bundled | Launched Sept 2026 ([WIA](https://wineindustryadvisor.com/2026/09/21/vinsuite-launches-ask-vinny-bringing-ai-powered-decision-making-to-winery-teams/)) | — | No |
| **COLAClear / GoVisually** (US) | AI label pre-check against TTB rules (27 CFR 4/5/16) | Free beta (May 2026); the alternative is an attorney at $2,500+ ([WIA](https://wineindustryadvisor.com/2026/05/04/colaclear-launches-public-beta-automated-ttb-label-pre-screen/)) | Early | — | No EU/INAO equivalent found |
| **Vinte (Omega)** | AI sales agents that find importers and retailers in any market | Not public | Vendor claims only ([vinte.ai](https://www.vinte.ai/blog/ai-sales-agents-for-distributors)) | — | Unclear |
| **sommify** (EU) | AI assistant for distributor sales reps (offers, decks) | €70/seat/mo ([sommify.ai](https://sommify.ai/)) | — | — | EU-based |
| **BestWineImporters** | Database of 35k+ importers, distributors and retailers in 167 countries; AI search | Not public; sister product BestFoodImporters is $449–899 per 6 months ([plans](https://bestfoodimporters.com/plans/)) | Mixed Trustpilot reviews about stale contacts ([Trustpilot](https://www.trustpilot.com/review/bestwineimporters.com)) | — | Widely used by French exporters (E) |
| **Tastry / Preferabli** (US) | AI palate/recommendation engines | B2B licences | Tastry ≈$10–12M raised; Preferabli $24M, mostly loans ([CB Insights](https://www.cbinsights.com/company/tastry/financials)) | — | No |

**What the benchmarks prove (analysis):**
- **The pricing anchor is "% of DTC revenue."** Wineries accept tiered pricing that tracks their DTC revenue, roughly 0.5–3% all-in. A champagne grower with €200k of direct sales is used to paying about €100–400/mo for software.
- **Compliance and logistics are paid for.** Vinoshipper built a compliance-services business. Ekos and InnoVint sell traceability. Tasks that carry legal risk get budget.
- **AI products are bolt-ons sold through platform integrations** (WineSpeak to Commerce7, RedChirp to Tock). A champagne agency should likewise integrate with the French incumbents (Baqio, Vitisoft, Isavigne and others; see agent 02) rather than replace them.
- **The pure-SaaS winners took 10+ years and US-specific rules** (three-tier, state shipping). That moat does not transfer to France, but neither does the product.

---

## 3. European/French equivalents and gaps

| Name | Verified? | What it is | Relevance |
|---|---|---|---|
| **Baqio** (Dijon) | Yes | Commercial management: invoicing, DRM, e-shop, CRM, agent order-taking, stock. Champagne version "Baqio Bulles" and an allocation/primeur module ([Réussir](https://www.reussir.fr/vigne/baqio-adapte-son-logiciel-aux-vignerons-champenois)). Small team (~8, estimate) | A system of record to integrate with, not to compete with |
| **Solumatic** (Tours) – Vitisoft, Padawine, Viticode, **Vinca** | Yes | Vitisoft CRM plus "Vinca", billed as the first conversational AI for wine, launched at SIVAL 2026. Raised €1M, 23 staff ([SIVAL](https://online.sival-angers.com/event/sival-2026/product/UHJvZHVjdF8xNDA0NzA4), [Business Cool](https://business-cool.com/entreprendre/levee-fonds/solumatic-levee-de-fonds/)) | Shows incumbents are adding AI Q&A themselves |
| **SOWINE** (Paris/Bordeaux) | Yes | Marketing and communication agency for wine, champagne and spirits since 2006. Clients include Bollinger, G.H. Mumm and Philipponnat. Runs an Academy covering the Loi Évin and CRM ([CB News](https://www.cbnews.fr/node/40966)). No AI offer found | Potential partner or channel; proves maisons buy agency services |
| **Winalist** (Aÿ, Champagne) | Yes | Wine-tourism booking marketplace with 1,700+ partners in 10 countries; raised €1M in Jun 2025 ([Techleap](https://finder.techleap.nl/news/feed/winalist-secures-1m-for-global-expansion)) | Covers tasting-room booking; an AI-concierge competitor or partner |
| **Vinexposium Connect** | Yes (historic) | B2B matchmaking for Wine Paris: 19,350 meeting requests and 3,068 meetings in 2022 ([Vinexposium PR](https://www.vinexposium.com/wp-content/uploads/2022/02/CP_WINE-PARIS-VINEXPO-PARIS_2022_BILAN_FR.pdf)) | Importer-discovery channel tied to the fair |
| **Lucien** (Bourgogne/Chablis) | Partly (search summary) | AI agent that helps fill DSA documents and aid applications ([search via bonjouria/vitisphere](https://www.vitisphere.com/actualite-106400-une-intelligence-artificielle-developpee-sur-mesure-pour-la-filiere-vin.html)) | Evidence of demand for AI on excise and admin paperwork |
| **Vitivisio** | Yes | Sensors plus AI for vine health (Loire, Cognac, Bordeaux, Champagne) ([Sommeliers Int.](https://www.sommeliers-international.com/fr/focus/vitivisio-la-viticulture-intelligente)) | Vineyard side, out of scope |
| **AG2C** (Champagne accounting centre) | Yes | Digitising accounting flows; uses AI for cash forecasting ([La Champagne Viticole](https://lachampagneviticole.fr/lag2c-sous-le-signe-de-ladaptation-et-de-laccompagnement/)) | Trusted local intermediary and possible channel |
| Oenoview, WineFunding, "VinoTrade", "Wine Connect", "Œnocréatif" (Vignerons Indépendants) | **Not verified** | Searches returned nothing usable. "Wine Connect" appeared only as an AD'OCC Occitanie project ([PDF](https://www.agence-adocc.com/wp-content/uploads/2024/04/COMMUNIQUe_WineConnect.pdf)) | Do not cite without checking |

**Gaps: models with no French/Champagne equivalent found**
1. **Done-for-you AI and automation agency for wine estates.** None found. The closest are SOWINE (marketing, no AI) and generic n8n agencies (no wine knowledge).
2. **Two-way SMS/WhatsApp clienteling for private clients** like RedChirp. None found.
3. **AI importer prospecting tied to the export calendar** (Wine Paris, ProWein, Vinexpo Asia). Only generic databases exist.
4. **Compliance-as-a-service in the Vinoshipper style** for EU distance selling: excise representatives, e-DA/DSA, per-country labelling. Fragmented among freight forwarders. Agent 03 covers the detail.
5. **AI label pre-check** (COLAClear-style) for INAO/CIVC/EU labelling rules plus export rules (TTB COLA). None found.
6. **AI concierge for maisons' visitor and private-client enquiries.** Winalist handles booking but is not a brand-voice concierge.

---

## 4. Agency economics (France/EU, 2025–2026)

**Tool costs (F):** n8n Cloud Starter costs €20–24/mo and Pro €50–60/mo. A self-hosted instance costs €5–20/mo for the server, or ~$130–230/mo once maintenance labour is counted ([coworker.ai](https://coworker.ai/blog/n8n-pricing), [ExpressTech](https://expresstech.io/the-real-cost-of-self-hosting-n8n-in-2026/)). Make moved to credits on 27 Aug 2025: Core ~$9–16/mo, Pro ~$28 ([Lindy](https://www.lindy.ai/blog/make-com-pricing)). AI API costs run €20–100/mo for occasional use and €50–500/mo for autonomous agents ([autom-ia.com](https://autom-ia.com/blog/combien-coute-automatisation-ia-tpe-pme-2026/)).

**French agency price points (F, mostly from agency marketing pages):**

| Item | Range | Source |
|---|---|---|
| Monthly retainer, n8n agency for SMEs (build plus maintenance, no per-task billing) | €300–900 HT/mo | [inno-mation.com](https://inno-mation.com/agence-n8n) |
| Self-hosted n8n installation | from €1,300 HT, plus €20–120/mo infrastructure | [genee.tech](https://www.genee.tech/agence-n8n) |
| Simple workflow: freelancer / confirmed n8n freelancer / established French agency | €800–2,000 / €1,500–3,500 / €5,000–15,000 | [brand-advocacy.fr](https://brand-advocacy.fr/n8n-automatisation-pme-francaises-2026) |
| Custom AI system setup | €4,000–6,000, plus €50–100/mo recurring | [automatisation-intelligence-artificielle.fr](https://www.automatisation-intelligence-artificielle.fr/cout-automatisation-ia-entreprise/) |
| US benchmark: wine AI concierge SaaS | from $69/mo | WIN marketplace |
| US benchmark: wine-label attorney | $2,500+ retainer | COLAClear PR |

**Specialised agencies:** I found none in France that does AI automation for wine and spirits, luxury or agri-food. SOWINE does marketing. Several Colmar and Bordeaux web agencies do websites for wineries ([example](https://www.annecyfrenchtech.com/votre-agence-web-colmar-experte-en-marketing-digital-pour-le-secteur-viticole/)). US wine-specific lead-gen and marketing shops exist (Next Gen Wine Marketing, thecorner.ai, Vinagency).

**IT spend benchmarks:** I found no published "% of revenue" figure for wine estates. Ekos surveys show 45% of US wineries grade their own tech adoption C or lower ([Ekos](https://www.goekos.com/blog/45-of-wineries-grade-themselves-a-c-or-lower-on-technology-adoption/)). The best proxy is the DTC platform tiers above.

**What a champagne customer would bear (E):**

| Segment | Revenue | Current software spend (E) | Plausible agency ticket |
|---|---|---|---|
| Small grower (RM), mostly private clients plus cellar door | €300k–1M | €1–3k/yr (Baqio-type ERP, website, Mailchimp) | Setup €1.5–4k; retainer €250–500/mo (≈1–2% of revenue all-in). Needs a "productized pack" sold in winter (Jan–Mar) |
| Established grower / export grower | €1–3M | €3–10k/yr | Setup €4–10k; €500–1,200/mo |
| Mid maison / commercialising coop | €5–50M | €30–250k/yr IT (ERP, CRM, e-com, agencies) | Projects €15–60k; retainer €2–6k/mo; possibly "AI employee" seats at €300–800/mo each |

The NextAutomation framing (AI employees at $99–799/mo set against a $60k assistant) translates well. A French *assistant(e) commercial(e) export* costs roughly €40–55k/yr loaded **(E)**. A €500/mo "AI export assistant" is about 12–15% of that cost.

---

## 5. RE playbook → champagne translation

| NextAutomation RE play | Champagne translation | Evidence it works in wine | Legal / feasibility check | Verdict |
|---|---|---|---|---|
| **Speed-to-lead voice AI** (calls a new lead within 60s) | **Inbound** voice/WhatsApp agent for Q4 private-client orders, visit bookings and importer enquiries in FR/EN/DE/JA, with order capture into Baqio/ERP | RedChirp: 92% of texted customers reply within 5 min; webchats convert (vendor) ([WIA](https://wineindustryadvisor.com/2023/01/13/redchirps-complete-texting-platform-for-wineries)). WineSpeak concierges book tastings | **Outbound B2C calls without opt-in are banned since 11 Aug 2026** (loi 2025-594, art. L223-1; fines up to €375k) ([LegalPlace](https://www.legalplace.fr/actualites/demarchage-telephonique/)). AI Act Art. 50 requires an "I'm an AI" disclosure ([Cooley](https://www.cooley.com/news/insight/2026/2026-08-03-eu-ai-act-transparency-obligations-take-effect-2-august-2026)). Inbound only | **Adapt: inbound only.** Highest Q4 value for growers whose phones ring during harvest and in December |
| **Lead-gen scrapers** (Google Maps, Secretary of State) | Scrape and enrich importers, cavistes, Michelin/hotel lists, corporate-gift buyers and duty-free; score by fit; push to CRM | BestWineImporters (35k contacts, data quality complaints); Vinte; Vinexposium matchmaking volumes show demand | B2B email allowed on an opt-out basis if relevant to the recipient's job, with a professional nominative address ([CNIL rules via donneespersonnelles.fr](https://www.donneespersonnelles.fr/prospection-commerciale-rgpd)). Respect scraping ToS | **Strong.** Export is growers' biggest growth lever. Sell as "export pipeline as a service" around Wine Paris (Feb) and ProWein (Mar) |
| **AI follow-up / nurture** | Reorder campaigns to private-client lists (Christmas, Father's Day, weddings), club allocations, abandoned basket, card-declined outreach | RedChirp's $50.6M attributed sales; wine clubs shifting to SMS ([Wine Intelligence](https://wine-intelligence.com/blogs/wine-news-insights-wine-intelligence-trends-data-reports/ai-sms-smart-tech-how-wine-clubs-are-reinventing-direct-to-consumer-strategy)) | B2C needs opt-in, or the "existing customer, similar products" exception. CNIL (Jun 2026) says account creation alone is not a customer relationship. Content must stay Loi Évin-compliant (objective info, health warning) | **Strong.** Clear ROI, easy to measure |
| **Content pipeline** | Multilingual newsletter, Instagram, tech sheets, export-market translations from one source of truth | Many US vendors (BottleShots.ai etc.); FR incumbents are adding AI writing | **Loi Évin constraint (see §6).** Must be "information" (terroir, method, cuvée facts), no lifestyle or festive framing, health warning on ads, no influencer-style promotion | **Medium.** Sell as a "Loi Évin-safe" content engine, which is a differentiator |
| **Transaction coordinator** | **Order-to-shipment coordinator:** order → invoice → DAE/e-DA or DSA → carrier booking → tracking → customer update → DRM entry | Lucien (AI for DSA forms) shows demand; Vinoshipper built a compliance business | Excise liability stays with the entrepositaire agréé; AI prepares, a human validates | **Strong for maisons and export growers.** Sticky back-office work, low legal exposure if a human stays in the loop |
| **Custom CRM** | CRM unifying private clients, importers and agents, on top of Baqio/Vitisoft or HubSpot | Commerce7 and others prove CRM plus club is core | GDPR records and consent logging | **Medium.** Integrate with incumbents, don't rebuild |
| **"AI Employees" SaaS** | "Assistant export IA", "Assistant caveau IA", "Assistant admin douane IA" at €200–800/mo | US analogues at $69/mo+ | — | **Phase 2** once workflows are proven in 10–20 accounts |
| **Paid community (Skool)** | Community/training "IA pour vignerons", possibly with SGV, Vignerons Indépendants or a lycée viticole | SOWINE Academy proves paid training demand (≈30 one-day workshops) | — | **Good acquisition channel.** The audience is conservative and peer-driven |

---

## 6. Loi Évin: what it allows and forbids online

**Framework (F).** The Loi Évin of 10 Jan 1991 (Code de la santé publique, art. L3323-2 et seq.) is a **"permitted unless listed" regime**: anything not expressly authorised is forbidden ([Réussir](https://www.reussir.fr/vigne/communication-etre-en-conformite-avec-les-exigences-de-la-loi-evin)).

**Allowed media.** Internet advertising has been allowed since 2009, with three exceptions ([Réussir](https://www.reussir.fr/vigne/communication-etre-en-conformite-avec-les-exigences-de-la-loi-evin)):
- sites aimed mainly at young people (an audience with ~30% or more minors);
- sports association sites;
- intrusive or interstitial formats (pop-ups).

**Allowed content (L3323-4)** **[from general knowledge — verify exact wording]**. Advertising must be limited to objective, informative elements:
- alcohol degree;
- origin, appellation and composition;
- production method;
- name and address of the producer;
- sales terms and how to consume the product;
- objective references to terroir, distinctions and awards.

Every advertisement must carry the health warning "L'abus d'alcool est dangereux pour la santé, à consommer avec modération". Associations with festivity, success, seduction, sport or social performance are excluded.

**2016 terroir carve-out (F).** Article L3323-3-1 was created by loi 2016-41. It says that content about a production region, a geographical indication, a terroir, a wine route, know-how, history, or cultural, gastronomic or landscape heritage of a quality or origin-identified beverage is **not** advertising. The article was designed for wine tourism ([CMS](https://cms.law/en/fra/legal-updates/loi-evin-vers-un-requilibrage-entre-publicite-et-information-en-matiere-de-boissons-alcooliques), [ARPP](https://www.arpp.org/wp-content/uploads/2016/12/120216-CR-Réunion-ARPP-sur-la-Loi-santé.pdf)).

**Influencers and social media (F):**
- The influencer law of June 2023 confirmed that influencers are subject to the Loi Évin. A specific alcohol ban was dropped from that law ([Fréquence Médicale](https://www.frequencemedicale.com/generaliste/actualites/9939-Alcool-interdire-sa-promotion-aupres-des-mineurs-par-les-influenceurs)).
- On 4 Mar 2024 the Paris criminal court sanctioned posts by influencer Anna Rvr and producer Gérard Bertrand promoting a rosé. The producer received a €20,000 suspended fine (amount as reported by [Addictions France](https://addictions-france.org/datafolder/uploads/2024/07/Communique-de-presse-Anna-rvr.pdf)) **[verify judgment details]**.
- In 2023 Meta was ordered to remove content ([Syndicat Côtes-du-Rhône](https://syndicat-cotesdurhone.com/article/influenceurs-et-vin-attention-aux-risques)).
- Addictions France actively monitors and sues. Its Dec 2025 report found ephemeral stories made up about 70% of alcohol posts in 2023 ([report](https://addictions-france.org/datafolder/uploads/2025/12/Rapport-Alcool-et-reseaux-sociaux-2025_web.pdf)).
- Bills to ban alcohol advertising on social networks have been tabled ([AN l17b0588](https://www.assemblee-nationale.fr/dyn/17/textes/l17b0588_proposition-loi.pdf)) but were not adopted as of my sources.

**Concrete rules for an agency's deliverables (analysis, not legal advice):**

| Deliverable | Allowed | Forbidden or risky |
|---|---|---|
| Website / e-shop | Product facts, terroir, method, awards, prices, delivery terms, age gate, health warning on promotional pages | Pop-ups; imagery of parties or "success" |
| Newsletter (opt-in B2C) | New cuvée tech facts, harvest report, vintage notes, cellar-door hours, objective offers, health warning | "Celebrate like a winner", lifestyle framing, targeting under-18s |
| Instagram (own account) | Vineyard, harvest, know-how and heritage content (L3323-3-1); bottle with facts plus health warning on promotional posts | Young people drinking, festive or sexy framing, paid influencer reposts, contests that push consumption |
| Influencers | Very high risk in France. Even "gifted" posts can count as indirect advertising | Paid or gifted influencer campaigns aimed at France |
| Export markets | Local rules apply (TTB in the US; UK Portman Group). France-wide rules apply if the content targets France | — |
| AI-generated content | Must pass the same checks. The AI Act requires labelling of deepfake/synthetic media | AI "lifestyle" images of people drinking champagne |

**Product implication:** build a **"Loi Évin guardrail"** into the content pipeline. That means a rules-based plus LLM checker that strips non-permitted themes and inserts the health warning. This is a credible differentiator against generic agencies and against US tools.

---

## 7. Other risks

- **GDPR / ePrivacy (F).** B2C email and SMS require opt-in, or the existing-customer "similar products" exception. Pre-ticked boxes are invalid. B2B outreach is opt-out if it relates to the recipient's job. CNIL guidance of Jun 2026 says account creation alone is not a customer relationship ([Seban](https://www.seban-associes.avocat.fr/prospection-commerciale-communications-transactionnelles-et-relationnelles-la-commission-nationale-de-linformatique-et-des-libertes-cnil-clarifie-les-regimes-applicables-aux-communications-elec/)). Bought lists are risky. CNIL sanctions rose sharply in 2024 ([CB News](https://www.cbnews.fr/digital/les-sanctions-cnil-forte-hausse-2024)).
- **Cold-calling ban (F).** B2C telephone canvassing has required prior consent since 11 Aug 2026, consent lasts at most 1 year, the existing-customer exception remains, and fines reach €375k ([LegalPlace](https://www.legalplace.fr/actualites/demarchage-telephonique/)). Whether the regime applies to B2B calls was **not confirmed** in my sources. This kills NextAutomation-style outbound AI calling to French consumers.
- **EU AI Act Art. 50 (F).** Since 2 Aug 2026, chat and voice agents must disclose they are AI at first interaction. Synthetic media must be labelled. Fines reach €15M or 3% of turnover ([Cooley](https://www.cooley.com/news/insight/2026/2026-08-03-eu-ai-act-transparency-obligations-take-effect-2-august-2026), [CSA note](https://labs.cloudsecurityalliance.org/wp-content/uploads/2026/07/CSA_research_note_eu_ai_act_article_50_transparency_20260729-csa-styled-1.pdf)).
- **Excise liability (analysis).** DAE/DSA and DRM errors fall on the entrepositaire agréé (the producer). The agency needs human-in-the-loop validation, contractual limits of liability and professional indemnity insurance. It should position itself as "preparation and reminders", never as declarant.
- **Sector conservatism (F/E).** Many US wineries grade their own tech low ([Ekos](https://www.goekos.com/blog/45-of-wineries-grade-themselves-a-c-or-lower-on-technology-adoption/)), and French growers are often older and use peer networks. Selling through trusted intermediaries works better: AG2C-type accounting centres, SGV, Vignerons Indépendants, Baqio/Vitisoft partner programmes, SOWINE.
- **Seasonality and cash (E).** Harvest (late Aug–Sept) and Q4 peaks absorb all attention. Sell in Jan–Apr (after the holidays, around Wine Paris and ProWein) and go live before September. Q4 is when value is demonstrated. Bill monthly with annual commitments.
- **Market headwind (F).** Champagne shipped 271.4M bottles in 2024, down 9.2% ([wein.plus](https://magazine.wein.plus/news/comite-champagne-9-2-percent-decrease-in-sales-in-2024-significant-decline-due-to-inflation-and-economic-crisis)). That squeezes budgets but strengthens the case for tools that drive DTC and export growth.
- **Platform risk.** Incumbents are adding AI themselves (Solumatic's Vinca, vinSUITE's Ask Vinny). The agency's value must sit in cross-system workflows and service, not single features.

---

## 8. Market sizing (France-first)

**Customer counts (F, with source dates):**

| Region | Bottle-selling operators | Source |
|---|---|---|
| Champagne | ~4,400 vignerons selling champagne (of 15,800); ~42 commercialising coops (of 135); 360–380 maisons. Tasting Panel: <5,000 RM | [SGV guide 2018](https://www.yumpu.com/fr/document/view/61678810/les-guides-du-sgv-bonnes-pratiques-vendange-2018); [DGCCRF](https://www.economie.gouv.fr/dgccrf/champagne-les-principaux-enseignements-des-enquetes-conduites-en-2020-et-2021) |
| Bourgogne | 3,500+ domaines, of which 863 sell >10,000 bottles/yr; 266 maisons | BIVB via [b2match](https://www.b2match.com/e/agronov-sol-et-biosolutions-2024/participations/428353) |
| Bordeaux | 4,600–5,300 AOC growers; ~300 négociants. RA 2010: 3,600 Aquitaine vinifiers use short circuits | [Journal des Entreprises](https://www.lejournaldesentreprises.com/breve/allan-sichel-redevient-president-du-civb-2041637); [DRAAF NA](https://draaf.nouvelle-aquitaine.agriculture.gouv.fr/IMG/pdf/Regards_circuits_courts_vin_24_25_cle881546.pdf) |
| Loire | ~2,200 domaines, 310 négociants, 16 coops | [InterLoire 2024](https://vinsdeloire.fr/sites/interloire/files/2024-09/interloire_cp-infographie_juin-2024.pdf) |
| Alsace | ~4,000 growers, 850 bottlers | [LSA](https://www.lsa-conso.fr/les-vins-d-alsace-a-l-affiche,353769) |
| Cognac | 4,413 growers/bouilleurs; 265 houses (most growers sell eaux-de-vie to houses) | [Portail IE / BNIC 2023](https://portail-ie.fr/wp-content/uploads/2024/06/60-Vins__Spiritueux-Fiche_Identite_Cognac-V2.pdf) |
| France total | 560 coops; ~700 négoce houses | [FranceAgriMer 2026](https://www.franceagrimer.fr/sites/default/files/2026-02/08_FICHE_FILIERE_VIN_2026.pdf) |

**Sizing (E: my assumptions are stated):**

- **Champagne SAM.**
  - About 1,500 of the ~4,400 selling growers have enough volume and openness to pay. I assume roughly 1/3: those with >€500k revenue, an export or e-commerce ambition, and a next-generation manager. At €6k/yr average (€3k setup amortised plus €350/mo), that is about €9M.
  - About 150 mid maisons and commercialising coops (out of ~420) at €30k/yr is about €4.5M.
  - **Champagne SAM ≈ €13–14M/yr.**
- **France wine and spirits TAM.**
  - Bottle-selling operators in the six regions: roughly 4,400 + 3,500 + 3,600 + 2,200 + 850 + ~500 Cognac bottlers + ~1,500 négoce/coops ≈ 16,500. Rhône, Languedoc, Provence and the South-West would add many thousands more; they are excluded here.
  - At a blended €4–5k/yr, that is **≈ €65–85M/yr**.
- **SOM (3 years, one agency of 3–5 people).** 60–100 growers at €6k plus 8–15 maisons at €30k comes to **≈ €0.6–1.05M ARR**. That is consistent with a NextAutomation-scale productized agency. A SaaS layer ("AI employees") could extend the reach to 500+ accounts at €200–400/mo, about €1.2–2.4M ARR, but only after the workflows are proven.

**Benchmark sanity check:** Commerce7 took about 8 years to reach 3,500 wineries worldwide, and InnoVint reached about $3M of revenue bootstrapped. In the wine niche, even the winners are mid-sized businesses. Plan the champagne play as a profitable services business with productized add-ons, not a venture-scale SaaS, unless it expands to all French wine regions plus the EU.

---

## 9. Implications for the champagne play

1. **Lead offers, ranked:**
   1. Export pipeline (importer scraping, enrichment and B2B sequences);
   2. Private-client reorder engine (opt-in email/SMS/WhatsApp with Loi Évin guardrails);
   3. Inbound multilingual AI concierge (voice, WhatsApp, web) with AI disclosure;
   4. Order-to-shipment and excise-paperwork coordinator.
2. **Avoid outbound B2C voice AI** (cold-calling ban) and influencer content.
3. **Price** setups at €2–10k, retainers at €300–1,200/mo for growers and €2–6k/mo for maisons. Anchor against the cost of a hire and against DTC-platform tiers.
4. **Integrate, don't replace:** Baqio, Vitisoft, Isavigne, Shopify/WooCommerce, Sendcloud and others.
5. **Distribute through trusted channels:** SGV, Vignerons Indépendants, AG2C/CER accounting centres, SOWINE, Baqio partners, plus a paid "IA pour vignerons" community.
6. **Sell in Jan–Apr and prove value in Q4.**

---

## Sources (selected, all cited inline above)

- Commerce7 pricing: https://salessite-v3.commerce7.com/pricing/ ; https://commerce7.com/pricing
- WineDirect–Fullsteam: https://hl.com/about-us/transactions/winedirect-fullsteam/ ; https://wineindustryadvisor.com/2025/01/16/afternoon-brief-2783/
- eCellar: https://us.fitgap.com/products/035033/ecellar
- Vinoshipper: https://www.vinoshipper.com/pricing ; https://wineindustryadvisor.com/2024/11/12/the-us-wine-industry-welcomes-third-major-compliance-partner/
- InnoVint: https://getlatka.com/companies/innovint
- vintrace/Encompass: https://bizwest.com/2022/06/23/encompass-technologies-acquires-wine-software-company-vintrace/
- Ekos: https://www.cbinsights.com/company/ekos-1/financials ; https://dealroom.co/companies/ekos/
- Provi/SevenFifty: https://provi.com/company-news/provi-and-sevenfifty-complete-integration-creating-single-best-in-class-ecommerce-marketplace-for-wholesale-buyers ; https://www.shankennewsdaily.com/2022/01/26/30318/provi-and-sevenfifty-announce-partnership-creating-expanded-b2b-e-commerce-player/
- Andavi/GreatVines: https://www.madisonparkgrp.com/transactions/andavi-solutions-acquires-greatvines/
- Bottlebooks: https://drinksint.com/news/fullstory.php/aid/6050/.html
- RedChirp: https://wineindustryadvisor.com/2025/11/07/from-text-to-sale-elevate-your-winerys-customer-experience-with-redchirp-2/ ; https://wineindustryadvisor.com/2024/07/15/redchirp-and-tock-partner-to-improve-reservation-communications/
- WineSpeak.ai: https://www.prnewswire.com/news-releases/valle-della-pace-and-winespeakai-announce-commerce7-integration-into-sophia-the-virtual-concierge-and-wine-curator-at-valle-della-pace-302643229.html
- The Wine Agent listing: https://marketplace.wineindustrynetwork.com/listing/ai-powered-winery-concierge-delivers-24-7-hospitality-to-sell-more-wine/
- vinSUITE Ask Vinny: https://wineindustryadvisor.com/2026/09/21/vinsuite-launches-ask-vinny-bringing-ai-powered-decision-making-to-winery-teams/
- COLAClear: https://wineindustryadvisor.com/2026/05/04/colaclear-launches-public-beta-automated-ttb-label-pre-screen/
- Vinte: https://www.vinte.ai/blog/ai-sales-agents-for-distributors ; sommify: https://sommify.ai/ ; BestWineImporters: https://www.bestwineimporters.com/
- Tastry/Preferabli: https://www.cbinsights.com/company/tastry/financials
- Baqio: https://www.reussir.fr/vigne/baqio-adapte-son-logiciel-aux-vignerons-champenois
- Solumatic/Vinca: https://online.sival-angers.com/event/sival-2026/product/UHJvZHVjdF8xNDA0NzA4 ; https://business-cool.com/entreprendre/levee-fonds/solumatic-levee-de-fonds/
- SOWINE: https://www.cbnews.fr/node/40966
- Winalist: https://finder.techleap.nl/news/feed/winalist-secures-1m-for-global-expansion
- Vinexposium Connect: https://www.vinexposium.com/wp-content/uploads/2022/02/CP_WINE-PARIS-VINEXPO-PARIS_2022_BILAN_FR.pdf
- AG2C: https://lachampagneviticole.fr/lag2c-sous-le-signe-de-ladaptation-et-de-laccompagnement/
- Agency pricing: https://inno-mation.com/agence-n8n ; https://www.genee.tech/agence-n8n ; https://brand-advocacy.fr/n8n-automatisation-pme-francaises-2026 ; https://www.automatisation-intelligence-artificielle.fr/cout-automatisation-ia-entreprise/ ; https://autom-ia.com/blog/combien-coute-automatisation-ia-tpe-pme-2026/
- n8n/Make: https://coworker.ai/blog/n8n-pricing ; https://www.lindy.ai/blog/make-com-pricing
- Ekos tech adoption: https://www.goekos.com/blog/45-of-wineries-grade-themselves-a-c-or-lower-on-technology-adoption/
- Loi Évin: https://www.reussir.fr/vigne/communication-etre-en-conformite-avec-les-exigences-de-la-loi-evin ; https://cms.law/en/fra/legal-updates/loi-evin-vers-un-requilibrage-entre-publicite-et-information-en-matiere-de-boissons-alcooliques ; https://syndicat-cotesdurhone.com/article/influenceurs-et-vin-attention-aux-risques ; https://addictions-france.org/datafolder/uploads/2024/07/Communique-de-presse-Anna-rvr.pdf ; https://addictions-france.org/datafolder/uploads/2025/12/Rapport-Alcool-et-reseaux-sociaux-2025_web.pdf ; https://www.frequencemedicale.com/generaliste/actualites/9939-Alcool-interdire-sa-promotion-aupres-des-mineurs-par-les-influenceurs
- Cold calling: https://www.legalplace.fr/actualites/demarchage-telephonique/
- GDPR prospection: https://www.donneespersonnelles.fr/prospection-commerciale-rgpd ; https://www.seban-associes.avocat.fr/prospection-commerciale-communications-transactionnelles-et-relationnelles-la-commission-nationale-de-linformatique-et-des-libertes-cnil-clarifie-les-regimes-applicables-aux-communications-elec/
- AI Act: https://www.cooley.com/news/insight/2026/2026-08-03-eu-ai-act-transparency-obligations-take-effect-2-august-2026
- Counts: https://www.yumpu.com/fr/document/view/61678810/les-guides-du-sgv-bonnes-pratiques-vendange-2018 ; https://www.economie.gouv.fr/dgccrf/champagne-les-principaux-enseignements-des-enquetes-conduites-en-2020-et-2021 ; https://vinsdeloire.fr/sites/interloire/files/2024-09/interloire_cp-infographie_juin-2024.pdf ; https://www.lejournaldesentreprises.com/breve/allan-sichel-redevient-president-du-civb-2041637 ; https://www.lsa-conso.fr/les-vins-d-alsace-a-l-affiche,353769 ; https://portail-ie.fr/wp-content/uploads/2024/06/60-Vins__Spiritueux-Fiche_Identite_Cognac-V2.pdf ; https://www.franceagrimer.fr/sites/default/files/2026-02/08_FICHE_FILIERE_VIN_2026.pdf ; https://magazine.wein.plus/news/comite-champagne-9-2-percent-decrease-in-sales-in-2024-significant-decline-due-to-inflation-and-economic-crisis
