-- Build image
docker build -t template-image .

-- Check images
docker images

-- Run container
docker run -d --name template-container -p 88:80 -v ${pwd}:/app template-image

-- Remove container
docker rm template-container

-- Check containers
docker ps

-- Stop container
docker stop template-container

-- VSCode Extentions:
1. Dev Containers
2. Docker

-- Run docker-compose
docker-compose up
docker-compose up -d --build

-- Stop docker-compose
docker-compose down