#!/usr/bin/env python3

from scipy.sparse import csr_matrix, csc_matrix, coo_matrix
import numpy as np

# Matriz densa de ejemplo
dense_matrix = [
    [0, 0, 3, 0],
    [2, 0, 0, 0],
    [0, 7, 0, 0],
    [0, 0, 0, 5]
]

def coo_matrix_self(matrix):
    v=[]
    i=[]
    j=[]
    row_counter=-1
    for row in matrix:
        row_counter+=1
        for num in row:
            if num != 0:
                v.append(num)
                i.append(row_counter)
                j.append(row.index(num))
                print(f"\n[!]num:{num}, row:{row_counter}, column: {row.index(num)}")
    print(v)
    print(i)
    print(j)
#coo = coo_matrix(dense_matrix)

#csr = csr_matrix(dense_matrix)

#csc = csc_matrix(dense_matrix)

coo_matrix_self(dense_matrix)

