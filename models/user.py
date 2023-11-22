#!/usr/bin/python3
"""This module defines a class User"""
import os
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from models.base_model import BaseModel, Base

HBNB_TYPE_STORAGE = os.getenv('HBNB_TYPE_STORAGE')

class User(BaseModel, Base):
    """This class defines a user by various attributes"""
    __tablename__ = 'users'
    if HBNB_TYPE_STORAGE == 'db':
        email = Column(String(128), nullable=False)
        password = Column(String(128), nullable=False)
        first_name = Column(String(128), nullable=False)
        last_name = Column(String(128), nullable=False)
        places = relationship('Place', cascade='delete', backref='user')
        reviews = relationship('Review', cascade='delete', backref='user')
    else:
        email = ""
        password = ""
        first_name = ""
        last_name = ""
