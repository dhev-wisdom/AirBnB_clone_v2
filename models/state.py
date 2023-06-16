#!/usr/bin/python3
""" State Module for HBNB project """

import models
from models.base_model import BaseModel, Base
from models.city import City
from sqlalchemy.orm import relationship
from sqlalchemy import Column, String
from os import getenv


class State(BaseModel, Base):
    """ State class """
    if models.is_type == 'db':
        __tablename__ == 'states'
        name = Column(String, nullable=False)
        cities = relationship('City', backref='state', cascade='delete')
    else:
        name = ""

    if models.is_type != 'db':
        @property
        def cities(self):
            list_cities = []
            all_cities = models.storage.all(City).values()
            for city in all_cities:
                if city.state_id == self.id:
                    list_cities.append(city)
            return list_cities
