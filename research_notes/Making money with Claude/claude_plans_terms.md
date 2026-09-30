# The Claude Subscription as a Money-Making Tool (plans, terms, capabilities, copyright) — as of 2026-09-30

## 1. Current Claude plan tiers, prices, usage limits and included features

### Takeaway
Plans in late 2026 are Free ($0), Pro ($20/mo or $17/mo billed annually), Max 5x ($100/mo) and Max 20x ($200/mo), Team (Standard $25/$20 annual, Premium $125/$100 annual per seat), and Enterprise. All paid plans include Claude Code, Cowork, Claude in Chrome and Claude Design. Usage runs on a 5-hour session cap plus a weekly cap, and the cap is shared between claude.ai and Claude Code.

### Cited Findings
- **Free**: $0; web/desktop/mobile chat, web search, file creation, code execution, memory, artifacts, connectors, skills — [claude.com/pricing](https://claude.com/pricing) (fetched 2026-09-30)
- **Pro**: $20/month, or $17/month billed annually; "5x+ more" usage than Free; includes Claude Code, Claude Design/Slides/Docs, "Claude Science", Projects, the Chrome and Microsoft 365 extensions, and Research — [claude.com/pricing](https://claude.com/pricing)
- **Max 5x**: $100/month, 5x Pro usage per 5-hour session, higher output limits, priority access at peak times. **Max 20x**: 20x Pro usage per session, maximum output limits — [claude.com/pricing](https://claude.com/pricing). The support article gives Max 20x as **$200/month**, monthly billing only, with "priority access to our newest features and models" — [support.claude.com: What is the Max plan](https://support.claude.com/en/articles/11049741-what-is-the-max-plan). (The page summary I fetched said Max 20x was "From $100/month". That is probably a parsing artifact; the support article's $200 is the reliable figure.)
- **Team**: Standard seat $25/mo ($20 annual) with more usage than Pro, enterprise search, central billing and SSO. Premium seat $125/mo ($100 annual) with 5x Standard usage. **Enterprise**: $20/seat/mo plus API usage rates (annual), spend controls, SCIM, audit logs, HIPAA-ready option — [claude.com/pricing](https://claude.com/pricing). Team requires a minimum of 5 seats — [ai.zenken.co.jp (secondary)](https://ai.zenken.co.jp/en/post/claude-cowork-pricing/)
- The pricing page lists these model families: Opus, Sonnet, Haiku, "Fable" — [claude.com/pricing](https://claude.com/pricing)
- **How limits work**: a session limit resets every 5 hours, a weekly limit resets at a fixed time assigned to each account, and "additional caps may apply at Anthropic's discretion" — [support.claude.com Max plan](https://support.claude.com/en/articles/11049741-what-is-the-max-plan)
- Limits are "shared across Claude and Claude Code, meaning all activity in both tools counts against the same usage limits." When you hit a limit you can wait for the reset, turn on usage credits (extra usage), or switch to a Console/API account for intensive work — [support.claude.com: Using Claude Code with Pro or Max](https://support.claude.com/en/articles/11145838-using-claude-code-with-your-pro-or-max-plan)
- "Advertised usage limits for Pro and Max plans assume ordinary, individual usage of Claude Code and the Agent SDK." — [Claude Code docs: Legal and compliance](https://code.claude.com/docs/en/legal-and-compliance)
- **2026 limit changes (secondary sources, not confirmed on an Anthropic page)**: on May 6, 2026 Anthropic reportedly doubled Claude Code's 5-hour limits on all paid plans and removed peak-hour throttling. Estimated weekly Opus budget went from about 50h to about 75h on Max 5x and from about 200h to about 300h on Max 20x — [verdent.ai](https://www.verdent.ai/guides/claude-code-limits-doubled-may-2026). A promotion from May 13 to Aug 31, 2026 added 50% to Max weekly Claude Code limits and has now ended — [support.claude.com article 15910845](https://support.claude.com/en/articles/15910845-claude-code-may-july-2026-weekly-limits-promotion). A third-party estimate puts Max 5x at about 140–280 h/week of Sonnet in Claude Code and Max 20x at about 240–480 h/week — [search summary citing ai-toolbox / morphllm (secondary)](https://www.morphllm.com/claude-code-usage-limits)
- **Cowork**: available on the paid plans (Pro, Max, Team, Enterprise). It launched on Max first, then came to Pro with a warning that Pro users may hit limits sooner — [support.claude.com Get started with Cowork](https://support.claude.com/en/articles/13345190-get-started-with-cowork); [Ben's Bites](https://news.bensbites.com/posts/55592-anthropic-makes-claude-cowork-available-to-20month-pro-subscribers-after-launching-it-for-max-users-and-says-pro-users-may-hit-their-usage-limits-sooner)
- **Claude in Chrome**: a browser extension that reads pages, clicks and navigates. It needs a paid plan (Free accounts cannot sign in) and became generally available around Aug 26, 2026 — [gigazine](https://gigazine.net/gsc_news/en/20260827-claude-chrome-available/); [support.claude.com release notes](https://support.claude.com/en/articles/12306336-claude-in-chrome-release-notes)
- **Claude Design**: an Anthropic Labs product announced in April 2026 (sources give Apr 17 and Apr 20). It is powered by Opus 4.7 and in research preview for Pro, Max, Team and Enterprise. It produces designs, interactive prototypes, slide decks, landing pages, social and marketing assets, and can build a brand design system from a codebase or design files — [TechCrunch](https://techcrunch.com/2026/04/17/anthropic-launches-claude-design-a-new-product-for-creating-quick-visuals/); [Unite.AI](https://www.unite.ai/anthropic-launches-claude-design-for-visual-prototyping-and-presentations/)

### Inferences
- For a side business, Pro at $20 is the entry point for Claude Code, Cowork and the Chrome agent. Heavy daily agentic or coding work realistically needs Max 5x or 20x, because chat and Code draw on the same pool.
- The August 31 promotion has ended, so weekly Max limits in October 2026 are back at "standard" levels. These include the reported May doubling of the 5-hour cap, if that is accurate.

### Gaps
- Anthropic does not publish exact token or message counts per tier. Hour estimates come from third parties.
- I could not confirm the May 6, 2026 doubling on an anthropic.com page; only secondary reports.
- Current Free-plan access to Claude Code and Cowork: the pricing page lists Claude Code under Pro, which suggests Free does not include it, but I did not confirm this.

## 2. Consumer Terms and Usage Policy: output ownership, commercial use, restrictions, consumer vs commercial terms

### Takeaway
The Consumer Terms (effective Oct 8, 2025) assign users Anthropic's rights in Outputs, "if any". Nothing bars selling work you make with Claude. The key restrictions are:
- no bot or script access to consumer plans except through an API key
- no account sharing
- no reselling the Services
- no using outputs to build competing models
- (since Feb 2026, explicitly) no use of Free, Pro or Max OAuth credentials in third-party tools or in the Agent SDK

The Usage Policy (effective Sep 15, 2025) forbids fraud, spam, fake reviews and plagiarism. In high-risk domains it requires human review and AI disclosure.

### Cited Findings
- **Scope**: the Consumer Terms govern "Claude.ai, Claude Pro, and other products and services that we may offer for individuals." The Commercial Terms govern API keys, the Console and similar offerings — "this does not include Claude.ai or Claude Pro use for individuals or entities." — [Consumer Terms](https://www.anthropic.com/legal/consumer-terms)
- **Claude Code**: Free, Pro and Max users are under the Consumer Terms; Team, Enterprise and API users are under the Commercial Terms — [Claude Code Legal and compliance](https://code.claude.com/docs/en/legal-and-compliance)
- **Effective date**: "Effective October 8, 2025" — [Consumer Terms](https://www.anthropic.com/legal/consumer-terms)
- **Ownership**: users keep ownership of their Inputs. "Subject to your compliance with our Terms, we assign to you all of our right, title, and interest—if any—in Outputs." — [Consumer Terms](https://www.anthropic.com/legal/consumer-terms)
- **Automation ban**: you may not "access the Services through automated or non-human means, whether through a bot, script, or otherwise," "except when you are accessing our Services via an Anthropic API Key or where we otherwise explicitly permit it" — [Consumer Terms](https://www.anthropic.com/legal/consumer-terms)
- **No sharing**: "You may not share your Account login information, Anthropic API key, or Account credentials with anyone else. You also may not make your Account available to anyone else." — [Consumer Terms](https://www.anthropic.com/legal/consumer-terms)
- **No competing products or reselling**: users may not use the Services "to develop any products or services that compete with our Services, including to develop or train any artificial intelligence or machine learning algorithms or models or resell the Services." — [Consumer Terms](https://www.anthropic.com/legal/consumer-terms)
- **Other terms**: minimum age is 18, or higher where local law requires. Outputs "may contain material inaccuracies". Anthropic may "modify, suspend, or discontinue the Services… at any time without notice" — [Consumer Terms](https://www.anthropic.com/legal/consumer-terms)
- **OAuth and credential rule**: OAuth authentication "is intended exclusively for purchasers of Claude Free, Pro, Max, Team, and Enterprise subscription plans and is designed to support ordinary use of Claude Code and other native Anthropic applications." Developers building products, including with the Agent SDK, "should use API key authentication." Anthropic "does not permit third-party developers to offer Claude.ai login into their own applications, or to route requests through Free, Pro, or Max plan credentials on behalf of their users," and developers may not "collect, store, or intermediate Claude.ai credentials or session tokens." Enforcement may happen "without prior notice." — [Claude Code Legal and compliance](https://code.claude.com/docs/en/legal-and-compliance)
- **Timeline**: the docs were clarified on Feb 19, 2026. Billing enforcement started Apr 4, 2026: third-party-tool traffic, such as OpenClaw-type harnesses, no longer draws on subscription quota and is billed as overage — [AlternativeTo](https://alternativeto.net/news/2026/2/anthropic-officially-bans-using-subscription-authentication-for-third-party-claude-use); [Gigazine](https://gigazine.net/gsc_news/en/20260220-anthropic-third-party-block) (secondary; the April 4 date is from the search summary)
- **Reselling Claude Code**: offering Claude Code inside your own product requires the Commercial Terms and an unmodified binary. You "may not pay for, resell, or intermediate Claude usage on their end users' behalf"; each end user must authenticate with their own key or subscription. You may not use "Claude Code" or "Anthropic" in your product name or logo — [Claude Code Legal and compliance](https://code.claude.com/docs/en/legal-and-compliance)
- **Usage Policy** (effective Sep 15, 2025) prohibits:
  - fraud, scams, phishing and malware
  - plagiarism, or "submit[ting] AI-assisted work without proper permission or attribution"
  - IP infringement, spam, and fake reviews, comments or media
  - impersonation, or fake personas used to attribute content
  - deceptive or manipulative techniques
  — [Usage Policy](https://www.anthropic.com/legal/aup)
- **High-risk domains** (legal, financial, employment/hiring, insurance and similar) require a human in the loop and disclosure of AI use to consumers. Media or journalistic content that is automatically generated and published needs an AI disclosure. Violations can lead to throttling, suspension or termination — [Usage Policy](https://www.anthropic.com/legal/aup)

### Inferences
- **Allowed**: using a Pro or Max plan interactively to produce deliverables you sell, such as code, copy, designs, apps and documents. This is consistent with the terms, since outputs are assigned to you and nothing requires non-commercial use.
- **Not allowed on a consumer plan**:
  - running an automated backend service that calls claude.ai
  - letting clients use your login
  - wiring your Max OAuth token into a SaaS or a third-party agent harness

  Any product that serves end users needs API keys under the Commercial Terms.
- Running Claude Code yourself, including headless or scripted runs on your own machine, is an explicitly supported native application. The line is drawn at third-party apps, routing on behalf of others, and non-"ordinary, individual" usage.
- The Consumer Terms offer weaker business protections than the Commercial Terms. For example, the Commercial Terms typically include IP indemnity for outputs and a no-training default; I did not verify either for this note.

### Gaps
- I did not fetch the Commercial Terms, so I cannot confirm IP indemnity or data-use differences.
- The consumer data-training opt-in/opt-out setting (Oct 2025 terms change) was not verified in this pass.

## 3. Does Claude generate raster images? Design capabilities

### Takeaway
As of late 2026 I found no evidence that Claude natively generates raster images (photos or painted art). Visual output goes through code: SVG, HTML/CSS/canvas, charts, slides and prototypes, including the new Claude Design product. Claude also reads and analyzes images well.

### Cited Findings
- "Claude has vision and document understanding but no native image, audio, or video generation"; image workflows pair Claude with separate image generators — [suprmind.ai (secondary)](https://suprmind.ai/hub/claude/); [CyberLink blog 2026](https://es.cyberlink.com/blog/ia-generativa/5215/claude-ai-guia-completa)
- Opus 4.7 (released Apr 16, 2026) supports vision input, not image output — [speculativechic (secondary)](https://speculativechic.com/claude-ai-model-updates-2026-analysis-performance-features-and-developer-impact/)
- Prediction markets still ask whether Anthropic will add native image generation, which implies it has not happened — [Manifold](https://manifold.markets/Soli/will-anthropic-natively-integrate-i)
- Claude Design generates designs, prototypes, decks, landing pages and social or marketing assets from prompts, with iterative edits and brand design systems — [TechCrunch](https://techcrunch.com/2026/04/17/anthropic-launches-claude-design-a-new-product-for-creating-quick-visuals/)
- The Free plan includes file creation, code execution and artifacts, which produce HTML, SVG, documents and similar files — [claude.com/pricing](https://claude.com/pricing)

### Inferences
- Money-making that depends on design fits Claude when the product is vector or code-based: logos and icons as SVG, landing pages, slide decks, templates, data visualizations, printables built as HTML/PDF, and generative art from code such as p5.js or canvas. Photorealistic or illustrative raster work needs a separate tool (Midjourney, GPT-Image, Flux, etc.). Claude can write the prompts and critique the results.
- Claude Design's outputs are probably HTML/code-rendered visuals rather than diffusion images. This is inferred from how it is described, not confirmed.

### Gaps
- I found no primary Anthropic statement denying image generation, and absence of evidence is not proof. No Anthropic announcement of image generation turned up either.

## 4. Claude Code for side businesses and Pro vs Max for heavy use

### Takeaway
Claude Code comes with every paid plan and can build apps, automation scripts and sites. Claude in Chrome and Cowork add browser and desktop task automation. Pro's shared, capped pool is fine for light projects; sustained agentic coding realistically needs Max. You cannot legally resell or intermediate subscription access.

### Cited Findings
- Claude Code is included on Pro and above, and Pro and Max limits are shared between chat and Code — [claude.com/pricing](https://claude.com/pricing); [support.claude.com](https://support.claude.com/en/articles/11145838-using-claude-code-with-your-pro-or-max-plan)
- Pro users can buy extra usage (usage credits) after hitting limits, or move to API billing — [support.claude.com](https://support.claude.com/en/articles/11145838-using-claude-code-with-your-pro-or-max-plan)
- Max gives 5x or 20x Pro usage per 5-hour session plus priority access — [claude.com/pricing](https://claude.com/pricing)
- Estimated weekly Opus hours: about 75 (Max 5x) and about 300 (Max 20x) after May 2026, per a secondary source — [verdent.ai](https://www.verdent.ai/guides/claude-code-limits-doubled-may-2026)
- Claude in Chrome reads, clicks and navigates websites in the user's browser (paid plans) — [search summary, claudemarket.ai / gigazine](https://gigazine.net/gsc_news/en/20260827-claude-chrome-available/)
- Products built for others must use API keys, including Agent SDK apps — [Claude Code Legal and compliance](https://code.claude.com/docs/en/legal-and-compliance)

### Inferences
- **Viable models**:
  - freelance development or automation where you use Claude Code yourself and deliver code the client owns
  - building micro-SaaS products where the deployed product calls the API on API billing, not your subscription
  - internal automation of your own workflows
- If client apps embed Claude at runtime, budget for API costs separately from the subscription.

### Gaps
- No official hour or token figures from Anthropic for Pro in Claude Code.

## 5. Copyright of AI outputs and implications for selling AI-assisted work

### Takeaway
Anthropic assigns you whatever rights it has in outputs, but there may be none. In the US, purely AI-generated material is not copyrightable. Prompts alone are insufficient (USCO Part 2, Jan 29, 2025). The human-authorship rule was left standing when the Supreme Court denied cert in *Thaler v. Perlmutter* on Mar 2, 2026. Human selection, arrangement and modification can be protected.

### Cited Findings
- USCO released Part 2 of its Copyright and AI report on Jan 29, 2025. Its conclusions:
  - copyright protects only human authorship
  - prompts alone do not give enough control over expressive elements
  - humans can claim authorship where AI is a tool, and in expressive modifications or in the selection and arrangement of AI output
  - decisions are case by case
  - no new legislation is needed
  — [Manatt](https://manatt.com/insights/newsletters/copyright-office-releases-new-report-on-copyrightability-of-ai-works); [Ballard Spahr](https://www.ballardspahr.com/insights/alerts-and-articles/2025/01/copyright-office-issues-report-on-copyrightability-of-ai-content); [PrivacyWorld](https://www.privacyworld.blog/2025/02/copyright-office-copyrighting-ai-generated-works-requires-sufficient-human-control-over-the-expressive-elements-prompts-are-not-enough/). Primary source: https://www.copyright.gov/ai/ (blocked by the network proxy in this session)
- *Thaler v. Perlmutter*: the D.C. Circuit affirmed on Mar 18, 2025 that the Copyright Act requires a human author, and the Supreme Court denied certiorari on Mar 2, 2026 — [Mayer Brown](https://www.mayerbrown.com/en/insights/publications/2026/03/supreme-court-denies-review-in-ai-authorship-case); [Baker Donelson](https://www.bakerdonelson.com/supreme-court-denies-certiorari-in-thaler-v-perlmutter-ai-cannot-be-an-author-under-the-copyright-act); [Reed Smith](https://www.reedsmith.com/our-insights/blogs/viewpoints/102mlpl/supreme-court-denies-certiorari-in-thaler-v-perlmutter-human-only-rule-for-ai/)
- Anthropic's assignment covers only its rights "if any" — [Consumer Terms](https://www.anthropic.com/legal/consumer-terms)
- The Usage Policy forbids passing off AI-assisted work "without proper permission or attribution" and forbids infringing third-party IP — [Usage Policy](https://www.anthropic.com/legal/aup)

### Inferences
- You can legally sell Claude-assisted work: code, text, templates, designs. But raw AI output may be freely copyable by competitors. Protection comes from substantial human editing, selection and arrangement, from trade secrets or unpublished code, and from brand and trademark.
- When registering copyright, the AI-generated portions must be disclosed and disclaimed; this follows from USCO guidance on registrations.
- Buyers or clients may require warranties of originality or IP ownership. Consumer-plan users should not promise more than they have: only whatever rights exist, with no indemnity from Anthropic.
- Platforms such as KDP and Etsy may have their own AI disclosure rules; this is outside my scope.

### Gaps
- I could not read copyright.gov directly (egress blocked), so I did not verify the Part 2 text or any 2026 USCO registration guidance updates myself.
- Non-US rules (UK computer-generated works provision, EU, China) were not covered.
- Part 3 (training/fair use, pre-publication May 2025) is not relevant here and was not re-verified.
