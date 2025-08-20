#!/bin/sh

# Run database migrations
python manage.py migrate

# Collect static files
python manage.py collectstatic --noinput

# Start Gunicorn processes
gunicorn user_service.wsgi:application --config /app/gunicorn.conf.py &

# Start Nginx
nginx -g 'daemon off;'
