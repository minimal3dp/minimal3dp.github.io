# Agent Protocols & System Constraints

## 🛑 Mission Lock
**Primary Objective:** Build the **"Hardware Bridge"** — connecting mass-market appliance consumers to engineering deep-dives.
**Constraint:** All generated content, code, or strategy MUST serve one of two funnels:
1.  **Validated Data Ecosystem:** Tools that replace guesswork (Calculators, Slicer Profiles, Filament Tuning).
2.  **Deep Dive Funnel:** High-technical-depth content that establishes authority (YouTube -> Website).

If a task does not fit these categories, **STOP** and request `Orchestrator` verification.

---

## 🏗️ Project Structure & Subdomain Mapping
Agents must strictly adhere to this mapping to prevent path hallucination.

| Subdomain | Physical Path | Purpose |
| :--- | :--- | :--- |
| **Main Site** (`minimal3dp.com`) | `content/blog/`, `content/projects/`, `content/_index.md` | General tutorials, project showcases, landing page. |
| **Calc** (`calc.minimal3dp.com`) | `content/tools/`, `content/klipper-calibration/` | Physics-based calculators and interactive calibration guides. |
| **Filament** (`filament.minimal3dp.com`) | `content/filament/` *(To Be Created)* | Tuning databases and material-specific guides. |
| **Settings** (`settings.minimal3dp.com`) | `content/settings/` *(To Be Created)* | Slicer profiles (OrcaSlicer/PrusaSlicer) and config bundles. |
| **Assets** | `static/`, `assets/scss/` | Images, global styles, and SCSS. |

---

## 🛡️ Operational Dos & Don'ts

### Dos (Enforced)
1.  **Hugo Strict Mode:** All Hugo server commands must run with `-D` (Drafts) and `--panicOnWarning`. Zero tolerance for template warnings.
2.  **Atomic Commits:** Changes to `content/` and `assets/` must be committed separately.
3.  **Validate Links:** All internal links must use Hugo `ref` or `relref` shortcodes, not raw URLs.
4.  **Hardware Accuracy:** When detailing specs for **Voron** or **Bambu Lab** printers, verify against official documentation or the `memory/hardware_specs.md` file (if exists). **DO NOT GUESS.**

### Don'ts (Forbidden)
1.  **No Global CSS Changes:** Do not modify `assets/scss/_styles_project.scss` or `m3dp-design-system` without explicit **Human Approval** via the Orchestrator.
2.  **No Navigation Shifts:** Do not alter `hugo.toml` menu structures without a dedicated "Navigation Reshuffle" task.
3.  **No Unvalidated Metrics:** Do not invent "Scores" or "Ratings" for printers/filament without a defined formula in `dev/refs/`.

---

## 🚦 Safety Protocols
-   **CSS/JS Modifications:** Any change to `.scss` or `.js` files in `assets/` requires a `view_file` verification of the `hugo server` output (or browser screenshot) before task completion.
-   **New Sections:** creating a new top-level folder in `content/` requires User Approval.
