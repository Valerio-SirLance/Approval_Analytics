# Use the official Node.js image to build the React app
FROM node:16 AS build

WORKDIR /app

# Copy package.json and package-lock.json first to take advantage of Docker's caching mechanism
COPY package*.json ./

# Clean npm cache and install dependencies
RUN npm cache clean --force && npm install --legacy-peer-deps

# Install react-scripts explicitly (if not already in package.json)
RUN npm install react-scripts --save-dev

# Copy the entire directory content (including src, public, etc.)
COPY . /app/

# Build the React app
RUN npm run build

# Production image using nginx
FROM nginx:alpine

# Copy custom nginx.conf
COPY nginx.conf /etc/nginx/nginx.conf

# Copy the build files from the build stage to nginx
COPY --from=build /app/build /usr/share/nginx/html

# Expose the port the app will run on
EXPOSE 80

# Run nginx in the foreground
CMD ["nginx", "-g", "daemon off;"]
