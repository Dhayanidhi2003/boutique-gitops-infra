# Step 1: Use the official lightweight Nginx web server
FROM nginx:alpine

# Step 2: Set the directory inside the container
WORKDIR /usr/share/nginx/html

# Step 3: Delete any default placeholder files
RUN rm -rf ./*

# Step 4: Copy your e-commerce template files
COPY . .

# Step 5: Expose port 80
EXPOSE 80

# Step 6: Start Nginx
CMD ["nginx", "-g", "daemon off;"]