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
from models.base_model import Base, BaseModel
import sqlalchemy
from sqlalchemy import create_engine
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
        query_res = []
        dic = {}
        clses = [User, State, City, Amenity, Place, Review]

        if cls:
            query_res = self.__session.query(cls).all()
        else:
            query_res = []
            for cls_nam in clses:
                query_res.extend(self.__session.query(cls_nam).all())
            dic = {f"{obj.__class__.__name__}.{obj.id}": obj for obj in objs}

        return dic

    def new(self, obj):
        """ adds new object """
        self.__session.add(obj)

    def save(self):
        """ save all changes """
        self.__session.commit()

    def delete(self, obj=None):
        """ deletes an object """
        if obj:
            self.__session.delete(obj)

    def reload(self):
        """ creates all tables """
        Base.metadata.create_all(self.__engine)
        session_factory = sessionmaker(bind=self.__engine,
                                       expire_on_commit=False)
        Session = scoped_session(session_factory)
        self.__session = Session()

    def close(self):
        """
        closes the session self.__session.close()
        edit: class remove() method on the private session attribute
        """
        self.__session.remove()
