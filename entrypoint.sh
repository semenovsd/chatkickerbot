#!/usr/bin/bash
#Installation for 20.04



# Download & Install % Start Docker
sudo apt-get update
sudo apt-get install -y apt-transport-https ca-certificates curl gnupg-agent software-properties-common
curl -fsSL https://get.docker.com -o get-docker.sh
sh get-docker.sh
sudo systemctl start docker

## Enable userns-remap on the daemon
sudo echo "{
  \"userns-remap\": \"default\"
}" >/etc/docker/daemon.json
sudo systemctl restart docker

# Add group docker
sudo groupadd docker
sudo usermod -aG docker "${USER}"
sudo newgrp docker

# Create ssl certificate
. .env
mkdir "${SSL_DIR}"
openssl req -newkey rsa:2048 -sha256 -nodes -keyout "${SSL_DIR}${SSL_PRIV}" -x509 -days 365 -out "${SSL_DIR}${SSL_CERT}" \
-subj "/C=US/ST=Oregon/L=Portland/O=Company Name/OU=Org/CN=${DOMAIN_NAME_OR_IP}"
sudo chmod -R +r "${SSL_DIR}"
sudo exit
