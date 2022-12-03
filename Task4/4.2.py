import sympy as sp

def f_1(x):
    return x*sp.ln(x)

def f_2(x):
    return 1/(sp.sqrt(x**2-x-1))

x = sp.symbols('x')

res_1 = sp.integrate(f_1(x), x)
res_2 = sp.integrate(f_2(x), x)
print(res_1)
print(res_2)