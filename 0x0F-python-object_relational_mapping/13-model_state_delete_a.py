#!/usr/bin/python3
""" Made by Christian Rojas for Holberton School 2021 """

from sqlalchemy.orm import sessionmaker
from sqlalchemy import (create_engine)
from model_state import Base, State
from sys import argv

if __name__ == "__main__":
    engine = create_engine("mysql+mysqldb://{}:{}@localhost/{}"
                           .format(argv[1], argv[2], argv[3]),
                           pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    session = Session()
    for instance in session.query(State).order_by(State.id):
        if "a" in instance.name:
            session.delete(instance)
    session.commit()
