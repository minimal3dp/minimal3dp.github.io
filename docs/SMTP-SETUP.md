# SMTP Setup Guide for Workflow Email Notifications

This guide walks through configuring SMTP credentials and repository secrets so the GitHub Actions email steps in `fetch-popular.yml` and `deploy-site.yaml` can send success/failure notifications.

---
## 1. Choose a Provider
Recommended providers (stable, API key based):

| Provider  | SMTP Server                           | Port(s) | Username Convention         | Notes |
|-----------|----------------------------------------|---------|-----------------------------|-------|
| SendGrid  | `smtp.sendgrid.net`                   | 587, 25 | `apikey` (literal string)   | Use API Key as password. Supports STARTTLS. |
| Mailgun   | `smtp.mailgun.org`                    | 587, 25 | Full Mailgun login/email    | Region-specific if using EU domains. |
| AWS SES   | `email-smtp.<region>.amazonaws.com`    | 587, 465| Generated SMTP username     | Must create SMTP creds from IAM/SES console. |
| Postmark  | `smtp.postmarkapp.com`                | 587      | POSTMARK API key            | High deliverability; use server API key as password. |
| Brevo (Sendinblue) | `smtp-relay.brevo.com`        | 587, 465| Brevo login or API key      | Enable SMTP under account settings. |
| Gmail (App Password) | `smtp.gmail.com`           | 587, 465| Gmail address               | Requires 2FA + App Password. Not ideal for production volume. |

Avoid using personal mailbox providers for production monitoring – use a dedicated transactional email service (SendGrid/Postmark/Mailgun/SES) for reliability and deliverability.

---
## Mailgun Quick Setup (minimal3dp.org)

If you're using Mailgun with sender `minimal3dp@minimal3dp.org`:

- SMTP server: `smtp.mailgun.org` (EU region: `smtp.eu.mailgun.org`)
- Port: `587`
- Username: Mailgun SMTP login for your domain (often `postmaster@minimal3dp.org`)
- Password: The SMTP password shown/created in Mailgun for that login
- From: `minimal3dp@minimal3dp.org` (ensure the domain is verified in Mailgun)

Add these GitHub Actions secrets:

- `SMTP_SERVER = smtp.mailgun.org`
- `SMTP_PORT = 587`
- `SMTP_USERNAME = postmaster@minimal3dp.org` (or your Mailgun SMTP user)
- `SMTP_PASSWORD = <your-mailgun-smtp-password>`
- `FROM_EMAIL = minimal3dp@minimal3dp.org`
- `TO_EMAIL = minimal3dp@minimal3dp.org` (add others comma-separated as needed)

DNS (Mailgun domain verification):
- SPF: include Mailgun (e.g., `v=spf1 include:mailgun.org ~all` or merge into existing SPF)
- DKIM: add the CNAME/TXT records Mailgun provides for `minimal3dp.org`
- Optional DMARC recommended

Connectivity test:
```bash
nc -vz smtp.mailgun.org 587
openssl s_client -starttls smtp -connect smtp.mailgun.org:587 -crlf <<EOF
EHLO minimal3dp.org
QUIT
EOF
```

Manual AUTH test (replace with your real SMTP username)

Important: The commands after the `openssl s_client` line are SMTP protocol commands that you type into the OPENSSL SESSION, not into your zsh shell. If you paste them directly into zsh, you'll see errors like `zsh: parse error near \n`.

Interactive method:
```bash
openssl s_client -starttls smtp -connect smtp.mailgun.org:587 -crlf
# then paste:
EHLO minimal3dp.org
AUTH LOGIN
# base64 values
# echo -n "postmaster@minimal3dp.org" | base64
# echo -n "<YOUR_MAILGUN_SMTP_PASSWORD>" | base64
MAIL FROM:<minimal3dp@minimal3dp.org>
RCPT TO:<minimal3dp@minimal3dp.org>
DATA
Subject: Mailgun SMTP OK
From: minimal3dp@minimal3dp.org
To: minimal3dp@minimal3dp.org

Hello from Mailgun test.
.
QUIT
```

Here‑doc method (fully non‑interactive; safer to copy/paste in zsh):
```bash
USER_B64=$(printf %s "postmaster@minimal3dp.org" | base64)
PASS_B64=$(printf %s "<YOUR_MAILGUN_SMTP_PASSWORD>" | base64)
openssl s_client -starttls smtp -connect smtp.mailgun.org:587 -crlf <<EOF
EHLO minimal3dp.org
AUTH LOGIN
$USER_B64
$PASS_B64
MAIL FROM:<minimal3dp@minimal3dp.org>
RCPT TO:<minimal3dp@minimal3dp.org>
DATA
Subject: Mailgun SMTP OK
From: minimal3dp@minimal3dp.org
To: minimal3dp@minimal3dp.org

Hello from Mailgun test.
.
QUIT
EOF
```

Once secrets are set, push to `main` or manually dispatch the Popular Posts workflow to receive success emails.

---
## 2. Create Credentials
### SendGrid
1. Log in → Settings → API Keys → Create API Key (Restricted: Mail Send only).
2. Copy the API key securely.
3. Username (in SMTP auth) is the literal string `apikey`.
4. Password is the API key value.

### Mailgun
1. Verify domain & set DNS records (SPF + DKIM) first.
2. Navigate to Sending → Domains → Select domain → Scroll to SMTP credentials.
3. Use the default login (e.g., `postmaster@yourdomain`) or create a new SMTP credential; copy password.
4. US region uses `smtp.mailgun.org`; EU region uses `smtp.eu.mailgun.org`.

### AWS SES
1. Verify domain and/or sender emails; move out of sandbox (Production access).
2. In AWS Console: SES → SMTP Settings → Create SMTP credentials.
3. Download credentials: gives SMTP username & password (different from IAM access keys).
4. Server hostname uses your SES region (e.g., `email-smtp.us-east-1.amazonaws.com`).

### Postmark
1. Create (or use existing) Server → API Tokens.
2. Use server API token as password; username also the token (or `apikey` – Postmark accepts both patterns).
3. Verify sender signatures (DKIM) before sending.

### Brevo
1. Activate transactional email: SMTP & API section.
2. Generate a new SMTP key.
3. Username is your Brevo login/email or the generated key; password is the key.

### Gmail (App Password)
1. Enable 2FA on the Google account.
2. Security → App Passwords → Generate one for “Mail”.
3. Use your Gmail address as username, app password as password.
4. Be aware of sending limits and potential spam classification; not ideal for production monitoring.

---
## 3. Map Credentials to GitHub Secrets
Create the following repository secrets (GitHub → Settings → Secrets and variables → Actions → New repository secret):

| Secret Name      | Value Example                                  |
|------------------|------------------------------------------------|
| `SMTP_SERVER`     | `smtp.sendgrid.net`                            |
| `SMTP_PORT`       | `587`                                          |
| `SMTP_USERNAME`   | `apikey` (SendGrid) / `postmark_api_token` etc.|
| `SMTP_PASSWORD`   | (Your API key / generated SMTP password)       |
| `FROM_EMAIL`      | `alerts@minimal3dp.com`                        |
| `TO_EMAIL`        | `owner@minimal3dp.com,monitoring@minimal3dp.com`|

Notes:
- Multiple recipients can be comma-separated in `TO_EMAIL`.
- Use a dedicated FROM address with proper SPF/DKIM alignment for best deliverability.

---
## 4. DNS & Deliverability Checks
To reduce spam filtering:
1. Add **SPF** record: `v=spf1 include:sendgrid.net include:mailgun.org ~all` (adjust for your provider – do **not** chain too many includes, keep authoritative).
2. Add **DKIM** records per provider instructions.
3. Optionally add **DMARC**: `v=DMARC1; p=none; rua=mailto:dmarc-reports@minimal3dp.com` then move to `p=quarantine` or `reject` once confident.
4. Test with tools: `https://www.mail-tester.com` or `https://dkimvalidator.com`.

---
## 5. Test Connectivity (Local)
Before pushing secrets, validate network reachability:
```bash
# Replace host & port as needed
nc -vz smtp.sendgrid.net 587

# STARTTLS handshake test
openssl s_client -starttls smtp -connect smtp.sendgrid.net:587 -crlf <<EOF
EHLO test.minimal3dp.com
QUIT
EOF
```
Expected: TLS session established, server greeting lines displayed.

---
## 6. Manual SMTP Smoke Test
You can send a raw message with `openssl` (for advanced verification):
```bash
openssl s_client -starttls smtp -connect smtp.mailgun.org:587 -crlf
# After CONNECT paste commands:
EHLO test.minimal3dp.com
AUTH LOGIN
# Base64 encode username & password:
# echo -n "apikey" | base64
# echo -n "YOUR_SENDGRID_API_KEY" | base64
# Paste encoded lines when prompted
MAIL FROM:<alerts@minimal3dp.com>
RCPT TO:<minimal3dp@minimal3dp.org>
DATA
Subject: SMTP Smoke Test\nFrom: alerts@minimal3dp.com\nTo: minimal3dp@minimal3dp.com\n\nHello from raw SMTP.\n.
QUIT
```
If 250 responses appear at each stage, credentials are valid.

---
## 7. GitHub Actions Usage
The workflows already contain steps using `dawidd6/action-send-mail@v3`:
- Success step sends a concise summary.
- Failure step sends alert + run URL.
- Steps are skipped if **any** secret is missing (current logic relies on provider returning auth failure or the absence of secrets).

If you prefer hard gating (skip when missing), you can wrap with an `if:` condition using an environment variable flag.

### Optional: Conditional Toggle
Add a secret `EMAIL_NOTIFICATIONS_ENABLED` with value `true`, then modify workflow conditions:
```yaml
if: success() && env.EMAIL_NOTIFICATIONS_ENABLED == 'true'
```
Set via:
```yaml
env:
  EMAIL_NOTIFICATIONS_ENABLED: ${{ secrets.EMAIL_NOTIFICATIONS_ENABLED }}
```

---
## 8. Rotating Credentials
- Rotate API keys quarterly or on suspicion of compromise.
- Update the GitHub secret immediately; no workflow code change required.
- Revoke old keys in provider dashboard.

---
## 9. Common Pitfalls & Fixes
| Issue | Symptom | Fix |
|-------|---------|-----|
| Wrong port | Timeout or hang | Use 587 (STARTTLS) or 465 (implicit TLS) per provider docs. |
| Missing STARTTLS | Auth fails | Ensure provider supports STARTTLS on chosen port; test with `openssl s_client -starttls smtp`. |
| SPF fail | Emails go to spam | Add/merge provider include into existing SPF (single SPF record only). |
| DKIM missing | Lower trust | Add DKIM CNAME/TXT records from provider. |
| SES sandbox | Only verified recipients | Request production access or verify all destination emails. |
| Gmail blocks | 535 auth errors | Ensure App Password (not regular password) and 2FA enabled. |
| Comma spacing in TO | Some providers reject | Remove spaces or ensure provider tolerates them (`addr1@example.com,addr2@example.com`). |

---
## 10. Observability Enhancements (Optional)
- Add a BCC archive recipient (e.g., `alerts-archive@minimal3dp.com`).
- Use provider dashboards to monitor bounce & spam rates.
- Integrate webhook events (SendGrid/Mailgun) for future reliability tracking.

---
## 11. Security Recommendations
- Never commit SMTP credentials; only store in GitHub Actions secrets.
- Restrict API key scope (SendGrid: “Mail Send” only).
- Use distinct keys per environment (prod vs staging) if workflows expand.
- Enable alerting on provider dashboard for sudden bounce spikes.

---
## 12. Quick Checklist
1. Pick provider & verify domain (SPF/DKIM).
2. Generate SMTP credentials/API key.
3. Add all six secrets to repository.
4. Push a commit or manually dispatch workflow.
5. Confirm Slack + email success message.
6. Force a failure (optional) to confirm error path.

---
## 13. Forcing a Failure (Optional)
Temporarily insert a step before email send:
```yaml
- name: Force failure test
  run: exit 1
```
Then push a branch → confirm failure email & Slack alert. Remove the step afterward.

---
## 14. Future Extensions
- Add PagerDuty integration for high-severity failures.
- Aggregate daily metrics and email a digest (extend existing GA4 script).
- Implement templated HTML emails (switch to action supporting HTML body or inline MIME). 

---
## 15. Support & Validation Tools
- `https://app.sendgrid.com/` (Activity, suppression lists)
- `https://www.mailgun.com/` (Logs, events)
- `https://postmarkapp.com/` (Message streams)
- `https://mxtoolbox.com/` (DNS & blacklist checks)
- `https://mail-tester.com/` (Spam score report)

---
### Questions?
If you need provider-specific YAML examples or HTML email formatting, ask and we can patch the workflows further.
