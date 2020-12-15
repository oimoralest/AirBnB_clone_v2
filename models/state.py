#!/usr/bin/python3
""" State Module for HBNB project """
import models
from models.base_model import BaseModel, Base
from models.city import City
from os import getenv
import sqlalchemy
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship


class State(BaseModel, Base):
    """ State class """
    if getenv("HBNB_TYPE_STORAGE") == "db":
        __tablename__ = "states"
        name = Column(String(128), nullable=False)
        cities = relationship("City", backref="state")
    else:
        @property
        def cities(self):
            """ Get a list of all related City current states"""
            cities = models.storage.all(City)
            listCities = []
            for classId, city in cities.items():
                if city.state_id == self.id:
                    listCities.append(city)
            return listCities
