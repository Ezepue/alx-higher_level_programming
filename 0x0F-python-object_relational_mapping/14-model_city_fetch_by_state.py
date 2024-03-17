#!/usr/bin/python3
'''
Prints all City objects from the database hbtn_0e_14_usa
'''

from sys import argv

from requests import Session
from model_state import State, Base
from model_city import City
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine, asc

if __name__ == '__main__':
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(argv[1], argv[2], argv[3]),
                           pool_pre_ping=True)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)

    with Session() as session:
        result = session.query(State,
                               City).join(City).order_by(asc(City.id)).all()
        for state, city in result:
            print("{:s}: ({:d}) {:s}".format(state.name, city.id, city.name))
