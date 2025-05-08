#!/bin/sh
cd ..

source venv/Scripts/activate

python manage.py makemigrations
python manage.py migrate

echo "Concluído. Pressione Enter ou aguarde 10 segundos..."
read -t 10