#!/usr/bin/python3
"""Fabric script"""
from fabric.api import env, local, run, put
from datetime import datetime
from os.path import exists
env.user = 'ubuntu'
env.hosts = ['34.75.154.27', '34.75.211.153']


def do_pack():
    """This function generates a .tgz file"""
    try:
        local("mkdir -p versions")
        path = "versions/web_static_{}.tgz".format(
                datetime.strftime(datetime.now(), "%Y%m%d%H%M%S"))
        local(
            "tar -cvzf {} web_static".format(path))
        return path
    except Exception:
        return None


def do_deploy(archive_path):
    """Deploy new static content"""
    if exists(archive_path) is False:
        return False
    try:
        upload = put(archive_path, "/tmp/")
        name = upload[0].split("/")[2].split(".")[0]
        run("mkdir -p /data/web_static/releases/{}".format(name))
        run("tar -xzf /tmp/{}.tgz -C "
            "/data/web_static/releases/{}".format(name, name))
        run("rm /tmp/{}.tgz".format(name))
        run("mv /data/web_static/releases/{}/web_static/* "
            "/data/web_static/releases/{}/".format(name, name))
        run("rm -rf /data/web_static/releases/{}/web_static".format(name))
        run("rm -rf /data/web_static/current")
        run("ln -s /data/web_static/releases/{} "
            "/data/web_static/current".format(name))
        return True
    except Exception:
        return False


def deploy():
    """This function creates a .tgz file and deploy it into the servers"""
    path = do_pack()
    if path is None:
        return False
    return do_deploy(path)
