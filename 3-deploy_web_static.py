#!/usr/bin/python3
"""Fabric script"""
from fabric.api import env
env.user = 'ubuntu'
env.hosts = ['34.75.154.27', '34.75.211.153']


def deploy():
    """This function creates a .tgz file and deploy it into the servers"""
    doPack = __import__('1-pack_web_static').do_pack
    doDeploy = __import__('2-do_deploy_web_static').do_deploy
    path = doPack()
    if path is None:
        return False
    return doDeploy(path)
