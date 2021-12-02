'''

Demo: Serve a Website [1/2]
First, create a folder called app in your current 
directory, and make an empty index.html file inside 
the folder.
# run an nginx:alpine-based container, in detached mode
# mount the /app folder into the container at the 
# path where nginx serves
# its files from (/usr/share/nginx/html)
# and expose port 80 to view the contents
docker container run -d \
--mount type=bind,source="$(pwd)/app",target=/usr/share/nginx/html \
-p 8080:80 nginx:alpine

'''

'''

Demo: Serve a Website [2/2]
Once your container is running, visit localhost:8080—you 
should see a blank page. Add some content to your html 
page, then save and refresh localhost:8080. Now you can 
see the new content you added, because the contents of 
your folder stays in sync with the contents of the folder 
inside your container.

'''

