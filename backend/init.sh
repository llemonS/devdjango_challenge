#!/bin/bash

echo "Looking for new dependencies..."
pip install -r requirements.txt

echo "Applying migrations..."
python manage.py makemigrations
python manage.py migrate

echo "Initializing backend worker..."
celery -A backend worker -l info &

echo "Running server."
python manage.py runserver 0.0.0.0:8000
