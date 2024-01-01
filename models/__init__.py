#!/usr/bin/python3
"""
This module instantiates an object of class FileStorage or DBStorage
"""
from os import getenv
from models.engine.db_storage import DBStorage
from models.engine.file_storage import FileStorage

HBNB_TYPE_STORAGE = getenv('HBNB_TYPE_STORAGE')


if HBNB_TYPE_STORAGE == 'db':
    storage = DBStorage()
else:
    storage = FileStorage()
storage.reload()
