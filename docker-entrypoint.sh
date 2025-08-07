#!/bin/bash
set -e

# Wait for database to be ready (if using external database)
echo "Applying database migrations..."
python manage.py migrate --noinput

echo "Collecting static files..."
python manage.py collectstatic --noinput

echo "Starting application..."
exec "$@"