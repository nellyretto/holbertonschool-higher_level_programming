#!/usr/bin/python3

"""
This script updates the name of a state in the database.

The script takes three command-line arguments: the username,
password, and database name.
It connects to the MySQL database using the provided credentials
and creates a session to interact with the database.

The script then queries the database to find the state with an id
of 2.
If the state is found, its name is updated to 'New Mexico' and the
changes are committed to the database.

Note: This script assumes the existence of a 'model_state' module that\
    defines the 'Base' and 'State' classes.
"""


import sys
from model_state import Base, State
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)
    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()

    updated_state = session.query(State).filter(State.id == 2).first()

    if updated_state:
        updated_state.name = 'New Mexico'
        session.commit()
