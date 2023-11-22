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
        time_format = "%Y-%m-%dT%H:%M:%S.%f"
        if kwargs:
            from models import storage
            # Creates BaseModel from dictionary.
            # Converts datetime string values into datetime object values.
            # del kwargs["__class__"]
            for key, value in kwargs.items():
                if key == "created_at" or key == "updated_at":
                    datetime_obj = datetime.strptime(value, time_format)
                    setattr(self, key, datetime_obj)
                elif key != "__class__":
                    setattr(self, key, value)
        else:
            from models import storage
            # Instantiate id, created_at & update_at to default values
            # upon instantiation of an object.
            self.id = str(uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            # storage.new(self)

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
        dictionary = dict(self.__dict__)
        dictionary["__class__"] = str(type(self).__name__)
        dictionary["created_at"] = self.created_at.isoformat()
        dictionary["updated_at"] = self.updated_at.isoformat()

        if '_sa_instance_state' in dictionary.keys():
            del dictionary['_sa_instance_state']

        return dictionary

    def delete(self):
        """ deletes the current instance from the storage """
        from models import storage
        storage.delete(self)
