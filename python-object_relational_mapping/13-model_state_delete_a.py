#!/usr/bin/python3

"""
This script connects to a MySQL database, retrieves all State objects,
deletes those whose names contain the letter 'a', and prints the id
and name of the remaining states.
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

    states = session.query(State).order_by(State.id).all()

    for state in states:
        if 'a' in state.name:
            session.delete(state)
        else:
            print("{}: {}".format(state.id, state.name))

    session.commit()
    session.close()
