#!/bin/sh
cd "$(dirname "$0")/../.."

source venv/Scripts/activate

python manage.py runserver 0.0.0.0:8000 &
SERVER_PID=$!
sleep  6

echo ""
echo ""
echo ""

echo "Running tests for ProjectsViewsTests..."
python manage.py test projects_app.tests.ProjectsViewsTests

kill $SERVER_PID
read -p "Pressione Enter para continuar..."