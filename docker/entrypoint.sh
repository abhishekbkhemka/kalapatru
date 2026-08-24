#!/bin/sh
set -e

echo "Waiting for MySQL..."
python <<'PY'
import os, time
import MySQLdb

url = os.environ.get("DATABASES_URL", "")
# mysql://user:pass@host:port/db
from urllib.parse import urlparse
u = urlparse(url)
host = u.hostname or "db"
port = u.port or 3306
user = u.username or "kalapatru"
password = u.password or "kalapatru"
db = (u.path or "/kalptaru1").lstrip("/")

for i in range(60):
    try:
        conn = MySQLdb.connect(host=host, port=port, user=user, passwd=password, db=db)
        conn.close()
        print("MySQL is ready")
        break
    except Exception as exc:
        print(f"  attempt {i+1}/60: {exc}")
        time.sleep(2)
else:
    raise SystemExit("MySQL did not become ready in time")
PY

echo "Running migrations..."
python manage.py migrate --noinput

echo "Bootstrapping local admin + org..."
python manage.py bootstrap_local

echo "Starting API on :8000"
exec python manage.py runserver 0.0.0.0:8000
