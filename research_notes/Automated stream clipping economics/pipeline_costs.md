# Full cost of an automated stream-clipping pipeline (2026)

Research date: 2026-09-30. All prices are in USD unless marked (EUR). Where a source gives its own date, it appears in brackets. Several primary vendor pages (opus.pro, developers.tiktok.com, docs.vizard.ai, costbench.com) were blocked by the research network proxy. Figures for those come from search-result snippets of the pages or from secondary aggregators, and are flagged. Before relying on any price, check it against the vendor's live page.

## 1. Discovery: how to find the most-watched streams/VODs of recent days

### Takeaway
Discovery costs almost nothing. The Twitch Helix API is free and allows 800 points/min per app token, which is enough to poll live streams, recent VODs and top clips. Kick's official API has no confirmed viewer-sorted endpoint, so people fill the gap with third-party scrapers. A paid stats API such as StreamsCharts ($199–$1,099/mo) is optional: it adds cross-platform "most-watched" rankings.

### Cited Findings
- Twitch Helix rate limit: 800 points per minute per client. Most endpoints, including Get Streams and Get Clips, cost 1 point. The bucket refills at about 1 point every 75 ms. Create Clip has its own separate limit. — [Twitch dev forum: Error 429](https://discuss.dev.twitch.tv/t/error-429-limitation-helix-api/25216); [Rate limit bucket thread](https://discuss.dev.twitch.com/t/rate-limit-bucket-app-vs-user-access-token/37904)
- The Twitch API costs nothing: rate limits apply, but there is no paid tier (in the same threads). Get Streams returns live streams paginated and sorted by viewer count — [DEV Community: paginated Twitch stream data](https://dev.to/aarongoldsmith1/twitch-tv-api-get-live-stream-data-from-paginated-results-4ama)
- StreamsCharts API [2026] uses flat per-request credits:
  - Starter: $199/mo for 500 credits
  - Business: $749/mo for 3,000 credits
  - Elite: $1,099/mo for 5,000 credits
  - Core stats cost 1 credit, enrichment 2 credits, streamer-list endpoints 5–10 credits. Top-ups are billed at the plan's per-credit rate.
  - Free tier: top 100 Twitch channels for the last 7 days, at 0 credits. — [StreamsCharts API pricing](https://streamscharts.com/api/pricing); [StreamsCharts self-serve API announcement](https://streamscharts.com/news/streams-charts-opens-self-serve-api-access)
- For Kick, search found only third-party or unofficial APIs that give live viewer counts and top-streams-by-viewers: Apify actors and oanor's Kick API. No official docs.kick.com endpoint that sorts livestreams by viewers turned up. — [Apify Kick scraper](https://apify.com/getascraper/kick-scraper); [Apify: find top Kick streamers by viewers](https://apify.com/aitooolsmax/kick-data-scraper/examples/find-top-kick-streamers-live.md); [oanor Kick API](https://oanor.com/api/kick-api)
- YouTube Data API: each Google Cloud project gets 10,000 quota units/day for free. Search and list calls use this general bucket. — [Phyllo: Is the YouTube API free in 2026](https://www.getphyllo.com/post/is-the-youtube-api-free-in-2026-quota-limits-costs-when-to-pay)

### Inferences
- Polling the top ~500 Twitch live streams every 5 minutes takes about 5 calls (100 results per page) × 288 polls/day, roughly 1,440 points/day. That is far under the 800/min cap, so Twitch discovery is effectively $0.
- The free StreamsCharts tier (top 100 Twitch channels, last 7 days) may be enough for the "most-watched of past few days" question at low volume. The $199 Starter plan is only justified if you need Kick/YouTube rankings too.
- Budget $0–$50/mo for Kick data via Apify-style actors. This is an estimate: Apify per-result prices were not collected.

### Gaps
- I did not verify the official Kick public API (docs.kick.com) capabilities or its rate limits.
- TwitchTracker and SullyGnome API pricing was not found. As far as I know, neither sells a public paid API, but I could not confirm this.
- I did not get the exact YouTube quota cost of search.list, which is widely cited at 100 units. Check it in the Google quota calculator.

## 2. Ingest/download: yt-dlp/streamlink, bandwidth, storage, VOD sizes

### Takeaway
A 1080p60 Twitch VOD is about 2.7 GB/hour at 6,000 kbps. yt-dlp and streamlink are free, and ingress to storage is free. Storage stays under $30/mo even at the high scenario, provided VODs are kept only for ~7 days, or you download just the segments around candidate moments.

### Cited Findings
- 6,000 kbps is about 2.7 GB per hour. Twitch's 1080p60 guidance is about 6,000 kbps. — [Videomaker: best bitrate for Twitch](https://www.videomaker.com/how-to/shooting/files-and-formats/what-is-the-best-bitrate-for-a-twitch-stream/); [Livereacting bandwidth calculator](https://www.livereacting.com/tools/stream-bitrate-bandwidth-calculator)
- Cloudflare R2: $0.015/GB-month (Standard) or $0.01 (Infrequent Access), with $0 egress. Class A operations cost $4.50 per million and Class B $0.36 per million. — [Mecanik: R2 pricing explained](https://mecanik.dev/en/posts/cloudflare-r2-pricing-explained-real-costs-vs-s3-and-backblaze/); [DevOpsBoys R2 vs S3 vs B2 2026](https://devopsboys.com/blog/cloudflare-r2-vs-aws-s3-vs-backblaze-b2-2026)
- Backblaze B2 [July 2026]: $6.95/TB-month with free transactions. Egress is free up to 3× average monthly storage, then $0.01/GB. — [SpeedtestHQ R2 vs B2 2026](https://www.speedtesthq.com/compare/cloudflare-r2-vs-backblaze-b2)
- Hetzner raised prices on 2026-04-01 (cloud about +30–35%) and again on 2026-06-15 (new orders only). Examples:
  - CX23: €3.99 → €5.49
  - CPX22: €7.99 → €19.49
  - CPX52: €36.49 → €100.49
  - — [wz-it: Hetzner price increase June 2026](https://wz-it.com/en/blog/hetzner-price-increase-june-2026-cpx-ccx-alternatives/); [Igor'sLAB: Hetzner April 2026](https://www.igorslab.de/en/hetzner-to-significantly-increase-prices-for-cloud-and-dedicated-servers-from-april-2026/)

### Inferences
Assumptions: about 2 publishable clips per VOD-hour analysed, and VODs kept 7 days.

| Scenario | VOD-hours/day | Download | Rolling storage | R2 cost | B2 cost |
|---|---|---|---|---|---|
| Low | 5 | 13.5 GB/day | ~95 GB | ~$1.4/mo | ~$0.7/mo |
| Mid | 25 | 67 GB/day | ~470 GB | ~$7/mo | ~$3.3/mo |
| High | 100 | 270 GB/day, ~8 TB/mo | ~1.9 TB | ~$28/mo | ~$13/mo |

- Downloading only audio (about 0.1 GB/h at 128 kbps) plus short video windows around candidate moments cuts bandwidth by about 90%.
- At the high scenario, 8 TB/mo of ingress needs a VPS or server with generous included traffic. Hetzner-class servers typically include 20 TB+, but that allowance was not verified in this research.

### Gaps
- Twitch's actual VOD bitrates vary. Many partners stream at 6–8 Mbps, and quality tiers differ. 2.7 GB/h is nominal.
- No sourced AWS S3 2026 price was collected. It is commonly about $0.023/GB-month plus about $0.09/GB egress, but this is unverified here.
- Legal/ToS risk of downloading VODs (Twitch/Kick/YouTube ToS and copyright) was not costed.

## 3. Highlight detection: chat spikes, top clips, transcription, LLM scoring, GPUs

### Takeaway
The cheapest signal is free: Twitch's own top clips (Get Clips, sorted by views) and chat-message velocity spikes. Transcription is the biggest variable cost. It costs $0.15–$0.46 per VOD-hour through APIs, versus about $0.01 per VOD-hour self-hosted on a rented RTX 4090. LLM scoring with Gemini 2.5 Flash or GPT-5 mini costs about 1 cent per VOD-hour.

### Cited Findings
Transcription APIs:
- OpenAI Whisper API: $0.006/min ($0.36/h). gpt-4o-mini-transcribe: $0.003/min ($0.18/h). — [DEV Community: AI transcription pricing 2026](https://dev.to/eli_9c82b7dfe52c1bc371ffe/ai-transcription-pricing-2026-whisper-vs-deepgram-vs-assemblyai-2eec); [ConvertAudioToText pricing 2026](https://convertaudiototext.com/blog/transcription-pricing-comparison-2026)
- Deepgram Nova-3 monolingual: $0.0077/min pre-recorded pay-as-you-go ($0.46/h), $0.0048/min streaming. Multilingual: $0.0092/min pre-recorded, $0.0058/min streaming. — [DEV Community 2026](https://dev.to/eli_9c82b7dfe52c1bc371ffe/ai-transcription-pricing-2026-whisper-vs-deepgram-vs-assemblyai-2eec)
- AssemblyAI [Aug 2026]: $0.15–$0.21/hour (Universal from $0.15/h, which is $0.0025/min), plus $50 free credit. — [CostBench AssemblyAI vs Deepgram 2026](https://costbench.com/compare/assemblyai-vs-deepgram), via search snippet (page blocked)

LLM scoring:
- Gemini 2.5 Flash: $0.30 per 1M input tokens, $2.50 per 1M output
- Claude Haiku 4.5: $1.00 input, $5.00 output
- GPT-5 mini: $0.25 input, $2.00 output
- [dated 2026-08-13] — [ModelCompare Gemini 2.5 Flash vs Claude Haiku 4.5](https://modelcompare.dev/pt/compare/google-gemini-2-5-flash-vs-anthropic-claude-haiku-4-5)

GPU cloud:
- RunPod RTX 4090: about $0.34/h (Community Cloud) or $0.69/h (Secure Cloud).
- Vast.ai RTX 4090: about $0.34–$0.50/h on-demand, from about $0.15/h interruptible.
- Both bill per second. — [Spheron: RunPod vs Vast.ai 2026](https://www.spheron.network/blog/runpod-vs-vastai-2026/)

Open-source reference builds:
- VadlapatiKarthik Auto-Clipper finds highlights in Twitch/Kick streams through chat spikes and retention data, cuts with FFmpeg, subtitles with Whisper and uploads to YouTube.
- OpenShorts uses faster-whisper word timestamps, transcript scoring, FFmpeg cutting and MediaPipe face tracking for 9:16 reframing.
- AutoClip runs locally: an LLM picks moments, then it reframes with speaker tracking and burns in captions.
- Sources: [GitHub topic: video-clipping](https://github.com/topics/video-clipping); [OpenShorts](https://openshorts.84-8-216-188.sslip.io/); [artbyjazi/autoclip](https://github.com/artbyjazi/autoclip); [opensource-clipping](https://github.com/NaufalRizqullah/opensource-clipping); [SamurAIGPT AI-Youtube-Shorts-Generator](https://oosmetrics.com/repo/SamurAIGPT/AI-Youtube-Shorts-Generator)

### Inferences
Monthly transcription cost per scenario (VOD-hours/month: low 150, mid 750, high 3,000):

| Scenario | gpt-4o-mini-transcribe ($0.18/h) | AssemblyAI ($0.15/h) | Deepgram pre-recorded ($0.46/h) | Self-hosted faster-whisper on 4090 |
|---|---|---|---|---|
| Low (150 h) | $27 | $22.5 | $69 | ~$1.3 |
| Mid (750 h) | $135 | $112 | $345 | ~$6.4 |
| High (3,000 h) | $540 | $450 | $1,380 | ~$25 |

- The self-hosted column assumes faster-whisper large-v3 runs about 40× realtime on a 4090 at $0.34/h. The 40× speed is my estimate and was not sourced.
- LLM token assumptions: a 1-hour stream transcript is about 12–15k tokens. Add sampled chat and prompt for about 20k input tokens, and about 2k output tokens per VOD-hour.
  - Gemini 2.5 Flash: 20k × $0.30/M + 2k × $2.50/M ≈ $0.011 per VOD-hour. That is about $1.7 / $8 / $33 per month for low / mid / high.
  - Claude Haiku 4.5: ≈ $0.03 per VOD-hour, or $4.5 / $22 / $90 per month.
  - Adding a second-pass title/hook/caption generation per clip is about 2k tokens per clip, which is negligible (< $5/mo even at 6,000 clips/mo on Flash).
- Chat-velocity detection needs only chat logs from IRC/EventSub or VOD chat replay downloaders. It is CPU-only and costs about $0.
- Using Twitch top clips as seeds skips VOD transcription for Twitch entirely. You then download only 30–60 s clips, which cuts both transcription and storage costs sharply.

### Gaps
- I did not collect a Lambda Labs 2026 GPU price.
- Current Anthropic, OpenAI and Google flagship model prices were not collected. Only the small models above were.
- Measured faster-whisper throughput on a 4090 was not sourced.

## 4. Rendering: FFmpeg, captions, auto-reframing (compute per clip)

### Takeaway
Rendering a 30–90 s 1080×1920 clip with burned-in captions and face-tracked crop takes CPU-seconds to about a minute. At any scenario, rendering fits on one mid-size VPS or on the same GPU box, so the marginal compute cost per clip is well under $0.01.

### Cited Findings
- OpenShorts and AutoClip do the full cut → 9:16 reframe → caption burn-in with FFmpeg plus MediaPipe face tracking. Both are open source and self-hostable. — [OpenShorts](https://openshorts.84-8-216-188.sslip.io/); [artbyjazi/autoclip](https://github.com/artbyjazi/autoclip)
- Hetzner cost-optimized CX23 costs €5.49/mo after June 2026. Dedicated-vCPU CPX22 costs €19.49/mo and CPX52 €100.49/mo (new orders). — [wz-it Hetzner June 2026](https://wz-it.com/en/blog/hetzner-price-increase-june-2026-cpx-ccx-alternatives/)
- A GPU box (RTX 4090) costs $0.34/h on RunPod Community, and NVENC encoding is available on it. — [Spheron 2026](https://www.spheron.network/blog/runpod-vs-vastai-2026/)

### Inferences
- Rough benchmark (my estimate, not sourced): a 60 s x264 "veryfast" 1080×1920 encode with an ASS subtitle overlay takes about 20–40 s on 4 vCPU. MediaPipe face detection at 5 fps samples adds about 10–20 s.
- On that basis, 200 clips/day is about 2–3 CPU-hours/day, which fits comfortably on one 8-vCPU VPS. Hetzner CPX-class costs roughly €20–€100/mo after the 2026 increases. Alternatively, run on a GPU box for about $0.002–$0.005 per clip.

| Scenario | Rendering + orchestration hosting |
|---|---|
| Low | ~$6–$20/mo |
| Mid | ~$20–$40/mo |
| High | ~$60–$120/mo |

### Gaps
- No sourced per-clip FFmpeg benchmarks.

## 5. Off-the-shelf SaaS alternatives and pricing

### Takeaway
SaaS clippers cost $15–$100/mo per seat, but they meter by minutes of source video. At pipeline volume (hundreds of VOD-hours/month) they either need enterprise contracts or become far more expensive than self-hosting. They make sense for the low scenario, or as a highlight/reframe engine behind your own discovery layer.

### Cited Findings
- OpusClip [2026]:
  - Free: $0, 60 credits
  - Starter: $15/mo, 150 credits
  - Pro: $29/mo (or $174/yr), 300 credits/mo, "limited API"
  - Business: custom pricing with full API and integrations
  - — [Creatify: OpusClip pricing 2026](https://creatify.ai/blog/opusclip-pricing-plans-and-what-you-ll-actually-pay-in-2026); [CostBench Opus Clip 2026](https://costbench.com/software/ai-video-editing-saas/opus-clip/) (secondary sources; opus.pro was blocked)
- Submagic [2026]:
  - Starter: $19/mo; Starter + Magic Clips: $38
  - Pro: $39; Pro + Magic Clips: $58
  - Business + API: $69; Business + API + Magic Clips: $88
  - — [CostBench Submagic 2026](https://costbench.com/software/ai-video-editing-saas/submagic/) via snippet
- Klap [2026]: $14–$94/mo. — [CostBench Klap 2026](https://costbench.com/software/ai-video-editing-saas/klap/) via snippet (tier details blocked)
- Vizard: the API is included on all paid plans, Creator ($29/mo) and Business ($39/mo). API jobs consume the same upload minutes as the web app. — [Vizard API docs: pricing](https://docs.vizard.ai/docs/pricing) via snippet
- Eklipse (gaming/stream-focused): paid from about $12.50/mo billed annually, or about $24.99 month-to-month. — [Eklipse blog: is Eklipse free](https://blog.eklipse.gg/eklipse-news-and-guide/is-eklipse-free-pricing-and-features-explained.html)

### Inferences
- If one OpusClip credit equals about 1 minute of source video (a common understanding, not verified here), Pro's 300 credits cover only 5 VOD-hours/month. The mid scenario needs about 45,000 source-minutes/month, which pushes you onto Business/custom pricing.
- Stream-native tools (Eklipse, StreamLadder, Powder) key off gaming moments and Twitch clips. They are cheap per seat but built for one creator's own channel, not multi-streamer farming.
- Hybrid strategy: use your own discovery plus Twitch top clips as the source, then send only short pre-trimmed segments to a SaaS API such as Submagic Business+API at $69 or Vizard at $29–$39. That keeps minutes metered low.

### Gaps
- No verified 2026 pricing was found for StreamLadder, Munch, 2short.ai, Powder, Crayo or Quso/vidyo.ai, or for OpusClip's API per-minute rate. The pages were blocked or absent from results.

## 6. Publishing: TikTok, YouTube, Instagram APIs; schedulers; multi-account costs

### Takeaway
Official APIs are free but gated:
- TikTok needs an app audit before posts can be public. Unaudited apps post private-only and serve at most 5 users per 24h.
- YouTube uploads now cost 100 units in a separate bucket of about 100 uploads/day per project (changed Dec 2025).
- Instagram allows 50–100 API posts per account per 24h, and Reels are capped at 90 s via the API.

Schedulers such as Ayrshare cost $149–$599+/mo. Grey-hat multi-accounting (anti-detect browsers plus proxies) adds $11–$89/mo plus about €3/GB of proxy traffic.

### Cited Findings
TikTok:
- Unaudited API clients can post only in SELF_ONLY (private) mode. Up to 5 users can post per 24h, and those accounts must be private at posting time. — [TikTok Content Sharing Guidelines](https://developers.tiktok.com/docs/en/content-sharing-guidelines) via snippet (page blocked)
- Direct Post is typically capped around 15 posts/day per creator account. This is not a hard published number; it is shared across all apps. — [Postly FAQ](https://postly.ai/resources/faq/publishing/publishing-23); [Blotato TikTok API](https://www.blotato.com/api/tiktok) (secondary)

YouTube:
- On 2025-12-04 Google cut videos.insert from about 1,600 units to about 100 units. Uploads now draw from a separate bucket with a default of 100 calls/day, so about 100 uploads/day per project, up from about 6. The general budget stays at 10,000 units/day per project, free. — [Phyllo: YouTube API 2026](https://www.getphyllo.com/post/is-the-youtube-api-free-in-2026-quota-limits-costs-when-to-pay); [ChannelCrawler: YouTube API daily limit (Mar 2026)](https://channelcrawler.com/insights/youtube-api-daily-limit-quotas-costs-and-how-to-scale-beyond-10000-units-channelcrawler)
- Older guides still cite 1,600 units. Verify in Google's quota calculator.

Instagram:
- The per-account limit is 100 API-published posts per rolling 24h, but some Meta docs say 50. Carousels count as 1 post. Check current usage with GET /<IG_ID>/content_publishing_limit. — [Meta: Instagram Content Publishing](https://developers.facebook.com/docs/instagram-platform/content-publishing); [bundle.social: Instagram API rate limits (Aug 2026)](https://bundle.social/blog/instagram-api-rate-limits)
- API Reels are capped at 90 s. — [bundle.social](https://bundle.social/blog/instagram-api-rate-limits)

Ayrshare [2026]:
- Premium: $149/mo, 1 profile
- Launch: $299/mo, 10 profiles
- Business: $599/mo, 30 profiles, then tiered up to 300
- Enterprise: custom
- Max Pack add-on: +$300/mo for maximum posting limits. Annual billing saves 17%.
- A "profile" is one brand, which can hold all its networks: TikTok, YouTube, Instagram and so on.
- — [Ayrshare pricing](https://www.ayrshare.com/pricing); [Blotato: Ayrshare pricing](https://www.blotato.com/blog/ayrshare-pricing)

Multilogin [2026]:
- PRO 10: $11/mo, 10 profiles, 1 GB proxy
- PRO 50: $29/mo, 50 profiles, 3 GB
- PRO 100: $40/mo, 100 profiles, 5 GB
- BUSINESS 300: $89/mo, 300 profiles, 10 GB
- Extra proxy traffic costs €3/GB.
- — [Multilogin plan comparison](https://multiloginx.helpjuice.com/en_US/account-subscription/subscription-plan-comparison); [Multilogin proxy top-up](https://multiloginx.helpjuice.com/en_US/add-ons/how-to-top-up-multilogin-proxy-traffic)

### Inferences
- **YouTube:** 200 clips/day spread across several channels is under the ~100 uploads/day per GCP project. One or two projects suffice, at $0. Note: public auto-upload from an unverified API project is typically locked to private until Google's API compliance audit. This is not verified here and is analogous to TikTok.
- **TikTok:** real public automation requires passing the audit. Otherwise operators fall back to a scheduler that is already audited (Ayrshare, Buffer, Blotato and similar) or to browser/phone automation.
- **Scheduler costs** at roughly 3 / 10 / 30 brand profiles: Ayrshare Premium × a few or Launch ($149–$299) for low, Launch ($299) for mid, Business ($599, optionally +$300 Max Pack) for high.
- **Proxy bandwidth trap:** if you upload through anti-detect browsers over a metered proxy, each 60 s 1080p clip is roughly 30–60 MB.
  - High scenario: 200 clips/day is about 6–12 GB/day, or 180–360 GB/mo. At €3/GB that is €540–€1,080/mo.
  - This is why API or scheduler posting is much cheaper than proxy-browser posting at scale.
  - Low scenario: about 10–20 GB/mo, or €30–€60.

### Gaps
- No verified 2026 pricing for Buffer, Repurpose.io, Blotato or GoLogin.
- No sourced cost for phone farms or SIMs, and no data on account ban rates.
- I could not access TikTok's audit requirements in full (the page was blocked).

## 7. Hidden costs and scenario totals

### Takeaway
At pipeline scale, pure infrastructure is cheap: roughly $50–$1,300/mo depending on scenario and API-vs-self-host choices. The dominant costs are hidden:
- developer time to build and maintain
- human QA
- schedulers or multi-account tooling
- account bans and demonetization from reposting others' content

### Cited Findings
- Hetzner's two 2026 price rises (+30–35% in April; up to +176% on CPX in June) show that "cheap VPS" assumptions from 2024–25 guides are stale. — [Igor'sLAB](https://www.igorslab.de/en/hetzner-to-significantly-increase-prices-for-cloud-and-dedicated-servers-from-april-2026/); [wz-it](https://wz-it.com/en/blog/hetzner-price-increase-june-2026-cpx-ccx-alternatives/)
- Open-source auto-clippers already exist: Auto-Clipper with FastAPI + Celery + React, OpenShorts, and AutoClip. This cuts build effort to integration work. — [GitHub topic: video-clipping](https://github.com/topics/video-clipping); [OpenShorts](https://openshorts.84-8-216-188.sslip.io/)

### Inferences
Assumptions:
- Low: 10 clips/day, about 5 VOD-hours/day, 3 accounts per platform.
- Mid: 50 clips/day, about 25 VOD-hours/day, 10 accounts.
- High: 200 clips/day, about 100 VOD-hours/day, 30 accounts.
- About 30 days/month. All figures are estimates built from the cited unit prices.

**Scenario totals (monthly):**

| Line item | Low (10/day) | Mid (50/day) | High (200/day) |
|---|---|---|---|
| Discovery (Twitch free; StreamsCharts optional; Kick scraper) | $0–$20 | $0–$220 | $199–$270 |
| Storage (R2/B2, 7-day retention) | ~$1 | ~$3–$7 | ~$13–$28 |
| Transcription (API / self-host) | $22–$27 / ~$1 | $112–$135 / ~$6 | $450–$540 / ~$25 |
| LLM scoring + titles (Flash / Haiku) | $2–$5 | $8–$25 | $35–$95 |
| Compute: VPS + GPU for render/reframe | $10–$20 | $25–$60 | $80–$150 |
| Publishing: official APIs | $0 | $0 | $0 |
| Scheduler (Ayrshare) | $149 | $299 | $599–$899 |
| Anti-detect + proxies (only if not using APIs) | ~$11 + €30–60 | ~$40 + €150–300 | ~$89 + €540–1,080 |
| **Infra subtotal, API route with scheduler** | **~$185–$220** | **~$450–$750** | **~$1,375–$1,900** |
| **Infra subtotal, self-host + own audited APIs, no scheduler** | **~$15–$50** | **~$40–$320** | **~$350–$560** |
| SaaS alternative (OpusClip/Submagic/Vizard) | $29–$88 plus scheduler | Business/custom; likely $300+ | Enterprise quote |

- **Human QA:** reviewing each clip for about 1 minute is 10 / 50 / 200 minutes a day. At an assumed $5–$15/h offshore VA rate (not sourced), that is about $25–$75 / $125–$375 / $500–$1,500 per month.
- **Developer time:** integrating open-source components into a robust multi-platform pipeline plausibly takes 80–200 h up front, plus 10–30 h/mo maintenance (API changes, platform ToS shifts). This is an estimate and not sourced.
- **Account bans/demonetization:** reposted content risks rejection from TikTok Creator Rewards and YouTube's reused-content policy. Expect to budget replacement accounts, and proxies if operating grey-hat. Unquantified.

### Gaps
- No sourced account-ban rates, human QA rates or developer-hour costs.
- No Reddit or Indie Hackers build logs with actual monthly bills were retrieved.
- Clipper revenue programmes (e.g., streamer-paid clipping campaigns) and platform payouts are out of scope, and no data was collected.
