# Deploying Minimal3DP (Hugo + Docsy) to Railway

This guide walks through deploying the static site to Railway.app. Two reliable approaches are provided:

- Approach A (Recommended): Railway Static Site service with Hugo build
- Approach B (Alternative): Dockerfile + NGINX container serving built `public/`

## Prerequisites
- GitHub repo connected (minimal3dp/minimal3dp.github.io)
- Hugo Extended installed locally for testing (`hugo version` shows "extended")
- Basic Railway account set up

## Verify Local Build
```zsh
hugo --gc --minify
open public/index.html
```
Ensure `public/` is generated without errors.

---

## Approach A: Railway Static Site (Recommended)
Railway's Static Sites service can build and serve Hugo output directly.

1) Create a new Railway project
- In Railway UI → "New Project" → "Deploy from GitHub"
- Select `minimal3dp/minimal3dp.github.io`

2) Add a Static Site service
- Choose "Static Site"
- Set Build Command: `hugo --gc --minify`
- Set Output Directory: `public`

3) Configure environment
- No start command needed for Static Site
- If your site uses environment secrets for scripts, keep them in GitHub Actions; Railway only needs to run the build

4) Deploy
- Trigger a deployment from the UI
- On success, Railway hosts the contents of `public/`

5) Auto-deploy from GitHub
- Enable "Auto Deploy" on push to `main`

6) Custom domain (optional)
- Add domain in Railway → set up DNS (CNAME to Railway domain)

### Notes
- If Railway’s build image doesn’t include Hugo, Static Sites still works by using Nixpacks. Most setups detect and run `hugo` correctly.
- If build fails due to missing Hugo, use Approach B.

---

## Approach B: Dockerfile + NGINX (Alternative)
Use a multi-stage Docker build to compile the site with Hugo Extended, then serve with NGINX.

### Sample Dockerfile (add to repo root)
```Dockerfile
# Stage 1: Build with Hugo Extended
FROM klakegg/hugo:0.152.2-ext-alpine AS builder
WORKDIR /site
COPY . .
RUN hugo --gc --minify

# Stage 2: Serve with nginx
FROM nginx:alpine
COPY --from=builder /site/public /usr/share/nginx/html
# Simple default nginx config
RUN rm /etc/nginx/conf.d/default.conf
COPY deploy/nginx.conf /etc/nginx/conf.d/default.conf
EXPOSE 8080
CMD ["nginx", "-g", "daemon off;"]
```

### Sample NGINX config (put in `deploy/nginx.conf`)
```nginx
server {
    listen 8080;
    server_name _;

    root /usr/share/nginx/html;
    index index.html;

    location / {
        try_files $uri $uri/ /index.html;
    }

    location ~* \.(css|js|svg|png|jpg|jpeg|gif|ico)$ {
        expires 7d;
        add_header Cache-Control "public, max-age=604800";
        try_files $uri =404;
    }
}
```

### Build & test locally (optional)
```zsh
docker build -t minimal3dp-site .
docker run -p 8080:8080 minimal3dp-site
open http://localhost:8080
```

### Deploy to Railway with Dockerfile
1) Push Dockerfile and `deploy/nginx.conf` to `main`
2) In Railway → New Service → "Deploy from GitHub" → select the repo
3) Railway detects the Dockerfile and builds
4) Service runs on port 8080; Railway will route traffic automatically

### Notes
- Dockerfile ensures Hugo Extended is present and avoids build-image variance
- NGINX port uses 8080 to avoid env-var templating; Railway routes properly

---

## CI/CD Considerations
- Keep GitHub Actions for data-fetch scripts and gh-pages deploy if you still use it
- For Railway, enable auto-deploy on push to `main` and rely on Railway builds
- You can disable gh-pages deployment workflow once Railway is primary (optional)

## Rollback / Re-deploy
- Use Railway deployments panel to roll back to a previous successful build
- Re-deploy from UI or push a new commit to `main`

## Troubleshooting
- Build fails: run `hugo --gc --minify` locally; fix errors; retry
- Missing Hugo in build image: switch to Dockerfile approach
- 404s on deep links: ensure NGINX `try_files` rule is present (Approach B) or Static Sites are configured properly

## Checklist
- [ ] Local `hugo --gc --minify` works
- [ ] Railway Static Site configured (`Build: hugo --gc --minify`, `Output: public`)
- [ ] Auto-deploy enabled on push to `main`
- [ ] Optional: Dockerfile + `deploy/nginx.conf` committed for containerized deploy
- [ ] Domain configured (optional)
