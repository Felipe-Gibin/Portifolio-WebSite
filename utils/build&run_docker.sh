#!/bin/sh
cd "$(dirname "$0")/.."

echo "Building the Django server..."
docker-compose build

read -p "Pressione Enter para continuar..."
echo "Starting the Django server..."
docker-compose up