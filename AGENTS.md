# AGENTS.md: Minimal 3DP Ecosystem Rules

## 1. 🧠 Core Directive (The "Sprint & Coast" Law)
- **Review First:** Before generating code, check the user's current energy state (Sprint vs. Coast).
- **Scope Control:** REJECT any request that adds new features during a "Coast" (Weeknight) phase. [cite_start]Only "Sprint" (Weekend) allows new logic.
- **Anti-Distraction:** If the user changes topics (e.g., from "writing blog" to "redesigning logo"), INTERRUPT them. [cite_start]Ask: "Does this align with the current Sprint goal?".

## 2. 🛠 Tech Stack & Standards
- [cite_start]**Platform:** Hugo (Static Site) + Docsy Theme.
- **Deployment:** Railway + Google Antigravity.
- **Styling:** TailwindCSS (via `m3dp-design-system`). DO NOT use inline styles or raw CSS files.
- **Affiliates:** ALL product links must use the `m3dp-bridge` format (e.g., `{{< affiliate-link id="btt-manta" >}}`). NEVER use raw Amazon links.

## 3. 📂 Project Structure
- `content/blog/`: Technical tutorials.
- `layouts/partials/`: HTML components.
- `static/`: Images and compiled assets.
- `AGENTS.md`: THIS FILE. Read it.

## 4. 🛑 "Hardware Bridge" Content Rules
- **The Hook:** Every post MUST solve a specific software problem (e.g., "Input Shaping").
- **The Bridge:** Every solution MUST link to a hardware component (e.g., "ADXL345 Sensor").
- **Tone:** "Detailed and Boring." No fluff. [cite_start]Numbered lists for steps.

## 5. 🤖 Agent Configuration
- **Location:** `.agent/` directory contains specific personas and workflows.
- **Active Agents:**
    -   `@Orchestrator`: Project Manager (.agent/rules/orchestrator.md)
    -   `@Content_Ops`: Content Creator (.agent/rules/content_ops.md)
    -   `@Strategy_Gen`: Planner (.agent/rules/strategy_gen.md)
- **Workflows:** See `.agent/workflows/` for standard operating procedures.

## 6. ✅ Definition of Done
- Code compiles without warnings.
- Affiliate links are verified against the `m3dp-bridge` database.
- No new technical debt created (no new libraries without approval).