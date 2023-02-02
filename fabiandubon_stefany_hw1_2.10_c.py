import numpy as np

# set values for variables 
a1= 15.8
a2= 18.3
a3= 0.714
a4 = 23.2
l_b_e = 0
l_b_e_n = 0

#inputs for  Z
Z= int(input("Enter value for Z:"))

#If statement to see what the value for a5 is
for A in range(Z, 3*Z):      #range given in the problem 
    if (A%2!=0):
        a5= 0
    elif (A%2==0) and (Z%2==0):
        a5 = 12.0
    else:
        a5= -12.0

#Equation to calculate the nuclear binding energy B
B=a1*A - a2*(A** (2/3)) - a3*((Z**2)/(A** (1/3))) - a4*(((A-2*Z)**2)/A) + a5/(A**(1/2))

b_e_nucleon = B/A
if (b_e_nucleon > l_b_e):
    l_b_e = b_e_nucleon
    l_b_e_n = A

print("For A the most stable nucleus is",A,"and the value of the binding energy per nucleon is",l_b_e,"MeV")