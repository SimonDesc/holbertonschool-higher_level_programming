#!/usr/bin/python3
import sys
import os

save_to_json_file = __import__("5-save_to_json_file").save_to_json_file
load_from_json_file = __import__("6-load_from_json_file").load_from_json_file

args = sys.argv
filename = "add_item.json"

# Vérifier si le fichier existe et lire son contenu
if os.path.isfile(filename):
    my_list = load_from_json_file(filename)
else:
    my_list = []

# Ajouter les nouveaux éléments à la liste
my_list.extend(args[1:])

# Sauvegarder la liste dans le fichier
save_to_json_file(my_list, filename)
