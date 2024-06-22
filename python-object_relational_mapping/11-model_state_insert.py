#!/usr/bin/python3


"""
This script inserts a new state into the database using
SQLAlchemy.

The script takes three command-line arguments:
- sys.argv[1]: MySQL username
- sys.argv[2]: MySQL password
- sys.argv[3]: MySQL database name

The script performs the following steps:
1. Creates a SQLAlchemy engine using the provided MySQL
credentials.
2. Creates the necessary tables in the database using
the Base.metadata.create_all() method.
3. Creates a session using sessionmaker and binds it to
the engine.
4. Creates a new State object with the name 'Louisiana'.
5. Adds the new State object to the session.
6. Commits the changes to the database.
7. Queries all the states from the database and prints
their IDs and names.
8. Closes the session.

Note: This script assumes that the 'model_state' module is
imported and contains the necessary SQLAlchemy models.
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

    c1 = State(name='Louisiana')
    session.add(c1)
    session.commit()
    print(c1.id)

    session.close()
