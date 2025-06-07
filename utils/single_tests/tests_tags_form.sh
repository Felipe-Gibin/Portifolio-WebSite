#!/bin/sh
cd ..
cd ..

source venv/Scripts/activate

python manage.py runserver 0.0.0.0:8000 &
SERVER_PID=$!
sleep  6

echo ""
echo ""
echo ""

echo "Running tests for TagsFormTest..."
python manage.py test admin_app.tests.TagsFormTest

kill $SERVER_PID
read -p "Pressione Enter para continuar..."