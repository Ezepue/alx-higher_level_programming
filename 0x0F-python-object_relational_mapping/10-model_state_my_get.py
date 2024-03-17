#!/usr/bin/python3
'''
prints the State object with the name passed
as argument from the database hbtn_0e_6_usa
'''

from sys import argv
from model_state import Base, State
from sqlalchemy import create_engine, asc
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(argv[1], argv[2], argv[3]),
                           pool_pre_ping=True)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    with Session() as session:
        all_state = session.query(State).filter(
            State.name.like(argv[4])).order_by(asc(State.id)).first()
        if all_state:
            print(all_state.id)
        else:
            print("Not found")
