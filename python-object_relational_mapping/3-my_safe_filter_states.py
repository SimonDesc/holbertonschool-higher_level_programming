#!/usr/bin/python3
"""lists specific states from database and prevent sql injection"""


import MySQLdb
import sys

if __name__ == "__main__":
    user_db = sys.argv[1]
    passwd_db = sys.argv[2]
    name_db = sys.argv[3]
    state_name_db = sys.argv[4]

    # Connexion à la BDD
    db = MySQLdb.connect(
        host="localhost", user=user_db, passwd=passwd_db, db=name_db, port=3306
    )

    # Création d'un curseur
    cursor = db.cursor()

    # Exécution de requêtes SQL
    cursor.execute(
        """
        SELECT cities.id, cities.name, states.name
        FROM cities, states
        WHERE states.id = cities.state_id
        AND states.name = %s
        ORDER BY cities.id ASC
        """,
        (state_name_db,),
    )

    # Récupération des résultats
    results = cursor.fetchall()

    # Affichage des résultats
    for element in results:
        print(element)

    # Femeture de la connexion
    db.close()
