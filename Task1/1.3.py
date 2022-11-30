import matplotlib.pyplot as plt
import numpy as np

a = 100
b = 50
t = np.arange(0, 2*np.pi, 0.1)
x = (a+b)*np.cos(2*t)
y = (a-b)*np.sin(4*t)

plt.title(f"График параметрически заданной функции (коэффициент a = {a} b = {b}).")
plt.grid()
plt.xlabel("Значения t")
plt.ylabel("Значения функции")
plt.plot(t, x, 'b-')
plt.plot(t, y, 'r-')
plt.draw()