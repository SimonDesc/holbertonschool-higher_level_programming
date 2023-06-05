#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if matrix is None:
        return
    for i in range(len(matrix)): # pour chaque ligne i
        for j in range(len(matrix[i])): # pour chaque colonne j dans la ligne i
            print("{}".format(matrix[i][j]), end=" ") # imprime l'élément à la ligne i, colonne j
        print("")



"""
M = [[3, 1, 5], [9, 8, -1], [10, 12, 2]]
M[1] = [9, 8, -1]
M[1][2] = -1
A[0][-1] = 5


matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
matrix[1] = 4 5 6



"""
