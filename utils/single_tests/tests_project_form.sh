#!/bin/sh
cd "$(dirname "$0")/../.."

echo "Running tests for ProjectFormTest..."
python manage.py test admin_app.tests.ProjectFormTest
read -p "Pressione Enter para continuar..."
echo ""
echo ""
