# Composing Dockerfiles
# Each line of execution in a Dockerfile will have its own image layer.

# Each line contains an instruction, which must begin with a keyword.

# Dockerfile Keywords: FROM (https://docs.docker.com/engine/reference/builder/#from)
# All Dockerfiles begin with a FROM statement.

# In this statement you specify the parent image to start from.

# For example, if I wanted to run a Flask server, I might start with a parent image that is the official Python image.

# Usage:

# FROM <IMAGE NAME>

FROM alpine:3.6

# Dockerfile Keywords: WORKDIR (https://docs.docker.com/engine/reference/builder/#workdir)
# WORKDIR changes the working directory in the image, sort of like using cd at the command line. That means any subsequent commands will take place in that directory.

# Additionally, WORKDIR will create a directory if it does not exist yet.

# Usage:

# WORKDIR <DIRECTORY PATH>

WORKDIR /the/workdir/path

# Dockerfile Keywords: COPY (https://docs.docker.com/engine/reference/builder/#copy)
# COPY moves a file, files, or directory from your host machine to a location on the image.

# Usage:

# COPY <LOCAL DIR PATH> <IMAGE DIR PATH>

COPY app app

# Dockerfile Keywords: ENV (https://docs.docker.com/engine/reference/builder/#env)
# ENV lets you set environment variables in the image.

# Usage:

# ENV <ENV VARIABLE>=<VALUE>

ENV ENV=VAR

# Dockerfile Keywords: EXPOSE (https://docs.docker.com/engine/reference/builder/#expose)
# EXPOSE indicates the port that should be exposed.

# Note that this does not actually publish the port—when you run a container based on the image you would still have to use the -p external_port:internal_port flag. The command just sets the intended port in the image’s metadata.

# Usage:

EXPOSE 8000

# A note about EXPOSE vs. publish
# EXPOSE tells Docker that the image will listen on the specified port within a container at runtime.

# This allows the container to easily communicate with others on the same network via this exposed port.

# Publishing a port (with the -p flag) maps the container’s EXPOSE’d port to a port on the Docker host (your local machine) via port forwarding.


# Dockerfile Keywords: RUN (Official documentation)
# RUN executes a command on the image.

# Usage:

# RUN <COMMAND>

# RUN echo "Hello World!"

# Dockerfile Keywords: CMD (Official documentation)
# CMD specifies the default process that a container based on the image should execute. An image can only have one CMD—if more than one is specified, only the latter will be used.

# If you include a command after the image name when running a container with docker container run ..., that will replace the CMD in the Dockerfile.

# Usage:

# # exec form (preferred)
# CMD ["individual", "strings", "for", "command"]

# # params for ENTRYPOINT (if specified)
# CMD ["param1", "param2"]

# # shell form (will execute in shell)
# CMD command param1 param2

CMD ["individual", "strings", "for", "command"]