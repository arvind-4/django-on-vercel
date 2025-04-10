#!/bin/bash

echo "Installing dependencies..."
python3.9 -m pip install -r requirements.txt
echo "Successfully installed dependencies."

echo "Running database migrations..."
echo "Migrating database..."
python3.9 manage.py migrate --noinput
echo "Database migrated."

echo "Creating superuser..."
DJANGO_SUPERUSER_EMAIL=${DJANGO_SUPERUSER_EMAIL}
DJANGO_SUPERUSER_USERNAME=${DJANGO_SUPERUSER_USERNAME}
DJANGO_SUPERUSER_PASSWORD=${DJANGO_SUPERUSER_PASSWORD}
python3.9 manage.py createsuperuser \
    --email $DJANGO_SUPERUSER_EMAIL \
    --username $DJANGO_SUPERUSER_USERNAME \
    --noinput || true
echo "Superuser created. If it already exists, this is ignored."

echo "Collecting static files..."
python3.9 manage.py collectstatic --noinput
echo "Static files collected successfully."
