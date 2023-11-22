#!/usr/bin/python3
""" Place Module for HBNB project """
import os
import models
from models.review import Review
from sqlalchemy.orm import relationship
from models.base_model import BaseModel, Base
from sqlalchemy import Column, Integer, String, Float, ForeignKey

HBNB_TYPE_STORAGE = os.getenv('HBNB_TYPE_STORAGE')


class Place(BaseModel, Base):
    """ A place to stay """
    __tablename__ = "places"
    city_id = Column(String(60), ForeignKey('cities.id'), nullable=False)
    user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
    name = Column(String(128), nullable=False)
    description = Column(String(1024), nullable=False)
    number_rooms = Column(Integer, nullable=False, default=0)
    number_bathrooms = Column(Integer, nullable=False, default=0)
    max_guest = Column(Integer, nullable=False, default=0)
    price_by_night = Column(Integer, nullable=False, default=0)
    latitude = Column(Float, nullable=False)
    longitude = Column(Float, nullable=False)
    amenity_ids = []

    if HBNB_TYPE_STORAGE == 'db':
        reviews = relationship('Review', cascade='delete', backref='place')
    else:
        @property
        def reviews(self):
            return [review for review in models.storage.all(Review).values()
                    if review.place_id == self.id]
