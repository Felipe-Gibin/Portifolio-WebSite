#!/bin/sh
cd "$(dirname "$0")/.."

echo "Iniciando migrações do banco de dados..."
python manage.py makemigrations projects_app
python manage.py makemigrations admin_app
python manage.py makemigrations main_app
python manage.py makemigrations
python manage.py migrate

read "Concluído. Pressione Enter ou aguarde 10 segundos..."
