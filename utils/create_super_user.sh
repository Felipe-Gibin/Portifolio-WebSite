#!/bin/sh
cd "$(dirname "$0")/.."

echo "Creating superuser..."
python manage.py createsuperuser
read -p "Pressione Enter para continuar..."