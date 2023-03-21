#!/usr/bin/python3
"""some
"""

from sqlalchemy import (create_engine)
import os
from os import getenv
from models.base_model import Base
import models
from sqlalchemy.orm import scoped_session, sessionmaker


class DBstorage:
    #Private class attributes:
    __engine = None
    __session = None

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
        """query on the current database session 
        all objects depending of the class name"""
        if type(cls) is str:
            cls = eval(cls) # returns the result of the evaluated expression

        dictionary = {}

        if cls is None:
            for table in self.__all_classes:
                object = self.__session.query(table)
                for one_obj in object:
                    class_name = one_obj.__class__.__name__
                    key = class_name + '.' + one_obj.id
                    dictionary[key] = one_obj
        else:
            rows = self.__session.query(cls).all()
            for obj in rows:
                key = obj.__class__.__name__ + '.' + obj.id
                dictionary[key] = obj
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
