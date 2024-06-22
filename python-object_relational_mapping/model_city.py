#!/usr/bin/python3


from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from model_state import Base

Base = declarative_base()


class City(Base):
    """
    City class represents a city in the database.

    Attributes:
        id (int): The unique identifier for the city.
        name (str): The name of the city.
    """

    __tablename__ = 'cities'
    id = Column(Integer,
                primary_key=True,
                autoincrement=True,
                nullable=False)
    name = Column(String(128),
                  nullable=False)
