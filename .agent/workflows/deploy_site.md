---
description: "Deploy changes to production"
---
# Workflow: Deploy Site

1.  **Pre-Flight Check**:
    -   Run `hugo` to build locally and check for errors.
    -   Run `npx html-validate public/` (if available) or check console for 404s.

2.  **Commit**:
    -   Ensure `AGENTS.md` and `TODO.md` are up to date.
    -   Commit with semantic message (e.g., `feat: add input shaping guide`).

3.  **Push**:
    ```bash
    git push origin main
    ```

4.  **Verification**:
    -   Check Railway dashboard for deployment success.
    -   Visit live site to verify changes.
