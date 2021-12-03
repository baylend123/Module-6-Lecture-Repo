'''networks
If you don’t specify a network, all the containers in the docker-compose file will be put onto one custom network together.

If you want multiple networks, specify all the names under the top-level networks key. Containers can belong to multiple networks.

networks:
  network_name:
  second_network_name:
Putting it all together…
version: '3.8'

services:
  db:
    env_file:
      - ./.env.prod.db
    image: postgres:latest
    networks:
      - default
    volumes:
      - postgres-data:/var/lib/postgresql/data

  api:
    build: .
    env_file:
      - ./.env.prod
    depends_on:
      - db
    networks:
      - default
    ports:
      - 8000:8000

volumes:
  postgres-data:
Useful docker-compose CLI commands
docker-compose up: create all containers, networks and volumes described in our docker-compose file
docker-compose up -d: same as above, but run containers in detached mode
docker-compose -f <filename> up: create containers based on a different docker-compose file
docker-compose down: remove all containers and networks
docker-compose down -v: remove all containers, networks, and volumes'''