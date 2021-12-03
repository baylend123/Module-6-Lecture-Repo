# # log in to dockerhub
#   docker login
# # build from the dockerfile located in our current directory
# # and tag with your dockerhub username
#   docker build -t your-dockerhub-username/test_app .
# # push the image to dockerhub
#   docker image push your-dockerhub-username/test_app
# # you can remove the local version of the image
#   docker image rm your-dockerhub-username/test_app
# # make a container based on the image—because it does not exist locally, 
# # it will pull down the image from your dockerhub
#   docker container run -p 3000:3000 --name demo your-dockerhub-username/test_app