#!/usr/bin/python3
# A Fabric script that distributes archive to web servers

import os
import gzip
import shutil
import tarfile
from fabric.operations import sudo
from fabric.api import put, run, env, hosts


@hosts(['100.25.20.203', '18.235.243.68'])
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
    env.key_filename = '~/.ssh/school'
    source = archive_path
    base_file_name = os.path.basename(source)
    file_name = os.path.splitext(base_file_name)[0]
    upload_destination = '/tmp/'
    unzipped_destination = '/data/web_static/releases/'

    if not os.path.exists(source):
        return False

    if put(source, upload_destination).failed is True:
        print(f"Uploading archive to {upload_destination} failed")
        return False

    uploaded_file_path = os.path.join(upload_destination, base_file_name)
    extract_dir = os.path.join(unzipped_destination, file_name)
    relocate_files = extract_dir + "/web_static/*"
    empty_dir = extract_dir + "/web_static"

    sudo(f"mkdir -p {extract_dir}")
    sudo(f"tar -xzf {uploaded_file_path} -C {extract_dir}")
    sudo(f"rm {uploaded_file_path}")
    sudo(f"cp -r {relocate_files} {extract_dir}")
    sudo(f"rm -r {empty_dir}")
    sudo("rm -r /data/web_static/current")
    sudo(f"ln -s {extract_dir} /data/web_static/current")
    
    print("New version deployed!")
    return True
