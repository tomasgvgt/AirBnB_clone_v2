#!/usr/bin/python3
# Write a Fabric script that generates a .tgz archive from
# the contents of the web_static folder
# of your AirBnB Clone repo, using the function do_pack.
from fabric.api import run, local, put
import time
from os.path import getsize


def do_pack():
    """Creates a .tgz file"""
    local("mkdir -p versions")
    file_name = "web_static_" + str(time.strftime("%Y%m%d%H%M%S")) + ".tgz"
    try:
        local("tar -cvzf versions/{:s} web_static".format(file_name))
        bytes_size = getsize('./versions/{}'.format(file_name))
        path_string = "versions/{:s}".format(file_name)
        print("web_static packed: versions/{} -> {}Bytes".format(
            filename, bytes_size))
        return path_string
    except Exception:
        return None
