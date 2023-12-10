#!/usr/bin/python3
"""
Fabric script that generates a tgz archive from the contents of the web_static
folder of the AirBnB Clone repo
"""

from datetime import datetime
from fabric.api import local
from os.path import isdir


def do_pack():
    """
    Pack the files to an archive for deployment
    Args:
        None
    Returns:
        Path(path of the archive) - if true
        None ( if any exceptions occur)
    """
    try:
        time = datetime.now().strftime("%Y%m%d%H%M%S")
        if isdir("versions") is False:
            local("mkdir versions")
        arch_name = "versions/web_static_{}.tgz".format(time)
        local("tar -cvzf {} web_static".format(arch_name))
        return arch_name
    except:
        return None
