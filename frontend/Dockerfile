# Frontend build stage
FROM node:18-alpine AS frontend-builder

WORKDIR /app/frontend

# Copy package files
COPY frontend/package*.json ./

# Install dependencies
RUN npm ci

# Copy source
COPY frontend/ .

# Build
RUN npm run build

# Frontend runtime
FROM node:18-alpine AS frontend

WORKDIR /app

# Install serve to run the frontend
RUN npm install -g serve

# Copy built app from builder
COPY --from=frontend-builder /app/frontend/dist ./dist

EXPOSE 3000

CMD ["serve", "-s", "dist", "-l", "3000"]
