#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from os import getenv


class State(BaseModel, Base):
    """ State class """
    __tablename__ = 'states'
    if getenv('HBNB_TYPE_STORAGE') == 'db':
        name = Column(String(128), nullable=False)
        cities = relationship("City", cascade="all, delete",
                                backref='state')

    else:
        name = ""

        @property
        def cities(self):
            from models import storage
            from models.city import City
            temp = []
            dictio = storage.all(City)
            for value in dictio.values():
                if value.state_id == self.id:
                    temp.append(value)
            return temp
