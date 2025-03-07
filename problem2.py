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
        temp_dict = {}
        v3 = []
        i3 = []
        j3 = []

        for l in range(len(converted_dense_matrix.v)):
            temp_dict[(converted_dense_matrix.i[l],converted_dense_matrix.j[l])] =  converted_dense_matrix.v[l]
        
        for l in range(len(self.v)):
            if (self.i[l],self.j[l]) in temp_dict:
                v3.append(self.v[l] + temp_dict[(self.i[l],self.j[l])])

                temp_dict.pop((self.i[l],self.j[l]))

            else:
                v3.append(self.v[l])

            i3.append(self.i[l])
            j3.append(self.j[l])
        
        for (i,j), val in temp_dict.items():
            v3.append(val)
            i3.append(i)
            j3.append(j)
        
        result_matrix = Coo_matrix_self(v3,i3,j3)
        
        return result_matrix
    
    def multiplication(self,dense_matrix_to_multiply):
        converted_dense_matrix = build_coo_matrix_self(dense_matrix_to_multiply)
        temp_dict = {}
        result_matrix_dict = {}
        v3 = []
        i3 = []
        j3 = []

        for l in range(len(converted_dense_matrix.v)):
            temp_dict[(converted_dense_matrix.i[l], converted_dense_matrix.j[l])] = converted_dense_matrix.v[l]
        
        for l in range(len(self.v)):
            for (i2, j2), val2 in temp_dict.items():
                if self.j[l] == i2:
                    key = (self.i[l], j2)

                    if key in result_matrix_dict:
                        result_matrix_dict[key] += self.v[l]*val2
                    else:
                        result_matrix_dict[key] = self.v[l]*val2


        for (i, j), val in result_matrix_dict.items():
            v3.append(val)
            i3.append(i)
            j3.append(j)
        
        result_matrix = Coo_matrix_self(v3,i3,j3)
        return result_matrix
    
    def __str__(self):
        return f"v: {self.v}\ni: {self.i}\nj: {self.j}"


def build_coo_matrix_self(dense_matrix):
    v=[]
    i=[]
    j=[]
    row_counter=-1
    for row in dense_matrix:
        row_counter+=1
        for index, num in enumerate(row):
            if num != 0:
                v.append(num)
                i.append(row_counter)
                j.append(index)

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

def dense_matrix_sum(matrix1, matrix2):
    for i in range(len(matrix1)):
        for j in range(len(matrix1)):
            matrix1[i][j] = matrix1[i][j] + matrix2[i][j]

    return matrix1

def dense_matrix_multiplication(matrix1, matrix2):
    
    result_matrix = [[0] * len(matrix2) for _ in range(len(matrix1))]

    for i in range(len(matrix1)):
        for j in range(len(matrix2)):
            for k in range(len(matrix1)):  
                result_matrix[i][j] += matrix1[i][k] * matrix2[k][j]
    
    return result_matrix


coo_dense_matrix1 = build_coo_matrix_self(dense_matrix)
##coo_dense_matrix1.sum(dense_matrix_2)
##dense_matrix_sum(dense_matrix, dense_matrix_2)

result = dense_matrix_multiplication(dense_matrix, dense_matrix_2)
print("\n")
result_multiplied_matrix = build_coo_matrix_self(result)
print(result_multiplied_matrix)
print("\nself -->\n")
result_multiplied_matrix_self = coo_dense_matrix1.multiplication(dense_matrix_2)
print(result_multiplied_matrix_self)



#coo = coo_matrix(dense_matrix)

#csr = csr_matrix(dense_matrix)

#csc = csc_matrix(dense_matrix)



