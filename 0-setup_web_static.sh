#!/usr/bin/env bash
# Configures a web server
apt-get update
apt-get upgrade
apt-get install -y nginx
mkdir -p /data/web_static/releases/test/
mkdir -p /data/web_static/shared/
echo "Testing nginx configuration" > /data/web_static/releases/test/index.html
ln -sf /data/web_static/releases/test/ /data/web_static/current
chown -R ubuntu:ubuntu /data/
sed -i '/server_name _;/ a location /hbnb_static/ {\n\talias /data/web_static/current/;\n\t}'  /etc/nginx/sites-available/default
service nginx restart
