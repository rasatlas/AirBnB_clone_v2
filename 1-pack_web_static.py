#!/usr/bin/python3
# Fabric script that generates a .tgz archive

import os
from fabric import task
from datetime import datetime
from fabric.operations import local


@task
def do_pack():
    time_stamp = datetime.now().strftime('%Y%m%d%H%M%S')
    output_dir = 'versions'
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    archive_name = f'web_static_{time_stamp}.tgz'
    ouput_path = os.path.join(output_dir, archive_name)

    result = local(f'tar -czf {output_path} web_static')
    if result.succeeded:
        return output_path
    else:
        return None
