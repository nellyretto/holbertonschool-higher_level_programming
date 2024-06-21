#!/usr/bin/python3


"""
    This script retrieves a State object from the database
    based on the given state name.
    If the state is found, it prints the state's id and name.
    Otherwise, it prints "Not found".
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

    search_state_name = sys.argv[4]

    state = session.query(State).filter(State.name ==
                                        search_state_name).first()

    if state:
        print(state.id)
    else:
        print("Not found")

    session.close()
