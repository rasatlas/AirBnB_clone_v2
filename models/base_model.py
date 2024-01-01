#!/usr/bin/python3
"""This module defines a base class for all models in our hbnb clone"""
from uuid import uuid4
from datetime import datetime
from sqlalchemy import Column, String, DateTime
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class BaseModel:
    """A base class for all hbnb models"""
    id = Column(String(60), nullable=False, primary_key=True)
    created_at = Column(DateTime, nullable=False, default=datetime.utcnow())
    updated_at = Column(DateTime, nullable=False, default=datetime.utcnow())

    def __init__(self, *args, **kwargs):
        """Instatntiates a new model"""
        from models import storage

        self.id = str(uuid4())
        self.created_at = datetime.utcnow()
        self.updated_at = datetime.utcnow()
        time_format = "%Y-%m-%dT%H:%M:%S.%f"
        if kwargs:
            # Creates BaseModel from dictionary.
            # Converts datetime string values into datetime object values.
            # del kwargs["__class__"]
            if "updated_at" in kwargs:
                kwargs["updated_at"] = datetime.strptime(
                    kwargs["updated_at"], time_format
                )
            if "created_at" in kwargs:
                kwargs["created_at"] = datetime.strptime(
                    kwargs["created_at"], time_format
                )
            if "__class__" in kwargs:
                del kwargs["__class__"]
            self.__dict__.update(kwargs)

    def __str__(self):
        """Returns a string representation of the instance"""
        cls = (str(type(self)).split('.')[-1]).split('\'')[0]
        return '[{}] ({}) {}'.format(cls, self.id, self.__dict__)

    def save(self):
        """Updates updated_at with current time when instance is changed"""
        from models import storage
        self.updated_at = datetime.now()
        storage.new(self)
        storage.save()

    def to_dict(self):
        """Convert instance into dict format"""
        dictionary = {}
        dictionary.update(self.__dict__)
        dictionary.update({'__class__':
                          (str(type(self)).split('.')[-1]).split('\'')[0]})
        dictionary["created_at"] = self.created_at.isoformat()
        dictionary["updated_at"] = self.updated_at.isoformat()

        if '_sa_instance_state' in dictionary.keys():
            del dictionary['_sa_instance_state']

        return dictionary

    def delete(self):
        """ deletes the current instance from the storage """
        from models import storage
        storage.delete(self)
