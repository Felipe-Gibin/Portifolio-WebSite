#!/bin/sh
cd "$(dirname "$0")/../.."

echo "Running tests for MainAppViewsTests..."
python manage.py test main_app.tests.MainAppViewsTests
read -p "Pressione Enter para continuar..."
echo ""
echo ""