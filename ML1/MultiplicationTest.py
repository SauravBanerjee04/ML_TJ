#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 19 14:50:35 2021

@author: sauravbanerjee
"""

import math

def listmaker(x):
    b = []
    for m in range(x):
        b.append(0)
    return b

def creatematrix(y,x):
    m = []
    for b in range(y):
        m.append(listmaker(x))
    return m 

def mult(A,B):
    if not (len(A[0]) == len(B)):
        print("Error")
        return None
    result = [[sum(a * b for a, b in zip(A_row, B_col)) for B_col in zip(*B)] for A_row in A]
    return result


print(mult([[1,]],[[1]]))
a = [[1,2,3,4,5],[1,2,3,4,5],[1,2,3,4,5],[1,2,3,4,5]]
b = [[1,2,3],[1,2,3],[1,2,3],[1,2,3],[1,2,3]]
print(mult(a,b))




tfs = "T1"
linear = lambda x:x
def ramp(x):
    if(x >=0):
        return x
    else:
        return 0
logistic = lambda x: 1/(1+math.exp(-x)) 
t4 = lambda x: 2*logistic(x) - 1
activation = None
if tfs == "T1":
    activation = linear
elif tfs== "T2":
    activation = ramp
elif tfs == "T3":
    activation = logistic
else:
    activation = t4

def vectorize(matrix,act):
    for x in range(len(matrix)):
        for y in range(len(matrix[0])):
            matrix[x][y] = act(matrix[x][y])
    return matrix

print(vectorize(mult(a,b),logistic))