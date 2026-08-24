#!/bin/sh
set -e

# Production entrypoint.
# DB comes ONLY from env: DATABASE_URL or DATABASES_URL
# Never defaults to current production RDS.

DB_URL="${DATABASE_URL:-${DATABASES_URL:-}}"
if [ -z "$DB_URL" ]; then
  echo "ERROR: Set DATABASE_URL or DATABASES_URL to your NEW staging/test database."
  echo "Do not use the current production RDS URL until you intentionally cut over."
  exit 1
fi

echo "Waiting for database..."
python <<'PY'
import os, time
from urllib.parse import urlparse

url = os.environ.get("DATABASE_URL") or os.environ.get("DATABASES_URL") or ""
u = urlparse(url)
host = u.hostname or "localhost"
port = u.port or 3306
user = u.username or "root"
password = u.password or ""
db = (u.path or "/").lstrip("/") or "mysql"

try:
    import MySQLdb as dbapi
except ImportError:
    import pymysql
    dbapi = pymysql

for i in range(60):
    try:
        conn = dbapi.connect(host=host, port=port, user=user, password=password, database=db)
        conn.close()
        print("Database is ready")
        break
    except TypeError:
        # mysqlclient uses passwd=/db=
        try:
            conn = dbapi.connect(host=host, port=port, user=user, passwd=password, db=db)
            conn.close()
            print("Database is ready")
            break
        except Exception as exc:
            print(f"  attempt {i + 1}/60: {exc}")
            time.sleep(2)
    except Exception as exc:
        print(f"  attempt {i + 1}/60: {exc}")
        time.sleep(2)
else:
    raise SystemExit("Database did not become ready in time")
PY

echo "Collecting static files..."
python manage.py collectstatic --noinput

echo "Running migrations..."
python manage.py migrate --noinput

# First-deploy helper only — set BOOTSTRAP_ADMIN=false after creating your user
if [ "${BOOTSTRAP_ADMIN:-false}" = "true" ]; then
  export BOOTSTRAP_ADMIN_USER="${BOOTSTRAP_ADMIN_USER:-admin}"
  export BOOTSTRAP_ADMIN_PASSWORD="${BOOTSTRAP_ADMIN_PASSWORD:-admin123}"
  echo "Bootstrapping admin (BOOTSTRAP_ADMIN=true)..."
  python manage.py bootstrap_local
fi

PORT="${PORT:-8000}"
WORKERS="${WEB_CONCURRENCY:-3}"
echo "Starting Gunicorn on :${PORT} (workers=${WORKERS})"
exec gunicorn kalapatru.wsgi:application \
  --bind "0.0.0.0:${PORT}" \
  --workers "${WORKERS}" \
  --timeout 120 \
  --access-logfile - \
  --error-logfile -
