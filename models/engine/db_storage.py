#!/usr/bin/python3
"""some
"""

from sqlalchemy import (create_engine)
import os
import models
from os import getenv
from models.base_model import Base
from sqlalchemy.orm import scoped_session, sessionmaker
from models.state import State
from models.city import City
from models.user import User
from models.place import Place
from models.review import Review
from models.amenity import Amenity


class DBStorage:
    """Class for MySQL database storage"""
    # Private class attributes:
    __engine = None
    __session = None
    # for @all method if @cls is None
    __classes = [State, City, User, Place, Review, Amenity]

    def __init__(self):
        """some"""
        user = os.getenv('HBNB_MYSQL_USER')
        passwd = os.getenv('HBNB_MYSQL_PWD')
        host = os.getenv('HBNB_MYSQL_HOST')
        database = os.getenv('HBNB_MYSQL_DB')

        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'.format(
            user, passwd, host, database),
            pool_pre_ping=True)

        if os.getenv('HBNB_ENV') == 'test':
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """
        query on the current database session,
        if cls != None of the class name,
        else all.
        """

        dictionary = {}
        dict_objects = {}

        if cls is not None:
            if cls not in self.__classes:
                return dictionary

            else:
                for record in self.__session.query(cls).order_by(cls.id):
                    dictionary.update(
                            {"{}.{}".format(type(record).__name__, record.id): record})

        else:
            for obj in self.__classes:
                for record in self.__session.query(obj).order_by(obj.id):
                    dictionary.update(
                            {"{}.{}".format(type(record).__name__, record.id): record})

        return dictionary

    # this method must return a dictionary: (like FileStorage)

    def new(self, obj):
        """add the object to the current database session"""
        # add the object to the current database session (self.__session)
        self.__session.add(obj)

    def save(self):
        """commit all changes of the current database session"""
        # commit all changes of the current database session (self.__session)
        self.__session.commit()

    def delete(self, obj=None):
        """delete from the current database session obj is not None"""
        if obj is not None:
            self.__session.delete(obj)

    def reload(self):
        """create all tables in the database"""
        # create all tables in the database
        Base.metadata.create_all(self.__engine)
        # create the current database session - from the engine
        create_db = sessionmaker(bind=self.__engine, expire_on_commit=False)
        Session = scoped_session(create_db)
        # invokes sessionmaker.__call__()
        self.__session = Session()
        # work with session

    def close(self):
        """Close current session"""
        self.__session.close()
