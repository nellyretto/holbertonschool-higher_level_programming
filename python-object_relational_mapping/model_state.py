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
"""
State class
"""

class State(Base):

    __tablename__ = 'states'
    id = Column(Integer,
                primary_key=True,
                autoincrement=True,
                nullable=False)
    name = Column(String(128),
                  nullable=False)
