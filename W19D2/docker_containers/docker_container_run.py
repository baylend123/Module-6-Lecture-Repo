'''
docker container run (Official documentation)
Usage:
    https://docs.docker.com/engine/reference/commandline/container_run/

docker container run [OPTIONS] image-name [COMMAND] [ARG...]
You always need to specify the image—every container is based on an image.
The optional “OPTIONS” are specified with a flag.
Any options you include will come before the image name
Each image has a default command—that will be replaced if you specify a new command 
(after the image-name)
'''

'''
Commonly used flags for docker container run:
flag	purpose	example usage
--name	specify a name for the container	--name hello
-p / --publish	publish a port to the “outside world” on your localhost (externalport:internalport)	-p 8080:80
-d	detached session (runs in background)	-d
--rm	automatically remove container once stopped	--rm
-it	use an interactive session (e.g. bash)	-it / -i -t

'''
