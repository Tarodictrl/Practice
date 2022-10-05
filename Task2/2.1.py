# Вариант - 9
import numpy as np


def Cramer(a, b) -> list:
    det = np.linalg.det(a)
    r = []
    for i in range(len(a)):
        vm = np.copy(a)
        vm[:, i] = b
        r.append(round(np.linalg.det(vm) / det))
    return r


a = np.array([
    [6, -4, -8, -2],
    [3, 2, -1, -3],
    [-1, -2, -2, -6],
    [2, 4, 1, -8]
])

b = np.array([
    -8,
    -9,
    44,
    17,
])

answer = Cramer(a, b)
print("Answer:=", answer)

