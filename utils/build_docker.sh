#!/bin/sh
cd "$(dirname "$0")/.."

echo "Starting the Django server..."
docker-compose build

read -p "Pressione Enter para continuar..."