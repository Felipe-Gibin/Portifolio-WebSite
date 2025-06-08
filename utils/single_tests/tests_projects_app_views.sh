#!/bin/sh
cd "$(dirname "$0")/../.."

echo "Running tests for ProjectsViewsTests..."
python manage.py test projects_app.tests.ProjectsViewsTests
read -p "Pressione Enter para continuar..."
echo ""
echo ""