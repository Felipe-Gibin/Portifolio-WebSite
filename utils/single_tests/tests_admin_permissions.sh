#!/bin/sh
cd "$(dirname "$0")/../.."

echo "Running tests for AdminPermissionsTest..."
python manage.py test projects_app.tests.AdminPermissionsTest
read -p "Pressione Enter para continuar..."
echo ""
echo ""