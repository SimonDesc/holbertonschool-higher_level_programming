#!/usr/bin/python3
"""a script that prints the State object with the name passed as argument"""
import sys
from sqlalchemy import create_engine, select, delete
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
    # Ouvre une session
    session = Session(engine)

    # charge les objets
    delete_name_db = session.query(State).filter(State.name.like("%a%")).all()

    # delete
    for state in delete_name_db:
        session.delete(state)

    session.commit()

    session.close()
