#!/usr/bin/env bash
# A Bash script that sets up web servers for the deployment of web_static
if ! command -v nginx > /dev/null 2>&1
then
	sudo apt-get -y update
	sudo apt-get -y install nginx
	sudo service nginx start
fi
mkdir -p /data/web_static/releases/test/
touch /data/web_static/releases/test/index.html

printf %s "<html>
  <head>
  </head>
  <body>
    Holberton School
  </body>
</html>" > /data/web_static/releases/test/index.html

mkdir -p /data/web_static/shared/

ln -sf /data/web_static/releases/test/ /data/web_static/current

chown -R ubuntu:ubuntu /data/

printf %s "server {
    listen 80 default_server;
    listen [::]:80 default_server;
    add_header X-Served-By $HOSTNAME;
    root   /var/www/html;
    index  index.html index.htm;

    location /hbnb_static {
        alias /data/web_static/current/;
    }

    location /redirect_me {
        return 301 http://cuberule.com/;
    }

    error_page 404 /404.html;
    location /404 {
      root /var/www/html;
      internal;
    }
}" > /etc/nginx/sites-available/default

sudo service nginx restart
