#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if matrix is None:
        return
    # pour chaque ligne i
    for i in range(len(matrix)):
        # pour chaque colonne j dans la ligne i
        for j in range(len(matrix[i])):
            # imprime l'élément à la ligne i, colonne j
            print("{}".format(matrix[i][j]), end=" ")
        print("")
