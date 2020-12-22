#!/usr/bin/python3
"""Fabric script"""
from fabric import operations
from datetime import datetime


def do_pack():
    """This function generates a .tgz file"""
    try:
        operations.local("mkdir -p versions")
        path = "versions/web_static_{}.tgz".format(
                datetime.strftime(datetime.now(), "%Y%m%d%H%M%S"))
        operations.local(
            "tar -cvzf {} web_static".format(path))
        return path
    except Exception:
        return None
