# Docker Setup Guide

## Prerequisites

1. **Install Docker Desktop** (Free):
   - Download from: https://www.docker.com/products/docker-desktop/
   - Install and start Docker Desktop
   - Ensure Docker is running (you should see the Docker icon in your system tray)

## Local Docker Testing

### 1. Build the Docker Image
```bash
docker build -t mlops-pipeline .
```

### 2. Run the Container
```bash
docker run --rm mlops-pipeline
```

### 3. Interactive Mode (for debugging)
```bash
docker run -it --rm mlops-pipeline /bin/bash
```

## Docker Commands Reference

| Command | Description |
|---------|-------------|
| `docker build -t mlops-pipeline .` | Build image with tag 'mlops-pipeline' |
| `docker run --rm mlops-pipeline` | Run container and remove after execution |
| `docker images` | List all Docker images |
| `docker ps -a` | List all containers (including stopped) |
| `docker rmi mlops-pipeline` | Remove the image |
| `docker system prune` | Clean up unused Docker resources |

## Troubleshooting

### If Docker build fails:
1. Ensure Docker Desktop is running
2. Check if you're in the correct directory (should contain Dockerfile)
3. Verify all files are present (src/, requirements.txt, etc.)

### If container fails to run:
1. Check the logs: `docker logs <container_id>`
2. Run interactively to debug: `docker run -it --rm mlops-pipeline /bin/bash`

## GitHub Actions Integration

The Docker image will be automatically built and tested in GitHub Actions when you push to the main branch. The CI/CD pipeline includes:

1. **Test Suite**: Runs pytest to validate code
2. **Train and Quantize**: Trains model and performs quantization
3. **Build and Test Container**: Builds Docker image and tests predictions

## Free Docker Alternatives

If you can't install Docker Desktop, you can use:

1. **GitHub Codespaces** (Free tier available)
2. **GitPod** (Free tier available)
3. **GitHub Actions** (Free tier available)

These cloud-based solutions can run Docker containers without local installation. 