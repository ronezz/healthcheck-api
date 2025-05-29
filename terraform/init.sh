#!/bin/bash

echo "Hello desde init.sh" > /home/ubuntu/test.txt

apt update -y
apt install -y docker.io git

systemctl start docker
systemctl enable docker

# Clonar tu repo (reemplaza con el tuyo)
git clone https://github.com/ronezz/healthcheck-api.git

cd healthcheck-api
docker build -t healthcheck-api .
docker run -d -p 80:5000 healthcheck-api
