#!/bin/sh
cd "$(dirname "$0")/../.."

echo "Running tests for SendEmailFormTest..."
python manage.py test main_app.tests.SendEmailFormTest
read -p "Pressione Enter para continuar..."
echo ""
echo ""