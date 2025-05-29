#!/bin/bash

apt update -y
apt install -y docker.io git

systemctl start docker
systemctl enable docker

git clone https://github.com/ronezz/healthcheck-api.git

cd healthcheck-api
docker build -t healthcheck-api .
docker run -d -p 80:5000 healthcheck-api
