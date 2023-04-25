#!/usr/bin/python3
# Fabric script that generates a .tgz archive from the contents of web_static

from fabric.api import local
from fabric.decorators import task
from datetime import datetime
import os


@task
def do_pack():
    """ Method generates a .tgz archive contents of the web_static """

    local("mkdir -p versions")

    
    now = datetime.now()
    date_string = now.strftime("%Y%m%d%H%M%S")
    new_dir_name = "versions/web_static_{}.tgz".format(date_string)
    local(f'tar cvzf {new_dir_name} web_static')

    if os.path.exists(new_dir_name):
        return new_dir_name
    else:
        return None

