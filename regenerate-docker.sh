#!/bin/bash
echo "-> Stop and remove database container"
docker-compose stop db
docker-compose rm -f db
docker-compose run --rm web scripts/initialize-docker.sh
