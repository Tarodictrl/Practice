from scipy import integrate
import math
import matplotlib.pyplot as plt
import numpy as np

def f(x):
    return 1/(math.sqrt(x+3)+math.sqrt((x+3)**3))

f2 = np.vectorize(f)
v, err = integrate.quad(f, -2, 0)
x = np.arange(-2, 0, 0.01)
print("Значение интеграла: ", v)

plt.title(f"График функции")
plt.grid()
plt.xlabel("Значения x")
plt.ylabel("Значения функции f(x)")
plt.plot(x, f2(x), 'b-')
plt.show()