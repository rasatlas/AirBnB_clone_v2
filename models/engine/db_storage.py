#!/usr/bin/python3
"""
engine linked to mysql database which manages storage
"""
import os
from models.user import User
from models.city import City
from models.place import Place
from models.state import State
from models.review import Review
from models.amenity import Amenity
from models.base_model import Base
from sqlalchemy import create_engine, inspect
from sqlalchemy.orm import sessionmaker, scoped_session

HBNB_MYSQL_USER = os.getenv('HBNB_MYSQL_USER')
HBNB_MYSQL_PWD = os.getenv('HBNB_MYSQL_PWD')
HBNB_MYSQL_HOST = os.getenv('HBNB_MYSQL_HOST')
HBNB_MYSQL_DB = os.getenv('HBNB_MYSQL_DB')
HBNB_ENV = os.getenv('HBNB_ENV')


class DBStorage:
    """ class connects to MySQL server """
    __engine = None
    __session = None
    Session = None

    def __init__(self):
        """ creates new instance """
        self.__engine = create_engine(
            'mysql+mysqldb://{}:{}@{}/{}'.format(HBNB_MYSQL_USER,
                                                 HBNB_MYSQL_PWD,
                                                 HBNB_MYSQL_HOST,
                                                 HBNB_MYSQL_DB),
            pool_pre_ping=True,
        )

        if (HBNB_ENV == 'test'):
            # Create an inspector to get table names
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """
        Query on the current database session.
        """
        objects = dict()
        all_classes = (User, State, City, Amenity, Place, Review)
        if cls is None:
            for class_type in all_classes:
                query = self.__session.query(class_type)
                for obj in query.all():
                    obj_key = '{}.{}'.format(obj.__class__.__name__, obj.id)
                    objects[obj_key] = obj
        else:
            query = self.__session.query(cls)
            for obj in query.all():
                obj_key = '{}.{}'.format(obj.__class__.__name__, obj.id)
                objects[obj_key] = obj
        return objects

    def new(self, obj):
        """ adds new object """
        if obj is not None:
            try:
                self.__session.add(obj)
                self.__session.flush()
                self.__session.refresh(obj)
            except Exception as ex:
                self.__session.rollback()
                raise ex

    def save(self):
        """ save all changes """
        self.__session.commit()

    def delete(self, obj=None):
        """ deletes an object """
        if obj is not None:
            self.__session.query(type(obj)).filter(
                    type(obj).id == obj.id).delete(
                    synchronize_session=False
            )

    def reload(self):
        """ creates all tables """
        Base.metadata.create_all(self.__engine)
        session_factory = sessionmaker(bind=self.__engine,
                                       expire_on_commit=False)
        self.__session = scoped_session(session_factory)()

    def close(self):
        """ closes the session """
        self.__session.close()
