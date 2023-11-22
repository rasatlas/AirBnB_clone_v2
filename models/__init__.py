#!/usr/bin/python3
"""
This module instantiates an object of class FileStorage or DBStorage
"""
import os
from models.engine.db_storage import DBStorage
from models.engine.file_storage import FileStorage

HBNB_TYPE_STORAGE = os.getenv('HBNB_TYPE_STORAGE')


if HBNB_TYPE_STORAGE == 'db':
    storage = DBStorage()
else:
    storage = FileStorage()
storage.reload()
