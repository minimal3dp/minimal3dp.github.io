# Minimal 3DP

Based on Docsy template

## Update Template

```bash
hugo mod get -u github.com/google/docsy@v0.12.0
```

## Run in Dev

```bash
hugo server -D
```

## Run in Prod

```bash
hugo
```

## Docs

- Copilot usage guidelines: see `.github/copilot-instructions.md` for repo-specific conventions and prompt efficiency tips.
- Setup guides: see `docs/` folder for SMTP, recommendations, and archived notes.

## Notifications (Slack)

Add a repository secret `SLACK_WEBHOOK_URL` containing a Slack Incoming Webhook URL (create one in your Slack workspace under Apps > Incoming Webhooks). The `fetch-popular.yml` and `deploy-site.yaml` workflows will:

- Post a ✅ success message with commit short SHA and run id
- Post a 🚨 failure message including a direct run URL

If the secret is absent the steps auto-skip safely.

### Creating the Secret
1. Slack: Install "Incoming Webhooks" app, choose channel, copy webhook URL.
2. GitHub: Settings > Secrets and variables > Actions > New repository secret.
3. Name: `SLACK_WEBHOOK_URL`, Value: (paste URL).

### Testing
Trigger a build (push to `main` or run the Popular Posts workflow) and confirm message in Slack channel.

## Notifications (Email)

Email notifications are now implemented for both workflows (success + failure). Add these repository secrets:

- `SMTP_SERVER` (e.g. smtp.sendgrid.net)
- `SMTP_PORT` (e.g. 587)
- `SMTP_USERNAME` (SMTP auth user)
- `SMTP_PASSWORD` (SMTP auth password/token)
- `FROM_EMAIL` (sender address)
- `TO_EMAIL` (comma-separated recipients)

On success you receive a summary; on failure an alert with run URL. If any secret is missing the email step is skipped safely.

Detailed provider-specific instructions: see `docs/SMTP-SETUP.md`.

### One-click SMTP Smoke Test
- Go to GitHub → Actions → "SMTP Smoke Test" → Run workflow.
- Optionally set recipients in the input; otherwise it uses the `TO_EMAIL` secret.
- Requires these secrets to be set: `SMTP_SERVER`, `SMTP_PORT`, `SMTP_USERNAME`, `SMTP_PASSWORD`, `FROM_EMAIL`, `TO_EMAIL`.
