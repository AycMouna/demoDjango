#!/bin/bash

# Run database migrations
python manage.py migrate --noinput

# Start gunicorn server
gunicorn --bind 0.0.0.0:8000 demoDjango.wsgi:application
