#!/bin/bash
echo "Apply Database Migration"
python manage.py migrate
exec "$@"