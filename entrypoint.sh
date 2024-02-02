#!/bin/sh
echo "Apply Database Migration"
python manage.py migrate --no-input
python manage.py collectstatic --no-input
gunicorn src.wsgi:application --bind 0.0.0.0:8000
