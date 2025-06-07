#!/bin/sh
cd "$(dirname "$0")/../.."

source venv/Scripts/activate

python manage.py runserver 0.0.0.0:8000 &
SERVER_PID=$!
sleep  6

echo ""
echo ""
echo ""

echo "Running tests for ProjectFormTest..."
python manage.py test admin_app.tests.ProjectFormTest

kill $SERVER_PID
read -p "Pressione Enter para continuar..."
