# Production / staging deploy

Deploy the **new** stack to a **different** server for testing.  
Current production is not changed by these files.

## Safety

1. Use a **new** MySQL (empty or a restored copy). Do **not** point `DATABASE_URL` at current production RDS until you cut over on purpose.
2. Local day-to-day: `docker compose up` (`docker-compose.yml`).
3. Staging/prod: `docker-compose.prod.yml` + `.env.production`.

---

## Deploy on any VPS (Linode, DigitalOcean, EC2, …)

On the **new** server:

```bash
git clone <api-repo> kalapatru
git clone <fe-repo> kalapatru-fe
cd kalapatru

cp .env.production.example .env.production
# edit .env.production — NEW DB, SECRET_KEY, hosts, VITE_API_BASE_URL
```

### MySQL on the same VPS

```bash
docker compose -f docker-compose.prod.yml --profile with-db \
  --env-file .env.production up -d --build
```

In `.env.production`:

```
DATABASE_URL=mysql://kalapatru:CHANGE_ME@db:3306/kalapatru_staging
```

### Managed / external MySQL

```bash
docker compose -f docker-compose.prod.yml --env-file .env.production up -d --build
```

Then open:

- Web: `http://YOUR_SERVER_IP/`
- API: `http://YOUR_SERVER_IP:8000/`
- Admin: `http://YOUR_SERVER_IP:8000/admin/`

After first login, set `BOOTSTRAP_ADMIN=false` and recreate the API container.

---

## Env vars (API)

| Variable | Required | Notes |
|----------|----------|-------|
| `DATABASE_URL` or `DATABASES_URL` | yes | New DB for staging |
| `SECRET_KEY` | yes | Long random string |
| `DEBUG` | yes | `False` |
| `ALLOWED_HOSTS` | yes | API hostname(s) |
| `CORS_ALLOWED_ORIGINS` | yes | Frontend origin(s) |
| `CSRF_TRUSTED_ORIGINS` | if HTTPS | Include `https://…` |
| `BOOTSTRAP_ADMIN` | optional | `true` only first boot |
| `WEB_CONCURRENCY` | optional | Gunicorn workers (default 3) |
| `PORT` | optional | Default `8000` |

## Frontend (build-time)

| Variable | Notes |
|----------|-------|
| `VITE_API_BASE_URL` | Public API URL the browser will call |

---

## Check you are not on old prod

```bash
# On the new server
printenv DATABASE_URL
# Host must NOT be your current production RDS hostname
```
