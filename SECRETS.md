**Secret Management — Quick Guide**

- **Do not commit** `.env` or any file containing secrets. `.gitignore` already excludes `.env`.
- **Use environment variables** for `SECRET_KEY`, `DB_PASS`, and other credentials in development and production.
- **Store secrets in your deployment platform / CI** (e.g., GitHub Actions Secrets, AWS Parameter Store, Vault).
- **Rotate keys** immediately if a secret was accidentally exposed or default values were used earlier.
- **Use a strong `SECRET_KEY`** (at least 32 bytes); generate with a cryptographically secure generator.
- **Limit token lifetime** (`ACCESS_TOKEN_EXPIRE_MINUTES`) and revoke/rotate keys when required.
- **Audit repository history** for committed secrets (use tools like `git-secrets`, `truffleHog`, or `gitleaks`).

Example (local `.env`):

DB_HOST=localhost
DB_PORT=5432
DB_NAME=newsdb
DB_USER=postgres
DB_PASS=your_db_password_here
SECRET_KEY=replace_with_a_strong_secret_key

If you want, I can add a short CI example for storing secrets in GitHub Actions.
