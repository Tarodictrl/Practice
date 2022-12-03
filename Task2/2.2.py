# Вариант - 22

import numpy as np
import pandas as pd

matrix = np.array([
    [5, 1, 2, 3, 10, -2],
    [4, 0, 5, -8, -2, 6],
    [0, 12, 2, -2, -2, -1],
    [2, 15, 0, -16, 8, 16],
    [2, -12, -3, 1, -3, 6],
    [-8, 11, -8, 1, 1, 7]
], dtype=float)

b = np.array([
    -39,
    -6,
    61,
    36,
    -71,
    50
])

def Gauss(matrix: np.array, b: np.array):
    matrix = np.c_[matrix, b]
    for nrow, row in enumerate(matrix):
        divider = row[nrow]
        row /= divider
        for lower_row in matrix[nrow+1:]:
            factor = lower_row[nrow]
            lower_row -= factor*row
    for nrow in range(len(matrix)-1,0,-1):
        row = matrix[nrow]
        for upper_row in matrix[:nrow]:
            factor = upper_row[nrow]
            upper_row[-1] -= factor*row[-1]
            upper_row[nrow] = 0
    return np.array(matrix, dtype=int)[:,-1]

print(pd.DataFrame(matrix, index=["x1", "x2", "x3", "x4", "x5", "x6"],
      columns=["x1", "x2", "x3", "x4", "x5", "x6"]))
print("b:=", b)
print("Answer:=", Gauss(matrix, b))