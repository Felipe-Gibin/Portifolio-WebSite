#!/bin/sh
cd ..

source venv/Scripts/activate

python manage.py makemigrations projects_app
python manage.py makemigrations admin_app
python manage.py makemigrations main_app
python manage.py makemigrations
python manage.py migrate

echo "Concluído. Pressione Enter ou aguarde 10 segundos..."
read -t 10