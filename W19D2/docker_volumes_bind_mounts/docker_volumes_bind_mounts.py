'''

Docker volumes/bind mounts
Using bind mounts and volumes allows data to persist even after a container is gone.

Bind mounts directly mount the contents of a folder on your filesystem into your container.

Volumes are managed by Docker—so you wouldn’t directly access the files, but can be accessed and modified from within a container.

'''

'''
Options for creating volumes/bind mounts
There are two different types of syntax you can use with docker container run to establish volumes and bind mounts. Both flags can create either volumes or bind mounts.

-v and --mount flags have the same purpose.
--mount is typically preferred as it is considered to be clearer.
docker container run -v ...
docker container run --mount ...

'''
'''
--mount syntax
Pass in a series of <key>=<value> pairs in any order, separated by a comma.

Type must be “bind” for bind mounts, or “volume” for volumes
'''
'''

--mount syntax
for bind mounts
--mount type=bind,source=/absolute/path,target=/absolute/path/in/container
for volumes
--mount type=volume,source=name_of_volume,target=/absolute/path/in/container
'''