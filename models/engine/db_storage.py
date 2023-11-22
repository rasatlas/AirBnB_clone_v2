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
# HBNB_MYSQL_HOST = os.getenv('HBNB_MYSQL_HOST')
HBNB_MYSQL_DB = os.getenv('HBNB_MYSQL_DB')
HBNB_ENV = os.getenv('HBNB_ENV')


class DBStorage:
    __engine = None
    __session = None

    def __init__(self):
        self.__engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.
                                      format(HBNB_MYSQL_USER, HBNB_MYSQL_PWD,
                                             HBNB_MYSQL_DB),
                                      pool_pre_ping=True)

        if (HBNB_ENV == 'test'):
            # Create an inspector to get table names
            inspector = inspect(self.__engine)

            # Get all table names in the database
            table_names = inspector.get_table_names()

            for table_name in table_names:
                self.__session.execute(f'DROP TABLE {table_name};')

    def all(self, cls=None):
        """
        Query on the current database session.
        """
        query_result = []
        dictionary_obj = {}

        if not cls:
            classes = [User, State, City, Amenity, Place, Review]
            for item in classes:
                query_result.extend(self.__session.query(item).all())
        else:
            query_result = self.__session.query(cls).all()

        for obj in query_result.items():
            key = f"{type(obj).__name__}.{obj.id}"
            dictionary_obj[key] = obj

        return dictionary_obj

    def new(self, obj):
        self.__session.add(obj)

    def save(self):
        self.__session.commit()

    def delete(self, obj=None):
        if obj:
            self.__session.delete(obj)

    def reload(self):
        Base.metadata.create_all(self.__engine)
        session_factory = sessionmaker(bind=self.__engine,
                                       expire_on_commit=False)
        Session = scoped_session(session_factory)
        self.__session = Session()
