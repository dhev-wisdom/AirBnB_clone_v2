#!/usr/bin/python3
# Write a Fabric script (based on the file 1-pack_web_static.py)
# that distributes an archive to your web servers, using the function do_deploy

from fabric.api import put, env, run
from os import path


env.hosts = ["34.232.53.58", "54.80.207.49"]

def do_deploy(archive_path):
    if path.exists(archive_path):
        put(archive_path, "/tmp/")

        # Extract the contents of the archive into the new dir
        archive_name = archive_path.split('/')[-1]
        archive_basename = archive_path.split('.')[0]

        run('mkdir -p /data/web_static/releases/{}/'.format(archive_basename))
        run('tar -xzf /tmp/{} -C /data/web_static/releases/{}/'.format(archive_name, archive_basename))

        # Create a symbolic link from the new directory to the current version of the site
        run('sudo rm -rf /data/web_static/current')

        # Check if files were unpacked direcly in releases folder
        # or in sub-directory web_static
        num_file = run('ls -1 /data/web_static/releases/{}/ | wc -l'.format(archive_basename))
        if num_file > 8:
            run('sudo ln -sf /data/web_static/releases/{}/ /data/web_static/current'.format(archive_basename))
        else:
            run('sudo ln -sf /data/web_static/releases/{}/web_static/ /data/we_static/current'.format(archive_basename))

        # Delete archive
        run('sudo rm /tmp/{}'.format(archive_name))

        # Set the ownership and permissions of the new files
        run('sudo chown -R ubuntu:ubuntu /data/')
        run('sudo chmod 755 /data/')

        return True
    else:
        return False
