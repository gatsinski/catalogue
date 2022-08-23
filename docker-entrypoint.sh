#!/bin/sh

echo "Collecting static files"
python3 manage.py collectstatic --noinput

echo "Applying database migrations"
python3 manage.py migrate

echo "Compiling translations"
python3 ./manage.py compilemessages

echo "Starting server"
gunicorn catalogue.wsgi:application -w 2 -b :8002 --access-logfile "-"
