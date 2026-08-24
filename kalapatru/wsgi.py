"""
WSGI config for kalapatru project.
"""
import os

try:
    import MySQLdb  # noqa: F401
except ImportError:
    import pymysql
    pymysql.install_as_MySQLdb()

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "kalapatru.settings")
from django.core.wsgi import get_wsgi_application

application = get_wsgi_application()
