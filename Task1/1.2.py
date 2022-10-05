# Вариант - 15
import numpy as np
import matplotlib
import matplotlib.pyplot as plt

matplotlib.use('TkAgg')

xval = np.linspace(-10, 10)
yval = xval.copy()

x, y = np.meshgrid(xval, yval)
z = ((x ** 3) + (x ** 2)) / (x * np.sin(y))

fig = plt.figure(figsize=(14, 9))
ax = plt.axes(projection='3d')

plt.title("График поверхности")
plt.xlabel("Значение X")
plt.ylabel("Значение Y")
ax.plot_surface(x, y, z)
plt.show()
