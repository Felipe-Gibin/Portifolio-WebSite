#!/bin/sh
cd "$(dirname "$0")/../.."

echo "Running tests for ProjectsIntegrationTest..."
python manage.py test projects_app.tests.ProjectsIntegrationTest
read -p "Pressione Enter para continuar..."
echo ""
echo ""