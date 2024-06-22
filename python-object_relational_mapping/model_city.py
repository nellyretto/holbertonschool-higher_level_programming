#!/usr/bin/python3

"""
Module for task 14
"""
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from model_state import Base, State  # Import State here
from sqlalchemy.orm import relationship


class City(Base):
    """
    Represents a city in the database.

    Attributes:
        id (int): The unique identifier for the city.
        name (str): The name of the city.
        state_id (int): The foreign key referencing the associated state.
        state (State): The associated state object.

    """
    __tablename__ = 'cities'
    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)
    state = relationship("State")
