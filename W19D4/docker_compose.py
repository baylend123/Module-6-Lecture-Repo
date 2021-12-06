'''

Docker-Compose
docker-compose allows you to create a collection of interconnected containers, networks, and volumes with a single command.

A lot of the options you had to specify at the command line every time you ran a container can be totally automated with docker-compose.

To use docker-compose, you first create a docker-compose.yml file which describes all of the services, networks, and volumes in your application.

'''

'''
docker-compose.yml file
The docker-compose tool uses files written in a data-serialization language called YAML (extension is .yml).

At the top level of each file, include the version of docker-compose, then you can list services (containers), plus any volumes or networks if necessary.


version: '3.8'

services:
  # any services go here
networks:
  # networks go here
volumes:
  # volumes
'''

'''
services
Services are containers. Immediately under the services keyword, the next level down will be the name of the containers.

version: '3.8'

services:
  container_name_1:
    # more info
  container_name_2:
    # more info
'''

'''
services keywords: build
When we create a container, we always have to specify an image.

If we are building the image from a Dockerfile, we can use the build keyword to specify the context for the Dockerfile. If the Dockerfile is in the same folder as the docker-compose.yml file, that context will just be . to indicate the present folder

container_name_1:
  build: .
'''

'''
services keywords: build
If the Dockerfile is named anything other than Dockerfile, you can indicate the Dockerfile name and the context (path) separately.

container_name_1:
  build: 
    context: .
    dockerfile: Dockerfile-prod

'''

'''

services keywords: image
If you are using an existing image that does not need to be built from a Dockerfile, you can specify the image name with the image keyword.

Docker will look for that image locally, and if it does not find it, it will pull from Dockerhub.

container_name_1:
  image: image_name
If you are also using the build keyword, then the image keyword will not have the same function.
'''

'''
services keywords: image
If you are building an image with the build keyword, then the image keyword will name the image that you are building.

container_name_1:
  build: .
  image: new_image_name

'''

'''
services keywords: volumes
The volumes keyword can specify any volumes or bind mounts that will be associated with the service.

If you use any named volumes, they will also need to be listed under the top level volumes keyword.

container_name_1:
  volumes:
    # for bind mounts
    - ./path/locally:/path/to/bind/mount/on/container
    # for named volumes
    - volume_name:/path/to/volume/on/container
    # for anonymous volumes
    - /path/to/volume/on/container
'''


'''
services keywords: networks
By default, all the containers in the docker-compose file will be put onto one custom network together. Sometimes, however, you may want separate networks. You can use the networks keyword on a given service to connect it to specific networks.

If you use any additional networks, they will need to be listed under the top level networks keyword. If you are only using the default network you don’t need to use the top-level networks keyword.

container_name_1:
  networks:
    - network_name

'''

'''
services keywords: environment
You can specify environment variables, like DATABASE_URL, SECRET_KEY, etc, using the environment keyword. That will allow you to specify the keywords directly.

container_name_1:
  environment:
    NAME: value
If you want to use a .env file instead, you can use the env_file keyword:

container_name_1:
  env_file:
    - ./.env

'''

'''
services keywords: ports
You can use the ports keyword to publish mappings between internal and external ports.

Unlike EXPOSE in a Dockerfile, this will actually publish the port, like using the -p flag with docker container run.

container_name_1:
  ports:
    # <external port>:<internal port>
    -8000:80

'''

'''
Docker services summary
services:
  service_name_1:
    build:
      context: ./folder_with_dockerfile
      dockerfile: Dockerfile-alternate.Dockerfile
    image: imagename 
    volumes: 
      # with a named volume - also list name under top-level volumes
      - volume_name:/path/to/volume/on/container
        # for bind mounts
      - ./path/locally:/path/to/bind/mount/on/container
    # by default, docker-compose will create a single network for all containers
    networks:
        - network_name
    environment:
      DATABASE_URL: postgresql://username:password/localhost
      ANOTHER_VARIABLE: more-stuff
    ports:
      # <external port>:<internal port>
      -8000:80
  second_service_2:
    image:
    #... all the other keywords for this service

'''

'''

volumes
If you include any named volumes, list their names under the top-level “volumes” key.

Anonymous volumes and bind mounts don’t need to be listed.

volumes:
  some_named_volume:
  another_named_volume:
'''

'''
networks
If you don’t specify a network, all the containers in the docker-compose file will be put onto one custom network together.

If you want multiple networks, specify all the names under the top-level networks key. Containers can belong to multiple networks.

networks:
  network_name:
  second_network_name:

fgfgfgfgfg
'''

'''
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

'''