#!/usr/bin/python3


"""
    Represents a state in the database.

    Attributes:
        id (int): The unique identifier of the state.
        name (str): The name of the state.
    """

from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class State(Base):

    """
    State class that maps to the 'states' table in the database.

    Attributes:
        id (int): An auto-generated, unique integer that
        serves as the primary key. Cannot be null.
        name (str): A string with a maximum length of 128
        characters. Cannot be null.
    """
    __tablename__ = 'states'
    id = Column(Integer,
                primary_key=True,
                autoincrement=True,
                nullable=False)
    name = Column(String(128),
                  nullable=False)
