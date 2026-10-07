# Champagne automation research: handoff

*Last updated 2026-10-07. Written for whoever restarts this locally (you, or a local Claude session).*

## The task (from the user)

Understand how NextAutomation works (an AI automation agency for real estate). Then apply that model to the **champagne industry**, focusing on how transactions are done:
- which CRMs are used and how automated they are;
- transporters' websites: are orders still placed by hand?
- where AI could make the processes smoother.

End with a recommendation for a small business that automates this sector. The main Claude coordinates; sub-agents do the parallel research.

## Why restart locally

The cloud session had two hard limits that weakened the research:
1. **Websites could not be opened.** The cloud environment's network policy returned 403 on almost every site (champagne.fr, hillebrandgori.com, baqio.com, vitisphere.com, grower sites…). Agents only saw **search-result snippets**, never full pages.
2. **Shared search budget.** All agents together got about 200 web searches per turn, and that ran out partway through every report.

A local session with normal internet access can open the pages and check the points marked unverified.

## Where things stand

| Step | Status |
|---|---|
| Read NextAutomation context (from GitHub repos `arsnnnn05/nextautomation-pipeline-scraping-bot` and `LucasNextAutomation/na-video-studio`; the local folders were not reachable from the cloud) | Done: `agent-reports/00-nextautomation-model.md` |
| Agent 1: market structure and transaction chain (grapes, brokers, B2B, DTC, paperwork) | Done: `agent-reports/01-market-and-transactions.md` |
| Agent 2: software / CRM / ERP landscape | Done: `agent-reports/02-software-crm-landscape.md` |
| Agent 3: logistics, transporters, how shipments are booked, excise documents | Done: `agent-reports/03-logistics-transport.md` |
| Agent 4: 25-grower website sample, sales channels, digital maturity, competitors, go-to-market | Done: `agent-reports/04-sales-digital-maturity-competitors.md` |
| Agent 5: international wine-tech benchmarks, agency pricing, Loi Évin, sizing | Done: `agent-reports/05-benchmarks-business-model.md` |
| Final synthesis doc ("Champagne Automation Opportunity", a Claude Doc at https://claude.ai/code/artifact/fd45b864-6f95-459b-b8bb-55244feeb95f) | **Sections 1–6 written; sections 7–12 not written** (see below) |

Doc sections already written: 1 NextAutomation model, 2 how champagne is traded, 3 software/CRMs, 4 transport, 5 manual steps ranked, 6 competitors.

Doc sections still to write (pending placeholders in the doc), with the content already decided:

**7. What I would build.** Offers in priority order:
1. **Order and back-office desk.** Order emails, PDF order forms and e-shop orders are read automatically into the wine ERP (Baqio, Vitisoft, Isagri, Wineriz). Then the pipeline produces an invoice and payment link, calculates shipping, generates the GAMMA 2 XML for the DAE/DSA (GAMMA accepts XML import, so no customs API is needed), books the carrier (by API, or a pre-filled email to regional hauliers) and sends tracking.
2. **Private-client reactivation engine.** Clean and segment the client file. Run opt-in email/SMS Q4 campaigns, reorder reminders and win-back for lapsed clients, all Loi Évin-checked.
3. **Export pipeline as a service.** Scrape and enrich importer, caviste, restaurant and corporate-gift buyer lists, then run B2B sequences in EN/DE/JA timed to Wine Paris (Feb) and ProWein (Mar).
4. **Inbound multilingual AI concierge.** Voice, WhatsApp and web assistant for Q4 orders, visit bookings and importer questions. It must disclose that it is an AI (EU AI Act).
5. Later: an "AI employees" productization (for example an export assistant, a cellar-door assistant, a customs-admin assistant) at €200–800/mo; a paid community "IA pour vignerons"; a broker back-office tool for the ~40 grape brokers (contracts, confirmations, invoices, payment splits).

How the real-estate playbook translates:
- speed-to-lead voice AI → **inbound only**;
- lead-gen scrapers → importer scraping (the strongest fit);
- transaction coordinator → order-to-shipment coordinator;
- content machine → Loi Évin-safe content engine.

Pricing:
- **Growers:** €1.5–5k setup plus €150–500/mo. Export growers: €4–10k plus €500–1,200/mo.
- **Mid-size houses:** €15–60k projects plus €2–6k/mo.
- **Anchor:** a seasonal admin hire (~€40–55k/yr loaded), or the margin on 300–500 extra bottles.

**8. Market size (estimates):**
- **Champagne:** ~4,100 operators sell their own bottles. About 1,500 serious growers at ~€6k/yr plus ~150 mid houses and co-ops at ~€30k/yr gives a champagne market of **≈ €13–14M/yr**.
- **France, six wine regions:** ≈ €65–85M/yr.
- **Realistic for one 3–5-person agency in 3 years:** €0.6–1M recurring revenue. This is a profitable productized-services business, not venture-scale SaaS, unless it expands to all French regions.

**9. Risks and legal limits:**
- **Loi Évin:** content allowed only if it is objective information or terroir/heritage, plus the health warning. No lifestyle or festive framing. Influencer campaigns are very risky (the 2024 Bertrand ruling).
- **Cold calls:** B2C cold calls need opt-in since 11 Aug 2026 (fines up to €375k).
- **EU AI Act Art. 50:** AI disclosure required since 2 Aug 2026.
- **Excise:** liability stays with the producer, so a human always validates documents.
- **GDPR:** B2C mailing requires opt-in.
- **The sector:** conservative, with lack of time as the top barrier.
- **Incumbents:** adding AI themselves (Vitisoft's Vinca, Vrille).
- **Seasonality:** the harvest (mid-Aug to Sept) and Q4 are untouchable.

**10. Go-to-market and first 12 months:**
- **Jan–Jun:** pilots with 5–10 next-generation growers (found on Instagram, the Champagne de Vignerons map and salon exhibitor lists). Fixed-price "order form → online orders + CRM + reactivation" pilot.
- **Partners:** Shop&Champ', eChampagne/Enovanet, local web agencies, the ERP vendors, accounting centres (AG2C, Cerfrance), SGV/CSGV and co-ops (one co-op deal reaches hundreds of growers).
- **Content:** a "Champagne grower digital barometer" built by scraping ~1,000 grower sites, pitched to La Champagne Viticole and Vitisphere.
- **Hooks:** the 2026–27 e-invoicing mandate; the export pivot (US tariffs at 15%); cavistes moving to grower champagnes.
- **Timing:** go live before August, prove value in Q4, publish case studies in January.

**11. Open questions:** see "What to verify next" below.

**12. Sources:** collect them from the source lists at the end of each agent report.

## What to verify next (needs real web access)

1. **Transporter booking flows.** Actually open the regional hauliers' sites (Transports Lebrun, LTD Reims, Viticolis, Transfret Champagne, Mazet) and record how an order is placed: phone, form or portal. This was the user's explicit question and is still inferred, not seen.
2. **Haulier list.** Scrape SIRENE/Pappers for transport companies (NAF 49.41, 52.29) in départements 51 and 10 to build the full list (it doubles as a lead list).
3. **Grower e-shop platforms.** Scrape ~200–1,000 grower sites (from the champagnedevignerons.fr map) to measure order form vs e-shop vs platform properly. The current figure (~70% offline) comes from a biased 25-site sample.
4. **APIs.** Check the API/integration docs of Baqio, Wineriz, Vitisoft and Isavigne, and the GAMMA 2 DTI+ XML schema.
5. **Legal.** The exact Loi Évin L3323-4 wording; details of the 2024 Bertrand ruling; whether the cold-call opt-in applies to B2B.
6. **Numbers.** Current CIVC contribution rates; brokers' commission %; grape payment schedule; the Vin & Société digital barometer 2026 edition; admin hours per estate.
7. **Unverified names.** Do not cite these: Siwine, Inovin, Logivitis, Transports Jacquemin/Gaudillat/TSE, WineFunding, VinoTrade. Infologic's Pol Roger client claim and the "Section 122" 10% US wine tariff also still need checking.
8. **Customer interviews.** Talk to 5–10 growers, 1–2 brokers and 1 regional haulier to confirm pain points and willingness to pay.

## How to restart locally

1. `git pull` this branch (`claude/adoring-pasteur-6imnh7` in `arsnnnn05/personal-work`) and open `champagne-research/`.
2. Start Claude Code in the repo and say something like:
   > Read champagne-research/HANDOFF.md and the agent reports. Run the "What to verify next" items with parallel research agents (they can open web pages now). Then finish sections 7–12 of the synthesis and update any figures the verification changes.
3. Reuse the agent split if re-running: (1) market/transactions, (2) software/CRM, (3) logistics/transport, (4) grower sample/competitors/GTM, (5) benchmarks/legal/sizing. The briefs for each are summarized in the first lines of every report.
4. Point the local session at your own NextAutomation folders too. The cloud session only saw the two GitHub repos, so local docs may add context (case studies, proposals, client list).

## Side note found during research

`docs/Stratégie de développement communautaire.docx` in `nextautomation-pipeline-scraping-bot` contains a Skool API key in plain text. Consider rotating it and removing it from the repo.
