#!/bin/sh
cd "$(dirname "$0")/../.."

echo "Running tests for AdminAppAuthTests..."
python manage.py test admin_app.tests.AdminAppAuthTests
read -p "Pressione Enter para continuar..."
echo ""
echo ""