#!/usr/bin/python3
"""_summary_
"""

from sqlalchemy import (create_engine)
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

        user = getenv('HBNB_MYSQL_USER')
        passwd = getenv('HBNB_MYSQL_PWD')
        host = getenv('HBNB_MYSQL_HOST')
        database = getenv('HBNB_MYSQL_DB')

        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}:{}'
                                      .format(user, passwd, host, database),
                                      pool_pre_ping=True)

        if getenv('HBNB_ENV') == 'test':
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """some"""
        # query on the current database session
        self.__session.query(models.classes[cls]).all()
        
        # if cls=None, query all types of objects (User, State, City, Amenity, Place and Review)
            # key = <class-name>.<object-id>
            # value = object
        
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
        """some"""
        # create all tables in the database
        self.__session = Base.metadata.create_all(self.__engine)
        # create the current database session - from the engine
        create_current_db = sessionmaker(bind=self.__engine, expire_on_commit=False)
        Session = scoped_session(create_current_db)
        # invokes sessionmaker.__call__()
        self.__session = Session()
        # work with session
