#!/usr/bin/env python
import os
import sys

# Prefer PyMySQL when mysqlclient native lib is unavailable (common on macOS).
try:
    import MySQLdb  # noqa: F401
except ImportError:
    import pymysql
    pymysql.install_as_MySQLdb()


if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "kalapatru.settings")
    from django.core.management import execute_from_command_line
    execute_from_command_line(sys.argv)
