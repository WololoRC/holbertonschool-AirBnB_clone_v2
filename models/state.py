#!/usr/bin/python3
""" State Module for HBNB project """
import models
from models.base_model import BaseModel, Base
from os import getenv
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship


class State(BaseModel, Base):
    """ State class """
    __tablename__ = 'states'

    # for DBStorage
    if getenv("HBNB_TYPE_STORAGE") == "db":
        name = Column(String(128), nullable=False)
        cities = relationship('City', backref="state", cascade="all, delete, delete-orphan")
    else:
        name = ""

        @property
        def cities(self):
            list_of_cities = []
            # relationship between State and City
            for city in models.storage.all("City").values():
                # with state_id equals to the current State.id
                if city.state_id == self.id:
                    list_of_cities.append(city)
            return list_of_cities
            # list of City with state_id equals to the current State.id
