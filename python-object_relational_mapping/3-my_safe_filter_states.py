#!/usr/bin/python3
"""lists specific states from database """

import sys
from sqlalchemy import create_engine, text


if __name__ == "__main__":
    user_db = sys.argv[1]
    passwd_db = sys.argv[2]
    name_db = sys.argv[3]
    state_name_db = sys.argv[4]

    # Connexion à la BDD
    engine = create_engine(
        "mysql+mysqldb://{user}:{pwd}@localhost:3306/{dbname}".format(
            user=user_db, pwd=passwd_db, dbname=name_db
        )
    )

    # Création de la connexion à la BDD
    with engine.connect() as connection:
        # "text" s'assure que la valeur sera correctement échappée
        query = text(
            """
        SELECT * FROM states
        WHERE BINARY
        name = :value
        ORDER BY states.id ASC
        """
        )
        # Exécution de la requête
        result = connection.execute(query, {"value": state_name_db})
        # Récupération des résultats
        for row in result:
            print(row)
