'''

Docker images
Docker images are the templates that we use to run containers.

Every time you run a container, you specify an image name.

All images are created from Dockerfiles, which are the instructions for
building the image.

But you can also make your own images, by writing a custom Dockerfile.

'''

'''
Docker image commands
Command	Description
docker image ls	list all images currently on machine
docker image history <IMAGE NAME>	show the layers in an image
docker image inspect <IMAGE NAME>	show all of the metadata associated with an image
docker image rm <IMAGE NAME>	remove a cached image from your system
docker image push <IMAGE NAME>	push an image (that is already built) to dockerhub
docker image build [OPTIONS] <PATH>	build an image from a Dockerfile based on the path

'''

