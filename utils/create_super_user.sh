#!/bin/sh
cd ..
source venv/Scripts/activate

python manage.py runserver 0.0.0.0:8000 &
SERVER_PID=$!
sleep  6

python manage.py createsuperuser --username admin --email admin@admin.com

echo ""
echo ""
echo ""
kill $SERVER_PID
read -p "Pressione Enter para continuar..."