# Use a lightweight Nginx web server as our base
FROM nginx:alpine

# Copy all the website files from this folder into the Nginx public directory
COPY . /usr/share/nginx/html

# Open port 80 so internet traffic can reach the website
EXPOSE 80