#!/usr/bin/env bash
# Start local stack (MySQL + API + FE). Never uses production RDS.
set -euo pipefail
cd "$(dirname "$0")/.."

if ! docker info >/dev/null 2>&1; then
  echo "Docker is not running. Start Docker Desktop, then retry."
  exit 1
fi

echo "Starting Kalapatru local stack..."
docker compose up --build "$@"
