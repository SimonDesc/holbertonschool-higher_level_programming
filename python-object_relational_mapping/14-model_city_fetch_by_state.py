#!/usr/bin/python3
"""contains the class definition of a City"""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from model_state import State, Base
from model_city import Base, City

if __name__ == "__main__":
    user_db = sys.argv[1]
    passwd_db = sys.argv[2]
    name_db = sys.argv[3]

    engine = create_engine(
        "mysql+mysqldb://{user}:{pwd}@localhost:3306/{dbname}".format(
            user=user_db, pwd=passwd_db, dbname=name_db
        )
    )

    session = Session(engine)
    cities = (
        session.query(State, City)
        .join(City, State.id == City.state_id)
        .order_by(City.id)
        .all()
    )

    for state_row, city_row in cities:
        print(f"{state_row.name}: ({city_row.id}) {city_row.name}")
