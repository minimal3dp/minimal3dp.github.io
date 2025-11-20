# Minimal 3DP TODO & Recommendations

**Last Updated:** November 19, 2025  
**Status:** Post YouTube Popular Videos Implementation

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

## 🔧 Immediate Action Items (High Priority)

### 1. GitHub Workflow Cleanup
- [x] Remove Slack; switch to email-only notifications (documented in `README.md`)
- [x] Replace conditional secret checks with config detection output
- [ ] (Optional) Manually dispatch workflows to confirm email success/failure behavior

### 2. Update Popular Videos Section - Static Fallback
- [x] Add 3–4 curated evergreen popular videos as fallback
- [x] Pull from existing popular posts data as interim solution (choose approach)

### 3. Add YouTube Thumbnail Optimization
- [x] Add `loading="lazy"`
- [x] Add `width` and `height` attributes
- [x] Add blur placeholder removal on load
- [ ] Convert thumbnails to WebP via Hugo image processing
- [ ] Generate very low-res base64 thumb for LQIP (optional)

### 4. Publish OrcaSlicer Bed Types Post
- [x] Review and edit content (`content/blog/posts/orcaslicer-bed-types/index.md`)
- [x] Add featured image
- [x] Change `draft: true` to `draft: false`
- [ ] Add to social media promotion queue
- [x] Create accompanying YouTube video (reference Data-Driven Strategy doc)

---

## 📊 Content Strategy Recommendations

### Based on Data-Driven Analysis (`dev/refs/Data-Driven Content Strategy Report`)

**Top 6 Video/Blog Topics (Ranked by Audience Demand):**

1. **Creality K2 Plus Upgrade Series (3-part series)**
   - Part 1: All-Metal Extruder Gear Kit installation
   - Part 2: Nozzle Wiper Module upgrade
   - Part 3: Klipper installation + OrcaSlicer profile
   - **Why:** Direct affiliate sales data shows high interest (4× gear kit purchases in 2025)
   - **Revenue potential:** High (hardware + affiliate links)

2. **Klipper Wiring Masterclass: Crimpers, JST & Dupont**
   - Hands-on tutorial for custom wiring harnesses
   - Feature iCrimp tools and connector kits (consistent best-sellers)
   - **Why:** Addresses proven high-friction task (tool purchases confirm)
   - **Cross-sell:** BTT control boards (also best-sellers)

3. **Definitive Klipper CAN-Bus Guide (Beyond Voron)**
   - Comprehensive guide for Ender 3 / K2 Plus
   - **Why:** Leverage #1 performing video topic (Voron CAN guide) for broader audience
   - **Revenue potential:** Very high (proven with $19.34 revenue on Voron version)

4. **OrcaSlicer Deep Dive: Mastering Specialty Filaments**
   - Focus on FLASHFORGE Chameleon & Silk PLA (audience purchasing these)
   - Settings optimization for visual effects
   - **Why:** Combines top-performing category (OrcaSlicer) with purchase behavior

5. **"Part 0" Voron Build: Ultimate Component Sourcing Guide**
   - Complete shopping list with affiliate links
   - **Why:** Capture audience at beginning of build journey
   - **Revenue potential:** High (multiple component purchases)

6. **Ultimate BTT SKR Mini E3 V3.0 Installation (Klipper Edition)**
   - Start-to-finish board swap + Klipper config
   - **Why:** One of most consistent affiliate purchases (2024-2025)
   - **Entry point:** Perfect for Klipper beginners

**Implementation Priority:**
1. K2 Plus Series (immediate affiliate opportunity)
2. Klipper Wiring (fills content gap, high engagement potential)
3. CAN-Bus Guide (proven revenue driver)
4. Others as time permits

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
- 🔲 Reddit strategy (r/3Dprinting, r/klippers, r/VORONDesign)
- 🔲 Discord presence (Klipper, Voron communities)
- 🔲 Guest posts on other 3D printing blogs

### Email Marketing
**Status:** Not implemented

Potential:
- Newsletter signup on high-traffic pages
- Weekly/monthly digest of new tools/guides
- Exclusive content for subscribers
- Affiliate promotion channel

**Implementation:**
- Start with simple Mailchimp/ConvertKit integration
- Gate downloadable resources (Klipper configs, cheat sheets)
- Build list before creating complex automations

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

## 💡 Future Features (Backlog)

### Tools to Consider
Based on audience needs:

1. **Klipper Config Generator**
   - Web tool for generating printer.cfg files
   - Templates for popular printers (Ender 3, Voron, K2 Plus)
   - Revenue: Affiliate links to control boards

2. **Print Time Estimator**
   - Compare slicer settings impact on print time
   - Show time/quality tradeoffs
   - Revenue: Affiliate links to faster printers/hotends

3. **Filament Drying Calculator**
   - Temperature/time recommendations by filament type
   - Revenue: Affiliate links to filament dryers

4. **Support Material Calculator**
   - Estimate support material waste and cost
   - Revenue: Affiliate links to support-friendly filaments

### Platform Enhancements

1. **User Accounts (far future)**
   - Save calculator settings
   - Store favorite content
   - Personalized recommendations
   - **Caveat:** Adds complexity, only if audience demands it

2. **Interactive Klipper Configurator**
   - Visual config builder
   - Real-time syntax validation
   - One-click download
   - **Effort:** High, but high value for audience

3. **Community Forum**
   - Q&A platform (self-hosted Discourse?)
   - Alternative: Discord integration
   - **Decision:** Validate demand first (Discord poll?)

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

## 📌 Notes & Context

### Design Decisions Made

**Why uv instead of pip/conda?**
- 10-100× faster than pip
- Deterministic builds (lock file)
- Better caching in CI/CD
- Single file configuration

**Why data/ + static/data/ for JSON?**
- `data/` = Hugo can access via `site.Data`
- `static/data/` = Client-side JS can fetch
- Workflow copies data → static for both use cases

**Why not use YouTube Analytics API?**
- Requires OAuth (complex setup)
- Data API v3 sufficient for view counts
- Keeps implementation simple
- API key auth easier to manage

### Known Limitations

1. **YouTube API quota:** 10k units/day (script uses ~200 per run)
2. **GA4 Data API:** Limited to properties user has access to
3. **Hugo build time:** Scales linearly with content (acceptable for now)
4. **No database:** All data in flat files (fine for current scale)

### When to Revisit Decisions

**Move tools to subdomains?**
- When a single tool exceeds 10k monthly users
- When tool needs separate tech stack (e.g., React app)
- When SEO data shows subdomain would benefit

**Add user accounts?**
- When at least 100 users request saved settings
- When building tools that require state (config builders)
- Not before validating demand

**Implement email marketing?**
- When monthly visitors exceed 5k
- When 50+ users request newsletter
- When content production is consistent (2× per week)

---

## 🏁 Next Steps (This Week)

1. **Fix workflow linting errors** (30 min)
2. **Copy youtube_popular.json to static/** for local builds (5 min) ✅
3. **Review and publish OrcaSlicer bed types post** (1 hour)
4. **Plan K2 Plus video/post** (reference data-driven doc) (2 hours)
5. **Update README** with YouTube feature (10 min)
6. **Test popular videos section** on production (after deploy) (15 min)

---

## 📚 Reference Documents

- `dev/refs/Data-Driven Content Strategy Report for Minimal 3DP.md` - Audience behavior analysis
- `dev/refs/MINIMAL3DP_APP_GUIDE.md` - Brand identity and architecture standards
- `dev/refs/Minimal 3DP_ A Comprehensive Brand Specification...md` - Core brand pillars
- `docs/YOUTUBE-SETUP.md` - YouTube API integration guide
- `docs/SMTP-SETUP.md` - Email notification setup
- `docs/RECOMMENDATIONS.md` - Historical SEO recommendations (archived)
- `docs/SHORTCODES-AND-PARTIALS.md` - Comprehensive shortcode and partial reference
- `.github/copilot-instructions.md` - AI agent guidance for this repo

---

**Maintained by:** GitHub Copilot + Mike Wilson  
**Review Frequency:** Monthly or after major feature additions
