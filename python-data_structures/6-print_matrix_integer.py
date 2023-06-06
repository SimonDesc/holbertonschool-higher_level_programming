#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if matrix == [[]]:
        print()
    for i in range(len(matrix)):
        # pour chaque colonne j dans la ligne i
        for j in range(len(matrix[i])):
            # imprime l'élément à la ligne i, colonne j
            print("{}".format(matrix[i][j]), end="")
            if (j != len(matrix) - 1):
                print("", end=" ")
        print("")
