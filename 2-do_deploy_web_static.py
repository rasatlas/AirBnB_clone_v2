#!/usr/bin/python3
# A Fabric script that distributes archive to web servers

import os
import gzip
import shutil
import tarfile
from fabric import Connection
from fabric.api import put
from fabric.api import run
from fabric.api import env


def do_deploy(archive_path):
    """
    A Fabric script (based on the file 1-pack_web_static.py) that distributes
    an archive to your web servers, using the function do_deploy:
    - Prototype: def do_deploy(archive_path):
    - Returns False if the file at the path archive_path doesn’t exist
    - The script should take the following steps:
        - Upload the archive to the /tmp/ directory of the web server
        - Uncompress the archive to the folder
        /data/web_static/releases/<archive filename without extension>
        on the web server
        - Delete the archive from the web server
        - Delete the symbolic link /data/web_static/current from the web server
        - Create a new the symbolic link /data/web_static/current on the web
        server, linked to the new version of your code
        (/data/web_static/release/<archive filename without extension>)
    - All remote commands must be executed on your both web servers
    (using env.hosts = ['<IP web-01>', 'IP web-02'] variable in your script)
    - Returns True if all operations have been done correctly, otherwise
    returns False
    - You must use this script to deploy it on your servers: xx-web-01 and
    xx-web-02
    """

    env.user = 'ubuntu'
    env.hosts = ['100.25.20.203', '18.235.243.68']
    key_path = '~/.ssh/school'
    connect_kwargs = {'password': key_path}
    source = archive_path
    base_file_name = os.path.basename(source)
    file_name = os.path.splitext(base_file_name)[0]
    upload_destination = '/tmp/'
    unzipped_destination = '/data/web_static/releases/'

    if not os.path.exists(source):
        return False

    # con = Connection(env.hosts, env.user, connect_kwargs=connect_kwargs)

    put(source, upload_destination)

    upload_file_path = upload_destination + base_file_name
    extract_dir = unzipped_destination + file_name
    uncompress = """
    with tarfile.open(upload_file_path, r:gz) as tar:
        tar.extractall(path=extract_dir)
    """
    run(uncompress)
    sudo('rm -rf upload_file_path')
    val = sudo('ln -sf extract_dir /data/web_static/current')

    if val.succeeded:
        return True
    else:
        return False
