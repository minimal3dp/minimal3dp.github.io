# Deploying Minimal3DP Site to Railway

This guide covers deploying the **Static Site** (Hugo) to Railway.app.

> **Note:** The `m3dp-bridge` application lives in a separate repository and is deployed separately.

## step 1: Prepare Railway

1.  Log in to [Railway.app](https://railway.app/).
2.  Click **New Project** > **Deploy from GitHub repo**.
3.  Select `minimal3dp/minimal3dp.github.io`.

## Step 2: Configure Service

1.  Click on the new service card to open **Settings**.
2.  Go to the **Settings** tab.
3.  Scroll to **Build**.
    *   **Builder:** Set to **Railpack** (the successor to Nixpacks) or **Static Site**.
        *   *Note:* Nixpacks is deprecated. Railpack is the new default standard.
    *   **Build Command:** `npm install && npm run build`
        *   *Why?* The build agent needs to install the dependencies (including Hugo) before running the build script.
    *   **Output Directory:** `public`
4.  **Root Directory:** `/` (Default).

## Step 3: Domain & Networking

1.  Go to the **Settings** tab > **Networking**.
2.  Click **Generate Domain** (to get a `*.up.railway.app` URL for testing).
3.  (Optional) Click **Custom Domain** to connect `minimal3dp.com`.
    *   Railway will provide DNS records (CNAME) to add to your registrar.

## Step 4: Verify Environment

Since this is a static site, you generally do *not* need Environment Variables unless your build scripts use them (e.g., Hugo secrets).

1.  Go to **Variables**.
2.  Ensure no conflicting variables are set.

## Troubleshooting

*   **Build Fails:** Check the **Deploy Logs**.
    *   If it says `hugo: command not found`, ensure you are using `npm run build` (which uses the local `hugo-extended` from `node_modules`).
*   **Styles Missing:** Ensure `Output Directory` is exactly `public`.

---

## Local Build Verification
Before pushing, you can verify the build command works locally:

```bash
npm install
npm run build
# Check if public/ folder is generated
```
