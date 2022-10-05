# Вариант - 9
import numpy as np
import matplotlib
import matplotlib.pyplot as plt

matplotlib.use('TkAgg')

f = lambda x: np.sin(x - 2) / (x ** 2 + 9) if x < 0 else np.sin(x ** 2 - x - 1) / (x ** 2 + 4)
x = np.arange(-100, 100)
y = [f(v) for v in x]

plt.plot(x, y)
plt.title("График одной функции")
plt.ylabel("Значение функции")
plt.xlabel("Значение X")
plt.show()
