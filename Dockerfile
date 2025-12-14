# Stage 1: Build the site
FROM node:20-slim AS builder

# Install Hugo Extended
# We use the pre-built binary to ensure compatibility and speed
ENV HUGO_VERSION=0.152.2
RUN apt-get update && apt-get install -y wget ca-certificates git golang && \
    wget -O hugo.deb https://github.com/gohugoio/hugo/releases/download/v${HUGO_VERSION}/hugo_extended_${HUGO_VERSION}_linux-amd64.deb && \
    dpkg -i hugo.deb && \
    rm hugo.deb && \
    rm -rf /var/lib/apt/lists/*

WORKDIR /app

# Copy dependency files
COPY package.json ./

# Install Node dependencies
RUN npm install

# Copy the rest of the site (hugo.toml, content/, assets/, etc.)
COPY . .

# Build the site
# We use the script from package.json but ensure it runs in production mode
RUN npm run build

# Stage 2: Serve with Nginx
FROM nginx:alpine

# Copy the built site from the builder stage
COPY --from=builder /app/public /usr/share/nginx/html

# Expose port 80 (Railway maps this to the public URL)
EXPOSE 80

# Start Nginx
CMD ["nginx", "-g", "daemon off;"]
