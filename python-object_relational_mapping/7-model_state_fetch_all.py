#!/usr/bin/python3
"""a script that lists all State objects from the database hbtn_0e_6_usa"""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from model_state import State, Base


if __name__ == "__main__":
    user_db = sys.argv[1]
    passwd_db = sys.argv[2]
    name_db = sys.argv[3]

    # Connexion à la BDD
    engine = create_engine(
        "mysql+mysqldb://{user}:{pwd}@localhost:3306/{dbname}".format(
            user=user_db, pwd=passwd_db, dbname=name_db
        )
    )

    session = Session(engine)
    states = session.query(State).order_by(State.id).all()

    for state in states:
        print(f"{state.id}: {state.name}")
