# Kalapatru API

Django 4.2 + DRF + JWT auth. Frontend lives in the sibling repo `kalapatru-fe`.

## Deploy (staging / new server — does not touch current prod)

See **[DEPLOY.md](./DEPLOY.md)**.

```bash
cp .env.production.example .env.production
# Point DATABASE_URL at a NEW MySQL — not current prod RDS
docker compose -f docker-compose.prod.yml --env-file .env.production up -d --build
```

Local Docker (unchanged): `docker compose up --build`

| Service | URL |
|---------|-----|
| Frontend | http://localhost:5173 |
| API | http://localhost:8000 |
| MySQL | localhost:3307 |

**Login:** `admin` / `admin123`

Stop:

```bash
docker compose down
```

Reset local DB (wipe volume):

```bash
docker compose down -v
docker compose up --build
```

---

## Stack

- Python 3.11 (Docker) / 3.9+ (local venv)
- Django 4.2 LTS + DRF + SimpleJWT
- MySQL 8 (Docker Compose)

## Auth API

| Method | Path | Notes |
|--------|------|-------|
| POST | `/api/auth/login/` | `{username,password}` → JWT + user |
| POST | `/api/auth/refresh/` | refresh access token |
| GET | `/api/auth/me/` | current user |
| GET/POST | `/api/auth/users/` | admin only |
| GET/PUT/DELETE | `/api/auth/users/<id>/` | admin only |

### Roles

- **admin** — full write + user management
- **operator** — write forwarding notes / dispatches
- **viewer** — read only

## Local venv (without Docker)

Point `.env` at a **local** MySQL — do not use production RDS for day-to-day work.

```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
# edit .env → DATABASES_URL=mysql://...@localhost:3306/kalptaru1
python manage.py migrate
python manage.py bootstrap_local
python manage.py runserver 0.0.0.0:8000
```

## Env notes

- Docker Compose sets `DATABASES_URL` to the local `db` service explicitly.
- `load_dotenv(..., override=False)` so Docker/shell env wins over any host `.env`.
- Reference local vars: `.env.docker`
