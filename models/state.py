#!/usr/bin/python3
""" State Module for HBNB project """
import os
from models.city import City
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from models.base_model import BaseModel, Base
from models.engine.file_storage import FileStorage

HBNB_TYPE_STORAGE = os.getenv('HBNB_TYPE_STORAGE')


class State(BaseModel, Base):
    """ State class """
    __tablename__ = "states"
    if HBNB_TYPE_STORAGE == "db":
        name = Column(String(128), nullable=False)
        cities = relationship("City", backref="state")
    else:
        name = ""

        @property
        def cities(self):
            """getter attribute cities that returns the list of City instances
               with state_id equals to the current State.id
            """

            from models.city import City
            from models.__init__ import storage

            list_object = []
            buf = storage.all(City)
            for key, val in buf.items():
                if self.id == val.state_id:
                    list_object.append(val)
            return list_object
