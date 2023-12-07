#!/usr/bin/env bash
# A Bash script that sets up web servers for the deployment of web_static
if ! which nginx > /dev/null 2>&1
then
	sudo apt-get -y update
	sudo apt-get -y install nginx
	sudo service nginx start
fi
mkdir -p /data/web_static/releases/test/index.html
touch /data/web_static/releases/test/index.html
mkdir -p /data/web_static/shared
ln -sf /data/web_static/releases/test/ /data/web_static/current
chown -r ubuntu:ubuntu /data/

printf %s "server {
	location /hbnb_static {
		alias /data/web_static/current/
	}
}" > /etc/nginx/sites_available/default
sudo service nginx restart

printf %s "<html>
  <head>
  </head>
  <body>
    Holberton School
  </body>
</html>" > /data/web_static/releases/test/index.html
