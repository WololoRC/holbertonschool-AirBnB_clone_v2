#!/usr/bin/python3
""" City Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey
from os import getenv


class City(BaseModel):
    """ The city class, contains state ID and name """

    if getenv("HBNB_TYPE_STORAGE") == "db":
        __tablename__ = 'cities'
        name = Column(String(128), nullable=False)
        state_id = Column(String(60), ForeignKey('state.id'))

    else:
        state_id = ""
        name = ""
