import math
import sympy as sp

x, y = sp.symbols('x y')

m = 1
n = 1
a = 16
b = 16
h = 1

E = 1
nu = 0.3
D = (E*h**3)/(12*(1-nu**2))

alpha = 0
beta = 0

def landa(m, n):
    return ( ( (m/a)**4 + 2*( ((m/a)**2)*((n/b)**2) ) + (n/b)**4 )/((m/(a*b))**2) )

print(landa(m, n))