# Deployment: Railway.app Monorepo Guide

This repository is a **Monorepo** containing two distinct services. You will deploy them as two separate services within a single Railway Project.

| Service | Path | Type | Deployment Method |
| :--- | :--- | :--- | :--- |
| **Site (Static)** | `/` | Static Site | Hugo Build (`public/`) |
| **App (Bridge)** | `/m3dp-bridge` | Web Service | Dockerfile (FastAPI + Postgres) |

---

## Service 1: Minimal3DP Site (Stateless)

This is the main documentation and blog.

1.  **Add Service > GitHub Repo**
    *   Select `minimal3dp/minimal3dp.github.io`
2.  **Settings > General**
    *   **Root Directory:** `/` (Default)
3.  **Settings > Build**
    *   **Builder:** Static Site
    *   **Build Command:** `hugo --gc --minify`
    *   **Output Directory:** `public`
4.  **Domain:** `minimal3dp.com` (or Railway provided domain)

---

## Service 2: M3DP-BRIDGE (Application)

This is the "Smart Link" redirector and backend dashboard.

### A. Database (PostgreSQL)
1.  **Add Service > Database > PostgreSQL** in the same project.
2.  Wait for it to deploy.
3.  Copy the `DATABASE_URL` from the "Connect" tab.

### B. Web Service (FastAPI)
1.  **Add Service > GitHub Repo**
    *   Select `minimal3dp/minimal3dp.github.io` (Again)
2.  **Settings > General**
    *   **Root Directory:** `/m3dp-bridge`  <-- **CRITICAL**
3.  **Settings > Build**
    *   **Builder:** Dockerfile
        *   Railway should auto-detect the `Dockerfile` in `/m3dp-bridge`.
4.  **Settings > Environment Variables**
    *   `DATABASE_URL`: Paste the Postgres URL from Step A.
    *   `PORT`: `8000`
5.  **Domain:** `go.minimal3dp.com` (or `m3dp-bridge-production.up.railway.app`)

### C. Verify Bridge
1.  Visit `https://YOUR-APP-URL/health` -> Should return `{"status": "ok"}`.
2.  Visit `https://YOUR-APP-URL/dashboard` -> Should show the Affiliate Link table.

---

## Local Development (Docker Compose)
To run the full stack locally (excluding the static site):

```bash
cd m3dp-bridge
docker-compose up --build
```

Access Dashboard at: `http://localhost:8000/dashboard`
