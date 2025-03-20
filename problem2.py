#!/usr/bin/env python3

from scipy.sparse import csr_matrix, csc_matrix, coo_matrix
import numpy as np
import time

#GLOBAL VARIABLES
dense_matrix_16x16 = []
dense_matrix_32x32 = []
dense_matrix_128x128 = []

for _ in range(16):
    dense_matrix_16x16.append([0] * 16)

for _ in range(32):
    dense_matrix_32x32.append([0] * 32)

for _ in range(128):
    dense_matrix_128x128.append([0] * 128)

values_16x16 = [(0, 2, 5), (3, 7, 9), (5, 10, 3), (12, 14, 8), (15, 4, 6)]
for i, j, val in values_16x16:
    dense_matrix_16x16[i][j] = val 

values_32x32 = [(1, 5, 7), (6, 12, 11), (15, 18, 4), (20, 22, 10), (25, 30, 3)]
for i, j, val in values_32x32:
    dense_matrix_32x32[i][j] = val

values_128x128 = [(10, 20, 15), (30, 40, 25), (50, 60, 35), (70, 80, 45), (100, 110, 55)]
for i, j, val in values_128x128:
    dense_matrix_128x128[i][j] = val


class Coo_matrix_self:

    def __init__(self,v,i,j):
        self.v = v
        self.i = i
        self.j = j
    
    def sum(self,dense_matrix_to_sum):
        converted_dense_matrix,time = build_matrix_self_time(dense_matrix_to_sum)
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
        
        return result_matrix,time
    
    def multiplication(self,dense_matrix_to_multiply):
        converted_dense_matrix,time = build_matrix_self_time(dense_matrix_to_multiply)
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
        return result_matrix,time
    
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

def build_matrix_spicy_time(matrix):
    
    start_time_library = time.time()
    coo_matrix_library = coo_matrix(dense_matrix)
    end_time_library = time.time()

    total_time_library = end_time_library - start_time_library

    return total_time_library

def build_matrix_self_time(dense_matrix):
    start_time_self = time.time()
    coo_matrix_self = build_coo_matrix_self(dense_matrix)
    end_time_self = time.time()
    total_time_self = end_time_self - start_time_self
    return coo_matrix_self,total_time_self



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

def calculate_operation_self_matrix(dense_matrix,operation):
    
    if (dense_matrix == "16x16"):
        dense_matrix = dense_matrix_16x16
    elif (dense_matrix == "32x32"):
        dense_matrix = dense_matrix_32x32
    elif (dense_matrix ==  "128x128"):
        dense_matrix = dense_matrix_128x128

    matrix_self = build_coo_matrix_self(dense_matrix)

    if operation == "MULTIPLICATION":
        operation_time_start = time.time()
        result, building_time = matrix_self.multiplication(dense_matrix)
        operation_time_end = time.time()
    elif operation == "ADDITION":
        operation_time_start = time.time()
        result, building_time = matrix_self.sum(dense_matrix)
        operation_time_end = time.time()
    print(f"\n{result}") 
    operation_time_total = operation_time_end - operation_time_start
    return building_time,operation_time_total


def calculate_operation_spicy_matrix(dense_matrix,operation,format):
    if (dense_matrix == "16x16"):
        dense_matrix = dense_matrix_16x16
    elif (dense_matrix == "32x32"):
        dense_matrix = dense_matrix_32x32
    elif (dense_matrix ==  "128x128"):
        dense_matrix = dense_matrix_128x128

    if format == "COO MATRIX":
        building_time_start = time.time()
        matrix = coo_matrix(dense_matrix)
        building_time_end = time.time()
    elif format == "CSR MATRIX":
        building_time_start = time.time()
        matrix = csr_matrix(dense_matrix)
        building_time_end = time.time()
    elif format == "CSC MATRIX":
        building_time_start = time.time()
        matrix = csc_matrix(dense_matrix)
        building_time_end = time.time()

    if operation == "MULTIPLICATION":
        operation_time_start = time.time()
        result = matrix @ matrix
        operation_time_end = time.time()
    elif operation == "ADDITION":
        operation_time_start = time.time()
        result = matrix + matrix
        operation_time_end = time.time()
        
    building_time_total = building_time_end - building_time_start
    operation_time_total = operation_time_end - operation_time_start
    operation_time_total += building_time_total
    print(f"\n[!]Matrix: {result}")
    
    return building_time_total, operation_time_total

def calculate_operation_dense_matrix(dense_matrix,operation):

    if (dense_matrix == "16x16"):
        dense_matrix = dense_matrix_16x16
    elif (dense_matrix == "32x32"):
        dense_matrix = dense_matrix_32x32
    elif (dense_matrix ==  "128x128"):
        dense_matrix = dense_matrix_128x128

    if operation == "MULTIPLICATION":
        operation_time_start = time.time()
        result = dense_matrix_multiplication(dense_matrix,dense_matrix)
        operation_time_end = time.time()
    elif operation == "ADDITION":
        operation_time_start = time.time()
        result = dense_matrix_multiplication(dense_matrix,dense_matrix)
        operation_time_end = time.time()

    operation_time_total = operation_time_end - operation_time_start

    return operation_time_total




