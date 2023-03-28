#!/usr/bin/python3
""" State Module for HBNB project """
import os
import models
from models.base_model import BaseModel, Base
from os import getenv
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship


class State(BaseModel, Base):
    """ State class """
    __tablename__ = 'states'

    # for DBStorage
    name = Column(String(128), nullable=False)
    cities = relationship(
            'City', backref="state",
            cascade="all, delete, delete-orphan")

    if os.getenv("HBNB_TYPE_STORAGE") != "db":
        @property
        def cities(self):
            """some"""
            list_of_cities = []
            for key, value in models.storage.all().items():
                if value.__class__.__name__ == 'City' and \
                        value.state_id == self.id:
                    list_of_cities.append(value)
            return list_of_cities
