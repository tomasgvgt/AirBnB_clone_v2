#!/usr/bin/env bash
# Bash script that sets up your web servers for the deployment of web_static
# Install nginx if not already installed
excec { 'configuration':
    command  => 'sudo apt-get -y update;
                command -v nginx || sudo apt-get -y install nginx;
                mkdir -p /data/web_static/shared;
                mkdir -p /data/web_static/releases/test;
                echo "Testing Nginx configuration" > /data/web_static/releases/test/index.html;
                ln -sf /data/web_static/releases/test /data/web_static/current;
                chown -hR ubuntu:ubuntu /data/;
                sed -i  "/listen 80 default_server/a\\tlocation /hbnb_static/ {\n\t\talias
                /data/web_static/current/;\n\t}\n" /etc/nginx/sites-available/default;
                sudo service nginx restart;',
    provider => 'shell',
}
