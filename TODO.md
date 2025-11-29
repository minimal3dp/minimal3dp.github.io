# Minimal 3DP TODO & Recommendations

**Last Updated:** December 2025  
**Status:** Strategic Blueprint Integrated - Year 1 Foundation Phase

---

## 🎯 Strategic Context (2025-2035 Blueprint)

**Vision Shift:** From "Content Creator" → "Data Authority & Platform Architect"  
**Core Strategy:** Build M3DP-BRIDGE ecosystem to decouple revenue from manual labor  
**Year 1 Target:** $300-$1,000/month (from current ~$200/month)

**Key Strategic Pillars:**

1. **"Hardware Bridge" Content Model** - Anchor software tutorials (Klipper/OrcaSlicer) to specific popular printers, capturing high-intent search traffic at point of purchase.

2. **Smart Link Infrastructure** - Deploy M3DP-BRIDGE with go.minimal3dp.com redirects to prevent revenue loss from link rot and enable A/B testing of affiliate vendors.

3. **Sprint & Coast Production** - Batch filming on weekends, edit during weeknights. One deep-dive every 2 weeks + shorts during off-weeks to maintain algorithm presence without burnout.

4. **Market Bifurcation Strategy** - Serve both "Appliance Consumers" (need OrcaSlicer profiles for Bambu alternatives) and "Engineering Enthusiasts" (need Klipper/Voron guides), bridging the gap between segments.

**10-Year Trajectory:**
- **Year 1-2:** Optimize affiliates + Hardware Bridge content → $300-1k/mo
- **Year 3-4:** Launch "OrcaSlicer Expert" membership + verified profile database → $2-5k/mo
- **Year 5-7:** B2B educational licensing + brand partnerships → $10k+/mo
- **Year 10:** Potential acquisition target (profile database) or autonomous passive operation

**Reference:** `guide/Strategic Ecosystem Architecture & Revenue Acceleration Blueprint for Minimal 3DP (2025-2035).md`

---

## ✅ Recently Completed (Nov 2025)

### YouTube Popular Videos Feature
- [x] Created `fetch_youtube_popular.py` script with YouTube Data API v3 integration
- [x] Built `popular-videos.html` shortcode with thumbnail display
- [x] Added GitHub workflow (`fetch-youtube-popular.yml`) with daily automation
- [x] Converted project to use `uv` for Python dependency management
- [x] Created comprehensive setup documentation (`docs/YOUTUBE-SETUP.md`)
- [x] Tested and verified real data fetch (3 videos displaying correctly)
- [x] Integrated with email notification system (Slack removed)

### Project Organization
- [x] Created `dev/` folder for untracked local development files
- [x] Moved `ga4/` and `refs/` folders to `dev/`
- [x] Organized documentation into `docs/` folder
- [x] Moved utility scripts to `scripts/` folder
- [x] Updated `.gitignore` for clean repository structure

### Content
- [x] Created blog post: "Mastering Bed Types in OrcaSlicer" (draft)
- [x] Fixed broken content in Voron build pages (YouTube/imgproc shortcodes)

---

## 🚀 Year 1 Foundation Phase (Q4 2025 - Q4 2026)

### Priority 1: M3DP-BRIDGE Platform (Infrastructure First)

**Goal:** Build the "force multiplier" that automates affiliate management and content gap analysis.

#### A. Core M3DP-BRIDGE Application
- [ ] **Scaffold M3DP-BRIDGE app** using AI Context Block from Strategic Blueprint
  - FastAPI + PostgreSQL + HTMX stack
  - Models: Printer, Filament, SlicerProfile, AffiliateLink
  - Deploy to Railway.app ($5/mo Hobby plan)
- [ ] **Smart Link Redirect System** (Critical Path)
  - Implement `GET /go/{slug}` endpoint with async click logging
  - Create `go.minimal3dp.com` CNAME pointing to Railway
  - Replace top 50 YouTube video static links with smart links
  - **Impact:** Prevents revenue loss from out-of-stock items, enables A/B testing
- [ ] **Profile Database MVP**
  - Seed database with 20 validated Printer + Filament + SlicerProfile combos
  - Create admin interface for adding/editing profiles (HTMX forms)
  - Export downloadable JSON configs

#### B. Hybrid Infrastructure Setup
- [ ] **VPS Sidecar for Heavy Processing**
  - Provision OVH VPS Starter ($4-5/mo) for long-running scripts
  - Deploy m3dp_Orcaslicer_Script_Runner to VPS
  - Connect to Railway PostgreSQL for job queue
  - **Total OpEx Target:** $9-10/mo (Railway + VPS)

### Priority 2: "Hardware Bridge" Content Deployment

**Goal:** Execute the 4 highest-ROI content opportunities identified in Strategic Blueprint.

#### Opportunity 1: Creality K2 Plus Upgrade Series (3-Part)
- [x] **Part 1: Micro Swiss FlowTech Install** (Blog post drafted Nov 2025)
  - [ ] Add remaining 7 images to blog post
  - [ ] Film companion YouTube video
  - [ ] Ensure all affiliate links use smart link format: `go.minimal3dp.com/flowtech-k2`
- [ ] **Part 2: Rooting the K2 Plus - Real Klipper Install**
  - Script: "Now that you have the FlowTech, unlock its full performance with Klipper"
  - Dependency loop: Hardware upgrade → Software unlock
  - Affiliate: Link to BTT control board, CAN-bus kit
- [ ] **Part 3: K2 Plus OrcaSlicer Mastery**
  - Custom profile for modded K2 (FlowTech + Klipper)
  - Max Volumetric Speed tuning to 35mm³/s
  - Downloadable profile from M3DP-BRIDGE

#### Opportunity 2: Klipper Wiring Masterclass
- [ ] **"Stop Failing Prints: Ultimate Crimping Guide"**
  - Focus: JST & Dupont connectors (iCrimp tools are consistent best-sellers)
  - Production: Macro lens, extreme close-ups, show failure modes
  - Strategic Value: Evergreen reference asset—link from all future build videos
  - Affiliate: iCrimp tool sets, connector kits, BTT boards

#### Opportunity 3: Voron "Part 0" - The Shopping List
- [ ] **"Voron 2.4 Part 0: How to Source Your BOM"**
  - Walk through Bill of Materials line-by-line
  - Explain *why* to choose LDO vs Moons motors, Hiwin vs Generic rails
  - Revenue Logic: Capture affiliate cookie for entire $1000+ build before user visits other channels
  - Link all parts via M3DP-BRIDGE smart links

#### Opportunity 4: OrcaSlicer Specialty Filaments
- [ ] **"Mastering Silk & Chameleon PLA in OrcaSlicer"**
  - Settings: Retraction, temp, outer wall speeds for "shiny" effect
  - Audience purchasing FLASHFORGE Chameleon per affiliate data
  - Synergy: Promotes filament.minimal3dp.com database
  - Cross-sell: Link to flowtech hotend (better temp control)

### Priority 3: Content Production System

**Goal:** Implement "Sprint & Coast" cadence to prevent burnout.

- [ ] **Define Monthly Sprint Schedule**
  - Sprint Weekend (1 per month): Film A-roll for 2-3 videos (no editing)
  - Coast Weeknights (3-4 weeks): Edit 30min/night, write descriptions, generate thumbnails
  - Release Cadence: 1 deep-dive every 2 weeks + 1 short/quick-tip on off-weeks
- [ ] **Content Calendar Template**
  - Align Hardware Bridge topics to product launch cycles (e.g., K2 Plus series when new K2 model drops)
  - Reserve 1 slot per quarter for "Data Authority" pieces (e.g., annual "State of 3D Printing" analysis)

---

## 🔧 Immediate Action Items (Next 30 Days)

### Technical Foundation
- [ ] **Deploy M3DP-BRIDGE MVP to Railway**
  - Use AI Context Block from Strategic Blueprint as prompt
  - Get smart link redirect working (`/go/test-link`)
  - Set up PostgreSQL database with schema
- [ ] **Create go.minimal3dp.com subdomain**
  - CNAME DNS record pointing to Railway app
  - Test redirect from `go.minimal3dp.com/test` → Amazon
- [ ] **Audit Top 50 YouTube Videos**
  - Identify videos with highest affiliate potential
  - Document all Amazon links for migration to smart links
  - Prioritize videos with >10k views

### Content Execution
- [ ] **Complete K2 Plus FlowTech Blog Post**
  - Add remaining 7 images (installation steps, before/after, calibration)
  - Update affiliate links to smart link format
  - Change `draft: false` when images complete
- [ ] **Script K2 Plus Part 2 Video**
  - Outline: Why Klipper unlocks FlowTech performance
  - B-roll list: Firmware flashing, SSH access, Fluidd interface
  - Parts list: BTT board, ribbon cables, power supply considerations

### Workflow Cleanup (Carryover)
- [ ] (Optional) Manually dispatch workflows to confirm email success/failure behavior
- [ ] Add to social media promotion queue when OrcaSlicer bed types post ready

---

## 📊 Strategic Content Roadmap (Year 1-3)

### The "Hardware Bridge" Philosophy

**Core Principle:** Users don't search for "generic Klipper tutorial"—they search for "Klipper on my [specific printer]." Anchor software expertise to hardware entry points to capture high-intent search traffic.

**Content Architecture:**
1. **Hardware Entry Point** (SEO: "How to X on [Printer Model]")
2. **Software Deep Dive** (Value: "Now optimize with OrcaSlicer/Klipper")
3. **Hardware Upsell** (Monetization: "Upgrade to [Component] for even better results")

### Year 1 Content Pipeline (2025-2026)

#### Q4 2025 - Q1 2026: Foundation Content
- **Creality K2 Plus Series** (3 videos + blog posts) - *In Progress*
- **Klipper Wiring Masterclass** (1 evergreen video)
- **Voron Part 0 Shopping Guide** (1 high-value video)
- **OrcaSlicer Specialty Filaments** (1 video + blog)

#### Q2-Q3 2026: Expand Hardware Bridges
- **Elegoo Neptune 4 Upgrade Path** (untapped market per Strategic Blueprint)
- **BTT SKR Mini E3 V3.0 Deep Dive** (proven affiliate performer)
- **Definitive CAN-Bus Guide** (leverage #1 video success, expand to Ender 3/K2 Plus)

#### Q4 2026: Data Authority Content
- **Annual "State of 3D Printing" Report** (establishes thought leadership)
- **The Great Bifurcation Explained** (Appliance vs Enthusiast segments)
- **OrcaSlicer vs PrusaSlicer 2026 Comparison** (evergreen SEO asset)

### Year 2-3: Digital Product Development (2027-2028)

**Transition from "Recommending Products" → "Selling Owned Assets"**

#### "OrcaSlicer Expert" Membership (Patreon/Discord)
- **Tier 1 ($5/mo):** Access to Verified Profile Database
  - 50+ Printer + Filament combos, downloadable from M3DP-BRIDGE
  - Monthly new profile releases
- **Tier 2 ($15/mo):** "Doctor Is In" Office Hours
  - Monthly Q&A calls for troubleshooting print defects
  - Direct Discord support channel

#### Direct Digital Asset Sales
- **"Klipper Masterclass" Course** ($49 one-time)
  - Modular curriculum: Installation → Tuning → Advanced Macros
  - Includes all config files, video lessons, written guides
- **"Gold Standard" Profile Pack** ($19 one-time)
  - 10 printer profiles validated for speed + quality balance
  - Free updates for 1 year

#### Brand Partnerships (Year 3+)
- **Fixed-Rate Sponsorships:** Negotiate with filament brands for "Official Partner" status
- **Co-Branded Hardware:** Partner with LDO Motors / Micro Swiss for "Minimal 3DP Certified" kits
- **B2B Educational Licensing:** Package curriculum for Community Colleges / Maker Spaces

### Content Gap Analysis (Ongoing)

**Use M3DP-BRIDGE Dashboard to identify:**
1. **High Sales / Low Content Gaps** - Products selling well but no tutorial exists
2. **Search Volume / Competition Gaps** - High searches, few quality results
3. **Emerging Hardware Trends** - New printers with high sales but low support

**Monthly Review Questions:**
- Which affiliate products had unexpected sales spikes? (Create content explaining use case)
- Which YouTube videos had high traffic but low affiliate CTR? (Add better product recommendations)
- Which search terms are bringing traffic with high bounce rate? (Content doesn't match intent—revise)

---

## 🛠️ Technical Improvements

### Python Environment (uv)
**Status:** ✅ Implemented

Benefits realized:
- Faster CI builds with caching
- Reproducible builds via `uv.lock`
- Single `pyproject.toml` replaces `scripts/requirements.txt`

**Remaining:**
- Consider adding dev dependencies for testing/linting
- Add pre-commit hooks for Python code quality

### Hugo Build Optimization
**Current:** 1.6s build time, 218 pages

Potential improvements:
- [ ] Enable Hugo caching in CI (`--cacheDir` flag)
- [ ] Add build performance monitoring
- [ ] Consider splitting large data files if they grow

### Monitoring & Analytics
**Current Setup:**
- GA4 Data API (automated popular posts)
- YouTube Data API (automated popular videos)
- GitHub Actions workflows with email notifications

**Gaps to address:**
1. **No uptime monitoring** - Add service like UptimeRobot or Better Uptime
2. **No performance monitoring** - Consider Lighthouse CI in deploy workflow
3. **No error tracking** - Consider Sentry for client-side errors (optional, may be overkill)
4. **Quota monitoring** - Add alerts for YouTube/GA4 API quota limits

### Security & Maintenance
**Priority:** Medium

Action items:
- [ ] Rotate YouTube API key annually (set calendar reminder)
- [ ] Review GitHub secret access quarterly
- [x] Add dependabot for Hugo module updates
- [ ] Document disaster recovery plan (backup strategy)

---

## 📈 SEO & Growth Opportunities

### Cross-Promotion Strategy
Based on `dev/refs/MINIMAL3DP_APP_GUIDE.md`:

**YouTube → Website Integration:**
- ✅ Every video links back to minimal3dp.com
- ✅ Video descriptions include tool/guide links
- 🔲 Add end screens with website CTAs
- 🔲 Create "YouTube Playlist" pages on site (embed playlists with context)

**Internal Linking:**
- [x] Audit existing posts for internal link opportunities
- 🔲 Add "Related Content" sections (manual or automated)
- 🔲 Create content hub pages (e.g., "All Klipper Guides")

**External Promotion:**
- ❌ Medium automation deprecated (no API tokens) – use manual copy/paste when strategically valuable (see updated `docs/MEDIUM-SETUP.md`).
- 🔲 Reddit strategy (r/3Dprinting, r/klippers, r/VORONDesign)
- 🔲 Discord presence (Klipper, Voron communities)
- 🔲 Guest posts on other 3D printing blogs

### Email Marketing / Newsletter Strategy
**Status:** ✅ MailerLite form implemented (Nov 2025)

**Current Implementation:**
- HTML form embedded via shortcode (`newsletter-signup.html`)
- Deployed on home page and blog post templates
- Direct POST to MailerLite, no JavaScript dependencies

**Year 1 Newsletter Strategy:**
- **Threshold:** Wait until 5k monthly visitors before aggressive list building
- **Content Frequency:** Monthly digest (not weekly—matches Sprint & Coast production)
- **Value Proposition:** "Early access to new profiles + exclusive troubleshooting tips"
- **Lead Magnet Ideas:**
  - "10 Essential Klipper Macros" PDF
  - "OrcaSlicer Speed vs Quality Settings Cheat Sheet"
  - "Voron BOM Shopping Checklist" (Excel with affiliate links)

**Year 2+ Email Automation:**
- Segment by interest: "Appliance Consumer" vs "Engineering Enthusiast"
- Drip campaigns for new subscribers (7-email onboarding series)
- Affiliate product launches (e.g., "New Micro Swiss hotend just dropped")
- Exclusive membership offers for Year 3 digital products

---

## 🔄 Workflow Improvements

### Add to fetch-youtube-popular.yml:
```yaml
# Consider adding:
- Caching previous JSON to avoid quota waste if no new videos
- Error handling: Keep old data if API fails
- Include video titles in email body
- Testing: Dry-run mode for local development
```

### Add to fetch-popular.yml:
```yaml
# Consider adding:
- Combine with YouTube fetch (single daily run?)
- Add website vs YouTube performance comparison
- Generate "trending" vs "evergreen" content reports
```

---

## 💡 Year 2-5 Feature Roadmap

### Phase 2A: Enhanced Tools (Year 2 - 2027)

**Priority 1: Profile Download Integration**
- **Integrate M3DP-BRIDGE with m3dp-uip calculators**
  - After user completes Flow Calibration → Offer downloadable validated profile
  - Button: "Get the Minimal 3DP Verified Profile for [Detected Printer]"
  - Drives membership signups (free profiles = teaser, full database = paid)

**Priority 2: Interactive Klipper Configurator**
- Web-based visual config builder
- Template selection: Ender 3, Voron 2.4, K2 Plus, Custom
- Drag-and-drop sensor placement, stepper direction toggles
- Real-time syntax validation, one-click download
- **Revenue:** Affiliate links to recommended control boards based on config complexity
- **Effort:** High (3-6 months part-time) but high strategic value

**Priority 3: Filament Drying Calculator**
- Temperature/time recommendations by material + humidity
- **Data Authority Play:** Aggregate user results to build "crowd-sourced" optimal settings
- Revenue: Affiliate links to filament dryers (Sunlu, PrintDry)

### Phase 2B: Community Monetization (Year 3 - 2028)

**OrcaSlicer Expert Discord (Paid Community)**
- **Tier 1 ($5/mo):** Access to Verified Profile Database
- **Tier 2 ($15/mo):** Live support + Monthly Q&A office hours
- **Tier 3 ($50/mo):** 1-on-1 build consultations (limit to 10 members)

**Moderation Strategy:** Nights/weekends only—no real-time expectation. "Async-first" community.

### Phase 3: B2B Pivot (Year 5+ - 2030+)

**Educational Licensing**
- Package "Klipper Masterclass" as workforce development curriculum
- Target: Community Colleges, Maker Spaces, Technical High Schools
- Pricing: $500-2000 per institution (one-time or annual)
- **Proof of Concept:** Start with 1 local pilot program before scaling

**Distributed Manufacturing Certification**
- The M3DP-BRIDGE profile database evolves into certification authority
- Print farms pay for "Minimal 3DP Certified" badge proving they can hit specific tolerances
- **Market Opportunity:** As 3D printing moves to distributed production, quality assurance becomes critical

### Backlog: Lower Priority Tools

1. **Print Time Estimator** (Nice-to-have, low differentiation)
2. **Support Material Calculator** (Niche use case)
3. **User Accounts** (Only if 100+ users request saved settings)
4. **Community Forum** (Discord sufficient until 10k+ monthly visitors)

---

## 📝 Documentation Needs

### User-Facing
- [x] YouTube API setup guide ✅
- [x] SMTP notification setup ✅
- [ ] "How to Use This Site" guide
- [ ] FAQ page expansion
- [ ] Calculator user guides (embed in tools)

### Developer-Facing
- [x] Python environment setup (uv) ✅
- [x] Workflow documentation ✅
- [ ] Hugo customization guide
- [ ] Deployment process documentation
- [ ] API documentation (if exposing endpoints)

---

## 🎯 Success Metrics

### Track Monthly:
- Unique visitors (GA4)
- Popular page views (top 10)
- YouTube → Website conversion rate
- Affiliate click-through rate
- Affiliate revenue (Amazon Associates)
- Email list growth (when implemented)
- Popular videos refresh accuracy

### Track Quarterly:
- Organic search traffic growth
- Domain authority / backlinks
- YouTube subscriber growth correlation with site traffic
- Tool usage statistics (calculator pageviews)
- Content ROI (time invested vs traffic generated)

---

## 📌 Strategic Design Decisions & Context

### Core Philosophy Shifts (Strategic Blueprint)

**From "Linear Effort-for-Income" → "Asynchronous Value Generation"**
- Old Model: Make video → Get views → Earn $0.50 CPM
- New Model: Build system (M3DP-BRIDGE) → Automate affiliate optimization → Revenue grows without new content

**From "Content Creator" → "Data Authority"**
- Old Identity: Entertainment-driven, personality-focused
- New Identity: Technical specificity, validated data, problem-solving authority
- **Moat:** Deep technical knowledge (Klipper firmware, OrcaSlicer optimization) competitors can't easily replicate

**Market Positioning: The "Translator"**
- Bridge between "Appliance Consumers" (want reliability) and "Engineering Enthusiasts" (want control)
- Unique value: Speak both languages (OrcaSlicer simplicity + Klipper complexity)

### Technical Decisions

**Why M3DP-BRIDGE + VPS Hybrid Architecture?**
- Railway.app ($5/mo): Easy git-push-deploy for web apps, managed PostgreSQL
- VPS Sidecar ($4-5/mo): Handles 10+ hour script runs without burning Railway credits
- **Total OpEx:** $9-10/mo (within $5-20 constraint)
- **Alternative Rejected:** Single Railway deployment would cost $50+/mo for heavy processing

**Why FastAPI + HTMX over React SPA?**
- No separate build step for frontend = faster iteration
- HTMX provides dynamic UX without client-side state complexity
- Perfect for solo weekend developer with limited time

**Why PostgreSQL + JSONB for profiles?**
- Relational for Printer/Filament entities (structured queries)
- JSONB for SlicerProfile configs (flexible schema, no migrations when OrcaSlicer adds new settings)

**Why Smart Links (go.minimal3dp.com) over direct Amazon?**
- Prevents revenue loss when products go out-of-stock (auto-update link targets)
- A/B test vendors (Amazon 3% vs Micro Swiss direct 5% commission)
- Click analytics show which content drives purchases

### Content Production Decisions

**Why "Sprint & Coast" over Consistent Daily?**
- Constraint: Part-time creator (nights/weekends only)
- Burnout Risk: Daily grind unsustainable for 10-year vision
- **Sprint:** 1 weekend/month for filming A-roll (2-3 videos)
- **Coast:** Weeknights for low-energy editing (30min/night)
- Result: 1 deep-dive every 2 weeks + shorts on off-weeks

**Why Hardware Bridge over Generic Tutorials?**
- SEO: Users search "How to X on [Printer Model]" not "Generic Klipper Guide"
- Monetization: Capture affiliate cookie at point of hardware purchase decision
- Differentiation: Most competitors do either hardware reviews OR software tutorials—not both integrated

### Known Limitations & Constraints

1. **Time:** Nights/weekends only—no real-time community moderation or daily uploads
2. **Budget:** $5-20/mo hosting limit—no expensive managed services
3. **Scale:** No database until M3DP-BRIDGE deployed—all data in flat JSON files
4. **API Quotas:** YouTube API 10k units/day, GA4 rate limits
5. **Content Volume:** Cannot compete on quantity—must win on depth + technical authority

### When to Revisit Strategies

**Pivot from Affiliate to Direct Sales:**
- When monthly revenue hits $1,000 (affiliate optimized)
- When email list exceeds 1,000 subscribers (audience to sell to)
- When 50+ users request "downloadable configs" (product-market fit signal)

**Launch Membership/Patreon:**
- When producing 2 videos per week consistently (proof of sustainability)
- When Discord server exceeds 500 active members (community critical mass)
- When validated profile database exceeds 50 entries (enough value to charge)

**Pursue B2B Educational Licensing:**
- When annual revenue exceeds $50k from consumer channels (stability to invest sales effort)
- When curriculum is packaged as standalone product (not dependent on Mike's time)
- When 1 pilot program succeeds (proof of concept)

---

## 🏁 Next Steps (Sprint 1 - December 2025)

### Week 1: Foundation Infrastructure
1. **Deploy M3DP-BRIDGE MVP** (4-6 hours)
   - Use Strategic Blueprint AI Context Block to scaffold app
   - Deploy to Railway.app, set up PostgreSQL
   - Get smart link redirect working: `go.minimal3dp.com/test` → Amazon
2. **Create DNS Records** (15 min)
   - CNAME: `go.minimal3dp.com` → Railway app
   - Test redirect from multiple devices

### Week 2: Smart Link Migration
3. **Audit Top 10 YouTube Videos for Link Migration** (2 hours)
   - Identify videos with >10k views + affiliate links
   - Document current Amazon ASINs
   - Create smart links in M3DP-BRIDGE dashboard
4. **Update Video Descriptions** (1 hour)
   - Replace static Amazon links with `go.minimal3dp.com/[slug]`
   - Add tracking parameters to measure CTR

### Week 3-4: Content Execution
5. **Complete K2 Plus FlowTech Blog Post** (3 hours)
   - Shoot remaining 7 images (installation steps, calibration results)
   - Update all affiliate links to smart link format
   - Publish: Change `draft: false`
6. **Script K2 Plus Part 2 Video** (2 hours)
   - Outline: "Unlocking FlowTech Performance with Real Klipper"
   - B-roll shot list: Firmware flashing, SSH setup, Fluidd interface tour
   - Parts list: BTT board recommendations, wiring requirements

### Carryover Tasks
- [ ] Test popular videos section on production (after deploy)
- [ ] Add OrcaSlicer bed types post to social media queue when ready

---

## 📚 Reference Documents

### Strategic Planning (2025-2035)
- **`guide/Strategic Ecosystem Architecture & Revenue Acceleration Blueprint for Minimal 3DP (2025-2035).md`** - ⭐ **Master Strategy Document**
  - 10-year roadmap: $200/mo → $10k+/mo
  - M3DP-BRIDGE technical architecture
  - "Hardware Bridge" content model
  - Sprint & Coast production cadence
  - AI Context Block for platform development

### Tactical Content & Analysis
- `dev/refs/Data-Driven Content Strategy Report for Minimal 3DP.md` - Audience behavior + affiliate sales analysis
- `dev/refs/MINIMAL3DP_APP_GUIDE.md` - Brand identity and architecture standards
- `dev/refs/Minimal 3DP_ A Comprehensive Brand Specification...md` - Core brand pillars

### Technical Documentation
- `docs/YOUTUBE-SETUP.md` - YouTube API integration guide
- `docs/SMTP-SETUP.md` - Email notification setup
- `docs/MEDIUM-SETUP.md` - Manual Medium cross-post guide (automation deprecated)
- `docs/RECOMMENDATIONS.md` - Historical SEO recommendations (archived)
- `docs/SHORTCODES-AND-PARTIALS.md` - Comprehensive shortcode and partial reference
- `.github/copilot-instructions.md` - AI agent guidance for this repo

### Key Decisions Log
- **Revenue Model:** Affiliate optimization (Year 1) → Digital products (Year 2-3) → B2B licensing (Year 5+)
- **Content Strategy:** Hardware Bridge approach (software tutorials anchored to specific printers)
- **Production Schedule:** Sprint & Coast (batch filming weekends, edit weeknights)
- **Infrastructure:** Railway.app ($5/mo) + VPS ($4-5/mo) = $9-10/mo total
- **Tech Stack:** FastAPI + PostgreSQL (JSONB) + HTMX (no React complexity)

---

**Maintained by:** GitHub Copilot + Mike Wilson  
**Review Frequency:** Monthly or after major strategic milestones  
**Strategic Alignment Check:** Quarterly review against 10-year blueprint
