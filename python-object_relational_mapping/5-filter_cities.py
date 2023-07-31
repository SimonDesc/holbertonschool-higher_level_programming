#!/usr/bin/python3
"""script that takes in the name of a state as an argument"""


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
        SELECT cities.name
        FROM cities, states
        WHERE states.id = cities.state_id
        AND BINARY states.name = %s
        ORDER BY states.id ASC
        """,
        (state_name_db,),
    )

    # Récupération des résultats
    results = cursor.fetchall()

    # Affichage des résultats
    city_list = []
    for city in results:
        city_list.append(city[0])
    # Assembler la liste en une seule chaîne
    city_str = ", ".join(city_list)
    print(city_str)

    # Femeture de la connexion
    db.close()
