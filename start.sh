pyth#!/bin/bash
python manage.py collectstatic --noinput
python manage.py migrate --noinput
gunicorn  jango.wsgi:application --bind 0.0.0.0:$PORT