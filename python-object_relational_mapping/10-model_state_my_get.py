#!/usr/bin/python3
"""a script that prints the State object with the name passed as argument"""
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
    state = session.query(State)\
        .filter(State.name == sys.argv[4])\
        .order_by(State.id)\
        .first()
    if state is None:
        print("Not found")
    else:
        print(state.id)

    session.close()
