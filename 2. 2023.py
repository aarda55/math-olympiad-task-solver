"""
This approximates this system of equations:
+ |y + 1| = 1 ,
y + |z + 2| = 1 ,
z + |x − 2| = 1
"""
import numpy as np
from scipy.optimize import fsolve

def equations(vars):
    x, y, z = vars
    eq1 = x + abs(y + 1) - 1
    eq2 = y + abs(z + 2) - 1
    eq3 = z + abs(x - 2) - 1
    return [eq1, eq2, eq3]

initial_guess = [1000, 1000, 1000] 
solutions = fsolve(equations, initial_guess)

print("Solutions:")
for sol in solutions:
    print(sol)
