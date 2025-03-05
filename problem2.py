#!/usr/bin/env python3

from scipy.sparse import csr_matrix, csc_matrix, coo_matrix
import numpy as np
import time

#GLOBAL VARIABLES
dense_matrix = [
    [0, 2, 0, 0, 1],
    [3, 0, 0, 4, 0],
    [0, 0, 5, 0, 0],
    [0, 6, 0, 0, 7],
    [8, 0, 0, 9, 0]
]

dense_matrix_2 = [
    [0, 4, 0, 0, 0],
    [0, 0, 0, 6, 0],
    [7, 0, 0, 0, 0],
    [0, 0, 2, 0, 8],
    [0, 0, 0, 3, 0]
]

class Coo_matrix_self:

    def __init__(self,v,i,j):
        self.v = v
        self.i = i
        self.j = j
    
    def sum(self,dense_matrix_to_sum):
        converted_dense_matrix = build_coo_matrix_self(dense_matrix_to_sum)



def build_coo_matrix_self(matrix):
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
    print("v = ",v)
    print("i = ",i)
    print("j = ",j)
    coo_matrix_self = Coo_matrix_self(v,i,j)
    return coo_matrix_self

def compare_building_time(matrix):
    start_time_self = time.time()
    coo_matrix_self = build_coo_matrix_self(matrix)
    end_time_self = time.time()
    
    start_time_library = time.time()
    coo_matrix_library = coo_matrix(dense_matrix)
    end_time_library = time.time()

    total_time_self = end_time_self - start_time_self
    total_time_library = end_time_library - start_time_library

    return total_time_self, total_time_library



build_coo_matrix_self(dense_matrix)
print("\n\n")
build_coo_matrix_self(dense_matrix_2)


#coo = coo_matrix(dense_matrix)

#csr = csr_matrix(dense_matrix)

#csc = csc_matrix(dense_matrix)



