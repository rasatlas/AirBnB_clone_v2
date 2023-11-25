#!/usr/bin/python3
""" State Module for HBNB project """
import os
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship
from models.place import place_amenity

HBNB_TYPE_STORAGE = os.getenv("HBNB_TYPE_STORAGE")


class Amenity(BaseModel, Base):
    """ a class of amenities """
    __tablename__ = 'amenities'
    if HBNB_TYPE_STORAGE == "db":
        name = Column(String(128), nullable=False)
        place_amenities = relationship('Place', secondary=place_amenity,
                                       viewonly=False)
    else:
        name = ""
