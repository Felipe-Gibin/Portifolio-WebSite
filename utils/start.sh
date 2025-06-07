#!/bin/sh
cd "$(dirname "$0")/.."

source venv/Scripts/activate
python manage.py runserver 0.0.0.0:8000
