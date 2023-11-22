#!/usr/bin/python3
""" Place Module for HBNB project """
import os
from sqlalchemy.orm import relationship
from models.base_model import BaseModel, Base
from sqlalchemy import Column, Integer, String, Float, ForeignKey, Table

HBNB_TYPE_STORAGE = os.getenv('HBNB_TYPE_STORAGE')

relation_ap = Table("place_amenity",
                    Base.metadata,
                    Column('place_id',
                           ForeignKey('places.id'),
                           primary_key=True,
                           nullable=False),
                    Column('amenity_id',
                           ForeignKey('amenities.id'),
                           primary_key=True,
                           nullable=False))


class Place(BaseModel, Base):
    """ A place to stay """
    __tablename__ = "places"
    if HBNB_TYPE_STORAGE == 'db':
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
        reviews = relationship('Review', backref='place', cascade='delete')
        amenities = relationship('Amenity', secondary='place_amenity',
                                 viewonly=False)
        amenity_ids = []
    else:
        city_id = ""
        user_id = ""
        name = ""
        description = ""
        number_rooms = ""
        number_bathrooms = 0
        max_guest = 0
        price_by_night = 0
        latitude = 0.0
        longitude = 0.0
        amenity_ids = []

    @property
    def reviews(self):
        """ returns a list of reviews """
        review_lists = []
        dict_objs = {}

        dict_objs = storage.all("Review")

        for val in dict_objs.values():
            if (val.place_id == self.id):
                review_lists.append(val)

        return review_lists
