#!/usr/bin/env bash
# Bash script that sets up your web servers for the deployment of web_static
# Install nginx if not already installed
sudo apt-get -y update
command -v nginx || sudo apt-get -y install nginx
# Create the folder /data/web_static/shared/ if it doesn’t already exist
mkdir -p /data/web_static/shared
# Create the folder /data/web_static/releases/test/ if it doesn’t already exist
mkdir -p /data/web_static/releases/test
# Create a fake HTML file /data/web_static/releases/test/index.html
# (with simple content, to test your Nginx configuration)
echo "Testing Nginx configuration" > /data/web_static/releases/test/index.html
# Symbolic link /data/web_static/current linked to the /data/web_static/releases/test/ folder.
ln -sf /data/web_static/releases/test /data/web_static/current
# Give ownership of the /data/ folder to the ubuntu user AND group
chown -hR ubuntu:ubuntu /data/
# Update the Nginx configuration to serve the content of /data/web_static/current/ to hbnb_static
sed -i  '/listen 80 default_server/a\\tlocation /hbnb_static/ {\n\t\talias /data/web_static/current/;\n\t}\n' /etc/nginx/sites-available/default
# Restart nginx
sudo service nginx restart
