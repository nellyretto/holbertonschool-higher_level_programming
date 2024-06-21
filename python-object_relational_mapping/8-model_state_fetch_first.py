#!/usr/bin/python3


"""
This script fetches the first state from the database using SQLAlchemy.

The script takes three command line arguments: the username,
password, and database name.
It establishes a connection to the MySQL database using the
provided credentials.
Then it creates a session and queries the State table to fetch
the first state.
If a state is found, it prints the state's ID and name.
If no state is found, it prints "Nothing".
Finally, it closes the session.

Example usage:
    $ python3 8-model_state_fetch_first.py <username>
    <password> <database_name>
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

    state = session.query(State).order_by(State.id).first()

    if state:
        print("{}: {}".format(state.id, state.name))
    else:
        print("Nothing")

    session.close()
