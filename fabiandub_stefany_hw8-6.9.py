import matplotlib.pyplot as plt
import math
import numpy as np
from numpy import linspace,sin,cos,ones,copy,tan,pi,array,arange,power,argmin
from numpy.linalg import solve,eigvalsh,eigh
from scipy.integrate import solve_ivp

#Part b

# Define constants
a = 1.6022e-18 # electron volt
M = 9.1094e-31 # kg, mass of electron
hbar = 1.056e-34 # J s, reduced Planck's constant
L = 5e-10 # m, width of well
e = 1.6022e-19 # C, charge of electron

# Define matrix dimensions
n_max = 4 # number of columns
m_max = 4 # number of rows

# Create empty matrix
H = np.zeros((n_max, m_max))

# Fill matrix using nested loops
for i in range(n_max):
    for j in range(m_max):
        n = i + 1
        m = j + 1
        if n == m:
            H[j, i] = ((hbar * np.pi)**2 / (2 * M * L**2)) * n**2 + a / 2
        elif n % 2 == 0 and m % 2 == 0 or n % 2 != 0 and m % 2 != 0:
            H[j, i] = 0
        else:
            H[j, i] = (2 * a / L**2) * (-((2 * L) / np.pi)**2) * (m * n / ((m**2 - n**2)**2))

# Calculate eigenvalues
evals = np.linalg.eigvalsh(H)
# print("H", H)
# print("ev", evals)

#part c
# Define matrix dimensions
n_max = 10 # number of columns
m_max = 10 # number of rows

# Create empty matrix
Hc= np.zeros((n_max, m_max))

# Fill matrix using nested loops
for i in range(n_max):
    for j in range(m_max):
        n = i + 1
        m = j + 1
        if n == m:
            Hc[j, i] = ((hbar * np.pi)**2 / (2 * M * L**2)) * n**2 + a / 2
        elif n % 2 == 0 and m % 2 == 0 or n % 2 != 0 and m % 2 != 0:
            Hc[j, i] = 0
        else:
            Hc[j, i] = (2 * a / L**2) * (-((2 * L) / np.pi)**2) * (m * n / ((m**2 - n**2)**2))

# Calculate eigenvalues
evals_c = np.linalg.eigvalsh(Hc)
# print("H", Hc)
# print("ev", evals)
for k in range(10):
    print(" The enery eigenvalue ", k+1, " is ", evals_c[k]/e)

#part c
# Define matrix dimensions
n_max = 100 # number of columns
m_max = 100 # number of rows

# Create empty matrix
Hd = np.zeros((n_max, m_max))

# Fill matrix using nested loops
for i in range(n_max):
    for j in range(m_max):
        n = i + 1
        m = j + 1
        if n == m:
            Hd[j, i] = ((hbar * np.pi)**2 / (2 * M * L**2)) * n**2 + a / 2
        elif n % 2 == 0 and m % 2 == 0 or n % 2 != 0 and m % 2 != 0:
            Hd[j, i] = 0
        else:
            Hd[j, i] = (2 * a / L**2) * (-((2 * L) / np.pi)**2) * (m * n / ((m**2 - n**2)**2))

# Calculate eigenvalues
evals_d = np.linalg.eigvalsh(Hd)
for k in range(10):
    print(" The energy eigenvalue  ", k+1, " is ", evals_d[k]/e)

#part e
# Calculate the eigenvalues and eigenvectors of the Hamiltonian matrix
eigenvalues, eigenvectors = eigh(Hd)

# Extract the eigenvectors corresponding to the ground state and the first two excited states
ground = eigenvectors[:, 0]
first = eigenvectors[:, 1]
second = eigenvectors[:, 2]

# Define a function to compute the wavefunction for a given state
def psi(state, x):
    psi_state = np.dot(state, np.sin(np.outer(np.arange(1, n_max+1), np.pi*x/L)))
    return 4.09 * psi_state**2

# Generate the x-values and evaluate the wavefunctions for each state
x = np.arange(0, L, 1e-12)
psi_g = psi(ground, x)
psi_f = psi(first, x)
psi_s = psi(second, x)
print(" Ground state: ", psi_g)
print(" First excited state: ", psi_f)
print("Second excited state: ", psi_s)

# Plot the probability densities
plt.plot(x, psi_g, label="Ground State")
plt.plot(x, psi_f, label="First Excited State")
plt.plot(x, psi_s, label="Second Excited State")
plt.title("Probability Density")
plt.xlabel("x")
plt.ylabel("Probability Density")
plt.legend()
plt.savefig("probdensas8.png")
plt.show()
