#!/usr/bin/env bash
# script that sets up your web servers for the deployment of web_static

if ! dpkg -s nginx > /dev/null 2>&1; then
	sudo apt update -y && sudo apt upgrade -y
	sudo apt install nginx -y
fi

# Create files and dirs if they don't exist
sudo mkdir -p /data/
sudo mkdir -p /data/web_static/
sudo mkdir -p /data/web_static/releases/
sudo mkdir -p /data/web_static/shared/
sudo mkdir -p /data/web_static/releases/test/

# Create a html file to test Nginx configuration
html="/data/web_static/releases/test/index.html"
sudo touch $html
sudo printf %s "<!DOCTYPE html>\n<html>\n\t<head>\n\t\t<title>Test Page</title>\n\t</head>\n\t<body>\n\t\t<h1>Holberton School!</h1>" > $html
#sudo printf %s "\n\t\t<p>This is a test page for Nginx configuration.</p>\n\t</body>\n</html>" >> $html

# Create a symbolic link
link_="/data/web_static/current"
link_to="/data/web_static/releases/test/"

if [ -L $link_ ]
then
	sudo rm -f "$link_"
else
	sudo ln -s "$link_to" "$link_"
fi

# Give ownership of /data/ folder to ubuntu user and group
sudo chown -R ubuntu:ubuntu /data/

# Update the Nginx configuration to serve the content of
# /data/web_static/current/ to hbnb_static

# Create a backup of the original configuration file
sudo cp /etc/nginx/sites-available/default /etc/nginx/sites-available/default.bak

# Update the configuration file
# Delete any previous for /hbnb_static

# sudo sed -i '/location \/hbnb_static/d' /etc/nginx/sites-available/default

# Delete any line containing alias /data/web_static/content

# sudo sed -i '/\t\talias \/data\/web_static\/current;\n\t}/d' /etc/nginx/sites-available/default

# sudo sed -i '/location \/hbnb_static {/,/}/d' /etc/nginx/sites-available/default

# sudo sed -E -i -e '/^[^#]*location \/hbnb_static[[:space:]]*{/,\n/^\}/d' /etc/nginx/sites-available/default
# sudo sed -E -i -e '/^[^#]*location \/hbnb_static[[:space:]]*\{/,/^\}/d' /etc/nginx/sites-available/default
sudo sed -i '/^[^#]*location \/hbnb_static[[:space:]]*{/,/^\s*}$/d' /etc/nginx/sites-available/default


# Add new location for /hbnb_static
sudo sed -i '0,/^[^#]*server {/s//&\n\tlocation \/hbnb_static {\n\t\talias \/data\/web_static\/current;\n\t}/' /etc/nginx/sites-available/default
# sudo sed -i '0,/^[^#]*server {/s//&\n\tlocation \/hbnb_static {\n\t\talias \/data\/current;\n\t}/' <filename>


#Reload nginx
sudo service nginx reload

# exit
exit 0
