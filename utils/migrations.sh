#!/bin/sh
cd ..

source venv/Scripts/activate

python manage.py makemigrations
python manage.py migrate
