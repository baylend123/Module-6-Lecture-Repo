'''
Docker networks
Networks allow containers to communicate with each other, whether or not they are exposing ports to the host.
Official documentation

https://docs.docker.com/network/
'''

'''
Networking with Docker
By default, containers are connected to the “bridge” driver network. While containers can communicate via IP address over the bridge network, it does not enable DNS resolution.

To be able to communicate via domain name over a network we must create a custom network.

'''