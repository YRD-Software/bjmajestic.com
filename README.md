
# Majestic Web

## Get Started

### Developing on local environment

`pip install -r requirements.txt`

### Developing using Docker Compose
`docker-compose up -f docker-compose.dev.yml`

## Docker Compose Files

The project's docker compose files are divided into two categories: **production** and **development**. 
- Production: [docker-compose.yml](https://github.com/frankjlin16/majesticWebDev/blob/main/docker-compose.yml)
- Development: [docker-compose.dev.yml](https://github.com/frankjlin16/majesticWebDev/blob/main/docker-compose.dev.yml)

## SSH Configuration for Azure

The files [sshd_config](https://github.com/frankjlin16/majesticWebDev/blob/main/sshd_config) and [ssh_setup.sh](https://github.com/frankjlin16/majesticWebDev/blob/main/ssh_setup.sh) are files that enbles SSH feature for container running on Azure.

## Azure Container Startup File

The file [startup.txt](https://github.com/frankjlin16/majesticWebDev/blob/main/startup.txt) contains the commands that will be executed when starting Azure container.