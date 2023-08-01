#!/usr/bin/python3
"""a script that prints the State object with the name passed as argument"""
import sys
from sqlalchemy import create_engine, select
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

    # charge l'objet
    new_name_db = session.execute(select(State).filter_by(id=2)).scalar_one()

    # Met à jour l'objet et l'element en bdd
    new_name_db.name = "New Mexico"

    session.commit()

    session.close()
