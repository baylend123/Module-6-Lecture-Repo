'''
Volumes
Official documentation
Volumes are managed from within Docker—don’t depend on your file structure.

You wouldn’t modify the contents directly (only from inside a container), but you can use it to spin up new containers with same contents.

Instead of providing a path to the folder (like you would with a bind mount) you can provide the name of the volume.
'''

'''
Demo: Persist data from a postgres instance that runs in a container
# pull the postgres image so we can inspect it
docker pull postgres
# inspect the image to find out what the path to the volume should be
# and what port we want to expose
docker image inspect postgres

'''
'''
Demo: Persist data from a postgres instance that runs in a container
# run the container with a volume named "postgres-data"
# that corresponds to the path where a 
# postgres container stores its data
# (/var/lib/postgresql/data)
docker container run -p 5431:5432 \
-e POSTGRES_PASSWORD=password \
--name postgres5431 -d \
--mount type=volume,source=postgres-data,target=/var/lib/postgresql/data postgres
# now use the psql command line tool to connect
# to the postgres instance running in our container
psql -p 5431 -h localhost -U postgres

'''