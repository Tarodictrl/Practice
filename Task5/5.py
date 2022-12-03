import numpy as np
from sympy import *

x = Symbol('x')
y = atan(sqrt(4*x**2-1))
x0 = 1
print("Первая производная y:=", y.diff(x))
print("Первая производная в точке x0:=", y.diff(x).subs(x, x0))
print("Вторая производная в точке x0:=", y.diff(x).diff(x).subs(x, x0))