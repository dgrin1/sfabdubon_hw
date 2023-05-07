import numpy as np
from numpy import array, empty, arange
from numpy.linalg import solve 



R =1 #the all the resistor have the same resistance
V_plus = 5

#create the matrix using the equations for the junctions 
A = array([[ 4, -1, -1, -1],
            [ -1, 3, 0, -1 ],
            [ -1, 0, 3, -1 ],
            [ -1, -1, -1, 4]], float)
v = array([ 5, 0, 5, 0 ],float) #define the solution for Ax = v
x = solve(  A, v)

print(f"V1 = {x[0]:.2f} V")
print(f"V2 = {x[1]:.2f} V")
print(f"V3 = {x[2]:.2f} V")
print(f"V4 = {x[3]:.2f} V")