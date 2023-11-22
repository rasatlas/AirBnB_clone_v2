#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from models.engine.file_storage import FileStorage
from models.city import City


HBNB_TYPE_STORAGE = os.getenv('HBNB_TYPE_STORAGE')


class State(BaseModel, Base):
    """ State class """
    __tablename__ = "states"
    name = Column(String(128), nullable=False)

    if HBNB_TYPE_STORAGE == "db":
        cities = relationship("City", cascade="delete", backref="state")
    else:
        @property
        def cities(self):
            """getter attribute cities that returns the list of City instances
               with state_id equals to the current State.id
            """
            return [city for city in FileStorage.storage.all(City)
                    if self.id == city.state.id]
