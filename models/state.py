#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from models.__init__ import storage
from models.city import City


class State(BaseModel, Base):
    """ State class """
    __tablename__ = "states"
    name = Column(String(128), nullable=False)
    cities = relationship("City", backref="state")

    @property
    def cities(self):
        """ Get a list of all related City current states"""
        cities = storage.all(City)
        listCities = []
        for classId, city in cities.items():
            if city.state_id == self.id:
                listCities.append(city)
        return listCities
