#!/usr/bin/python3
"""
1. generates a .tgz archive from
the contents of the web_static folder
of your AirBnB Clone repo, using the function do_pack.
2. Distributes an archive to your web servers, using the function do_deploy
"""
from fabric.api import run, local, put, env
from os.path import exists, getsize
import time
env.hosts = ["35.237.179.51", "34.73.191.248"]


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


def do_deploy(archive_path):
    """distributes an archive to your web servers"""
    if exists(archive_path) is False:
        return False
    try:
        put(archive_path, '/tmp/')
        filename = archive_path.split("/")[-1]
        filename_noextension = filename.split(".")[0]
        folder1 = "/data/web_static/releases/"
        folder2 = "/data/web_static/current"
        folder3 = folder1 + filename_noextension
        run("sudo mkdir -p {}".format(folder3))
        run("sudo tar -xzf /tmp/{} -C {}".format(filename, folder3))
        run("sudo rm /tmp/{}".format(filename))
        run("sudo mv {}/web_static/* {}/".format(folder3, folder3))
        run("sudo rm -rf {}/web_static".format(folder3))
        run("sudo rm -rf {}".format(folder2))
        run("sudo ln -s {}/ {}".format(folder3, folder2))
        return True
    except Exception:
        return False
