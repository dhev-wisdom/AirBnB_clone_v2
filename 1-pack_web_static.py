#!/usr/bin/python3
# Fabric script that generates a .tgz archive from the contents of web_static

from fabric.api import local
from datetime import datetime


def do_pack():
    """ Method generates a .tgz archive contents of the web_static """

    local("cd /web_static") # move to the web_static dir

    
    now = datetime.now()
    date_string = now.strftime("%Y%m%d%H%M%S")
    new_dir_name = "web_static_" + date_string + ".tgz"
    local(f'tar czf {new_dir_name} *')
    local(f'mv {new_dir_name} ..')
    local("cd ../")

