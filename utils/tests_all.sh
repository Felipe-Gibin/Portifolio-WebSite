#!/bin/sh
cd ..

source venv/Scripts/activate

python manage.py runserver 0.0.0.0:8000 &
SERVER_PID=$!
sleep  6

echo "Running tests for all forms..."
echo ""
echo ""
echo ""

echo "Running tests for SendEmailFormTest..."
python manage.py test main_app.tests.SendEmailFormTest
echo ""
echo ""
echo ""

echo "Running tests for ProjectFormTest..."
python manage.py test admin_app.tests.ProjectFormTest
echo ""
echo ""
echo ""

echo "Running tests for TagsFormTest..."
python manage.py test admin_app.tests.TagsFormTest
echo ""
echo ""
echo ""

echo "Running tests for MainAppViewsTests..."
python manage.py test main_app.tests.MainAppViewsTests
echo ""
echo ""
echo ""

echo "Running tests for AdminAppAuthTests..."
python manage.py test admin_app.tests.AdminAppAuthTests
echo ""
echo ""
echo ""

echo "Running tests for AdminPermissionsTest..."
python manage.py test projects_app.tests.AdminPermissionsTest
echo ""
echo ""
echo ""

echo "Running tests for ProjectsViewsTests..."
python manage.py test projects_app.tests.ProjectsViewsTests
echo ""
echo ""
echo ""

echo "Running tests for ProjectsIntegrationTest..."
python manage.py test projects_app.tests.ProjectsIntegrationTest
echo ""
echo ""
echo ""

kill $SERVER_PID
read -p "Pressione Enter para continuar..."