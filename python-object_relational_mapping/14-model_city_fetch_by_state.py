#!/usr/bin/python3

"""
    This script fetches all cities along with their
    corresponding states from the database.
    It uses SQLAlchemy to establish a connection to
    the database and retrieve the data.
    The script takes three command-line arguments: the
    username, password, and database name.
    """

import sys
from model_state import Base, State
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from model_city import City

if __name__ == "__main__":

    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)
    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()

    cities = session.query(City, State).join(State, State.id ==
                                             City.state_id).order_by(
                                                 City.id).all()

    for city, state in cities:
        print("{}: ({}) {}".format(state.name, city.id, city.name))

    session.close()
