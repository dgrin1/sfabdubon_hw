import numpy as np
import matplotlib.pyplot as plt

# constants
G = 6.67430e-11 # Newton's gravitational constant
M = 1.989e30 # mass of the Sun

# initial conditions
x0 = 4e12 # in meters
y0 = 0
vx0 = 0
vy0 = 500 # in m/s



# function to calculate derivatives
def f(r, t):
    x = r[0]
    vx = r[1]
    y = r[2]
    vy = r[3]
    fx = vx
    fvx = -G * M * x / (r1 ** 3)
    fy = vy
    fvy = -G * M * y / (r1 ** 3)
    return np.array([fx, fvx, fy, fvy], float)

#Calculate period of comet's orbit
T = 2 * np.pi * np.sqrt(x0 ** 3 / (G * M))

a = 0.0
b = 2*T
# time step
h = 50 # in seconds
nsteps = int((b-a )/ h)
print(nsteps)
tpoints = np.zeros(nsteps)
xpoints = np.zeros(nsteps)
ypoints = np.zeros(nsteps)
max_periods = 2*T
r = np.array([x0, y0,  vx0, vy0], float)
for i in range(nsteps):   # uses the fourth-order Runge-Kutta
    t = i * h
    tpoints[i] = t
    xpoints[i] = r[0]
    ypoints[i] = r[2]
    r1 = np.sqrt(r[0]**2 + r[2]**2)
    # xpoints.append(r[0])
    # ypoints.append(r[2])
    k1 = h * f(r, t)
    k2 = h * f(r + 0.5 * k1, t + 0.5 * h)
    k3 = h * f(r + 0.5 * k2, t + 0.5 * h)
    k4 = h * f(r + k3, t + h)
    r += (k1 + 2 * k2 + 2 * k3 + k4) / 6
    print(xpoints)
    if a>b:
        break

# function to perform one step of the Runge-Kutta method
# def rk4_step(t, y, h, f):
#     k1 = h * f(t, y)
#     k2 = h * f(t + h/2, y + k1/2)
#     k3 = h * f(t + h/2, y + k2/2)
#     k4 = h * f(t + h, y + k3)
#     return y + (k1 + 2*k2 + 2*k3 + k4)/6

# simulation time
# Calculate period of comet's orbit
# T = 2 * np.pi * np.sqrt(x0 ** 3 / (G * M))# 
# tmax 
# nsteps = int(tmax / h)
# print(tmax)
# # arrays to store the results
# t_arr = np.zeros(nsteps)
# x_arr = np.zeros(nsteps)
# y_arr = np.zeros(nsteps)

# # set initial conditions
# y = np.array([x0, y0, vx0, vy0])

# perform the simulation
# for i in range(nsteps):
#     t = i * h
#     tpoints[i] = t
#     xpoints[i] = y[0]
#     ypoints[i] = y[1]
#     # y = rk4_step(t, y, h, f)

# plot the results
plt.plot(xpoints, ypoints)
plt.xlabel('x (m)')
plt.ylabel('y (m)')
plt.title(" Trajecty of the Comet ")
plt.show()
