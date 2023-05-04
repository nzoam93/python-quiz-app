# Use an official Node.js image as the base image
FROM nginx:latest

# Set the working directory in the container
WORKDIR /frontend_app



#Note: we do NOT want to copy the package-lock.json because that is more specific (and may not work for all architectures)
# COPY package.json ./

COPY nginx.conf /etc/nginx/conf.d/default.conf

COPY build /usr/share/nginx/html
##########note: the build command assume that you have run 'npm install' and 'npm run build' on the local computer to create the /build folder!

# Expose the port where the application will run
EXPOSE 80

# Start the application
CMD ["nginx", "-g", "daemon off;"]
