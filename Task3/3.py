import numpy as np
import pandas as pd

a = np.random.rand(5, 5)
b = np.random.rand(5, 5)
c = np.random.rand(5, 4)
d = np.random.rand(4, 5)

x1 = 21.98
x2 = 87.25
n = 5
m = 3


g = np.dot((a-b), (np.dot(c, d)-np.dot(b, a)))
g_x1 = g + x1
g_x2 = g - x2

det_g = np.linalg.det(g)
reverse_g = np.linalg.inv(g)
test_g = np.round(np.dot(g, reverse_g))
rank_g = np.linalg.matrix_rank(g)
q = np.array(np.linalg.eigvals(g))
w = np.linalg.eig(g)[1]
diag_q = np.diag(q)

a_2 = g[n-1]
b_2 = g[:, m-1]
norm_a_2 = np.linalg.norm(a_2)
norm_b_2 = np.linalg.norm(b_2)
ort_a_2 = a_2 / norm_a_2
ort_b_2 = b_2 / norm_b_2
y = np.arccos(np.dot(a_2, b_2) / (norm_a_2 * norm_b_2))

print("Матрица A:=\n", pd.DataFrame(a))
print("Матрица B:=\n", pd.DataFrame(b))
print("Матрица C:=\n", pd.DataFrame(c))
print("Матрица D:=\n", pd.DataFrame(d))
print("Матрица G:=", pd.DataFrame(g))
print("Матрица G + x1:=\n", pd.DataFrame(g_x1))
print("Матрица G - x2:=\n", pd.DataFrame(g_x2))
print("Определитель матрицы G:=\n", det_g)
print("Обратная матрица G:=\n", pd.DataFrame(reverse_g))
print("Проверка обратной матрицы G:=\n", pd.DataFrame(test_g, dtype=int))
print("Ранг матрицы G:= ", rank_g)
print("Собственные значения матрицы G:=\n", q)
print("Собственные векторы матрицы G:=\n", w)
print("W * diag(Q):=\n", pd.DataFrame(np.dot(w, diag_q)))
print("G * W:=\n", pd.DataFrame(np.dot(g, w)))
print("Матрица A_2:=\n", pd.DataFrame(a_2))
print("Матрица B_2:=\n", pd.DataFrame(b_2))
print("Норма матрицы A_2:=\n", norm_a_2)
print("Норма матрицы B_2:=\n", norm_b_2)
print("Ортогональная матрица A_2:=\n", pd.DataFrame(ort_a_2))
print("Ортогональная матрица B_2:=\n", pd.DataFrame(ort_b_2))
print("Проверка ортогональности матриц A_2 и B_2:= ", np.dot(ort_a_2, ort_b_2))
print("Сумма векторов A_2 и B_2:= ", (np.sum(a_2)+np.sum(b_2)))
print("Количество положительных элементов в матрице A_2:= ", len(a_2[a_2>=0]))
print("Количество положительных элементов в матрице B_2:= ", len(b_2[b_2>=0]))
print("Количество отрицательных элементов в матрице A_2:= ", len(a_2[a_2<0]))
print("Количество отрицательных элементов в матрице B_2:= ", len(b_2[b_2<0]))
print("Сколярное произведение векторов A_2 и B_2:= ", np.dot(a_2, b_2))
print("cos(y):= ", np.cos(y))
print("sin(y):= ", np.sin(y))
print("Перекрестное произведение векторов:= ", norm_a_2 * norm_b_2 * np.sin(y))
print("Умножение векторных координат A_2 и B_2:=\n", pd.DataFrame(np.multiply(a_2, b_2)))
