# Use an official Node.js image as the base image
FROM node:latest

# Set the working directory in the container
WORKDIR /frontend_app

# Copy package.json 
#Note: we do NOT want to copy the package-lock.json because that is more specific (and may not work for all architectures)
COPY package.json ./

# Install dependencies
# note: do not do npm ci as that copies the package-lock
RUN npm install 

# Copy the rest of the application code to the container
COPY . .

# Build the React application
RUN npm run build

# Expose the port where the application will run
EXPOSE 3000

# Start the application
CMD ["npm", "start"]