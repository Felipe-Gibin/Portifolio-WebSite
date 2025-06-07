#!/bin/sh
cd "$(dirname "$0")/../.."

source venv/Scripts/activate

python manage.py runserver 0.0.0.0:8000 &
SERVER_PID=$!
sleep  6

echo ""
echo ""
echo ""

echo "Running tests for AdminPermissionsTest..."
python manage.py test projects_app.tests.AdminPermissionsTest

kill $SERVER_PID
read -p "Pressione Enter para continuar..."