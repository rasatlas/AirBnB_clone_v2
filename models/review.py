#!/usr/bin/python3
""" Review module for the HBNB project """
import os
from sqlalchemy import Column, String, ForeignKey
from models.base_model import BaseModel, Base


HBNB_TYPE_STORAGE = os.getenv('HBNB_TYPE_STORAGE')

class Review(BaseModel, Base):
    """ Review class to store review information """
    __tablename__ = 'reviews'
    if HBNB_TYPE_STORAGE == 'db':
        place_id = Column(String(60), ForeignKey('places.id'), nullable=False)
        user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
        text = Column(String(1024), nullable=False)
    else:
        place_id = ""
        user_id = ""
        text = ""
