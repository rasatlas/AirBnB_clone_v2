#!/usr/bin/python3
# Fabric script that generates a .tgz archive

import os
import tarfile
from fabric.api import local
from datetime import datetime


def do_pack():
    """
    A Fabric script that generates a .tgz archive from the contents of the
    web_static folder of your AirBnB Clone repo, using the function do_pack.
    Prototype: def do_pack():
    - All files in the folder web_static must be added to the final archive
    - All archives must be stored in the folder versions (your function should
    create this folder if it doesn’t exist)
    - The name of the archive created must be
    web_static_<year><month><day><hour><minute><second>.tgz
    - The function do_pack must return the archive path if the archive has
    been correctly generated. Otherwise, it should return None
    """

    time_stamp = datetime.now().strftime('%Y%m%d%H%M%S')
    output_dir = "versions"
    if not os.path.isdir(output_dir):
        os.mkdir(output_dir)

    archive_name = "web_static_{}.tgz".format(time_stamp)
    ouput_path = os.path.join(output_dir, archive_name)

    with tarfile.open(output_path, "w:gz") as tar:
        tar.add("web_static")

    if os.path.exists(output_path):
        return output_path
    else:
        return None
