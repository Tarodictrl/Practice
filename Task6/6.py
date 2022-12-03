import numpy as np
from scipy import interpolate
import matplotlib.pyplot as plt

x = np.array(
    [6.046 , 3.613, 9.76, 8.958, 9.535, 2.017, 3.555, 2.91, 0.9961, 7.093]
)
y = np.array(
    [3.408, 4.32, 4.094, 0.1542, 2.987, -2.601, 4.053, 0.8441, -2.391, -1.324]
)

f = interpolate.interp1d(x, y)
f2 = interpolate.interp1d(x, y, kind="quadratic")
f3 = interpolate.interp1d(x, y, kind="cubic")
xnew = np.linspace(x.min(), x.max(), 100)
plt.plot(xnew, f(xnew), '-', xnew, f2(xnew), '--', xnew, f3(xnew), ':')
plt.legend(['linear','quadratic', 'cubic'], loc='best')
plt.show()
