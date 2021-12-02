'''

Networking demo [1/2]
Let’s create a network, and attach containers to it so we can see how networked containers communicate.

For comparison, we’ll use two containers that are on the default network.

# create a network based on the bridge driver, called "test-network"
docker network create --driver bridge test-network
# create two images on that network
docker container run -d --name c1 --network test-network nginx:alpine
docker container run -d --name c2 --network test-network nginx:alpine

# create two more images, without specifying a network
docker container run -d --name c3 nginx:alpine
docker container run -d --name c4 nginx:alpine


# access the shell on one of our two networked containers
docker container exec -it c1 ash
# ping a container that is not on the network
ping -c 2 c3
# ping a container that is on the network
ping -c 2 c2


docker container exec -it c3 ash
ping -c 2 c1
ping -c 2 c4
'''