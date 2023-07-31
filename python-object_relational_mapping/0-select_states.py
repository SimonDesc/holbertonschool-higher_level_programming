#!/usr/bin/python3
"""lists all states from database """

import MySQLdb
import sys


user_db = sys.argv[1]
passwd_db = sys.argv[2]
name_db = sys.argv[3]

# Connexion à la BDD 
db = MySQLdb.connect(host="localhost", user=user_db, passwd=passwd_db, db=name_db, port=3306)

# Création d'un curseur
cursor = db.cursor()

# Exécution de requêtes SQL
cursor.execute("SELECT * FROM states")

# Récupération des résultats
results = cursor.fetchall()

# Affichage des résultats
for element in results:
    print(element);

# Femeture de la connexion
db.close()

