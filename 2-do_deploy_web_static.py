#!/usr/bin/python3
"""Fabric script"""
from fabric.api import put, run, env
from os.path import exists
env.user = 'ubuntu'
env.hosts = ['34.75.154.27', '34.75.211.153']


def do_deploy(archive_path):
    """Deploy new static content"""
    if exists(archive_path) is False:
        return False
    try:
        upload = put(archive_path, "/tmp/")
        name = upload[0].split("/")[2].split(".")[0]
        run("sudo mkdir -p /data/web_static/releases/{}".format(name))
        run("sudo tar -xzf /tmp/{}.tgz -C "
            "/data/web_static/releases/{}".format(name, name))
        run("sudo rm /tmp/{}.tgz".format(name))
        run("sudo mv /data/web_static/releases/{}/web_static/* "
            "/data/web_static/releases/{}/".format(name, name))
        run("sudo rm -rf /data/web_static/current")
        run("sudo ln -s /data/web_static/releases/{} "
            "/data/web_static/current".format(name))
        run("sudo rm -rf /data/web_static/current/web_static".format(name))
        return True
    except:
        return False
