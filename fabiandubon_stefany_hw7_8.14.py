from numpy import array,arange

# Constants
m = 9.1094e-31     # Mass of electron
hbar = 1.0546e-34  # Planck's constant over 2*pi
e = 1.6022e-19     # Electron charge
L = 20*1e-11    # Bohr radius
N = 1000
h = L/N
V0= 50*e
a= 1e-11
# Potential function
def V(x):
    return V0*(x**2)/(a**2)    #First potential V(x) asked
    # return V0*(x**4)/(a**4)   Second potential V(x) used
    

def f(r,x,E):
    psi = r[0]
    phi = r[1]
    fpsi = phi
    fphi = (2*m/hbar**2)*(V(x)-E)*psi
    return array([fpsi,fphi],float)

# Calculate the wavefunction for a particular energy
#value of the wave function Psi(L)
def solve(E):
    psi = 0.0
    phi = 1.0
    r = array([psi,phi],float)

    for x in arange(-10*a,10*a,h):
        k1 = h*f(r,x,E)
        k2 = h*f(r+0.5*k1,x+0.5*h,E)
        k3 = h*f(r+0.5*k2,x+0.5*h,E)
        k4 = h*f(r+k3,x+h,E)
        r += (k1+2*k2+2*k3+k4)/6

    return r[0]

# Main program to find the energies using the secant method
E1 = 0.0
E2 = e
psi2 = solve(E1)

# Ground state energy
target = e/1000
while abs(E1-E2)>target:
    psi1,psi2 = psi2,solve(E2)
    E1,E2 = E2,E2-psi2*(E2-E1)/(psi2-psi1)
print("Ground state energy =",E2/e,"eV")
# print (psi1, psi2)
# First excited state energy
E3 = 2*e
psi3 = solve(E2)
target = e/1000
while abs(E2-E3)>target:
    psi2,psi3 = psi3,solve(E3)
    E2,E3 = E3,E3-psi3*(E3-E2)/(psi3-psi2)
print("First excited state energy =",E3/e,"eV")

# Second excited state energy
E4 = 4*e
psi4 = solve(E3)
target = e/1000
while abs(E3-E4)>target:
    psi3,psi4 = psi4,solve(E4)
    E3,E4 = E4,E4-psi4*(E4-E3)/(psi4-psi3)
print("Second excited state energy =",E4/e,"eV")

