#!/bin/sh
cd "$(dirname "$0")/../.."

echo "Running tests for TagsFormTest..."
python manage.py test admin_app.tests.TagsFormTest
read -p "Pressione Enter para continuar..."
echo ""
echo ""