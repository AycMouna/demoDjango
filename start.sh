#!/bin/bash

# Run database migrations
python manage.py migrate --noinput

# Start gunicorn server on the PORT provided by Render
gunicorn --bind 0.0.0.0:${PORT:-8000} demoDjango.wsgi:application
