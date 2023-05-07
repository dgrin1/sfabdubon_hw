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
h = 0.1 # in seconds
delta= 1000
nsteps = int((b-a)/h)
print(nsteps)
tpoints = np.zeros(nsteps)
xpoints = np.zeros(nsteps)
ypoints = np.zeros(nsteps)
r = np.array([x0, y0, vx0, vy0], float)
i=0
while a < b and i<nsteps:   # uses adaptive step size
    t = i * h
    tpoints[i] = t
    xpoints[i] = r[0]
    ypoints[i] = r[2]
    r1 = np.sqrt(r[0] ** 2 + r[2] ** 2)
    k1 = h * f(r, t)
    k2 = h * f(r + 0.5 * k1, t + 0.5 * h)
    k3 = h * f(r + 0.5 * k2, t + 0.5 * h)
    k4 = h * f(r + k3, t + h)
    r_new = r + (k1 + 2 * k2 + 2 * k3 + k4) / 6
    delta_r = np.sqrt(((1/30)*(r_new[0] - r[0]) ** 2) + ((1/30)*(r_new[2] - r[2]))** 2)
    h_new = 0.9 * h * (delta / delta_r) ** 0.5
   
    if h_new > h:
        h = h_new
    r += (k1 + 2 * k2 + 2 * k3 + k4) / 6
    a += h
    i += 1
    print(xpoints)
    if i>= nsteps:
        break

# truncate arrays to the actual number of steps taken
tpoints = tpoints[:i]
xpoints = xpoints[:i]
ypoints = ypoints[:i]

# plot the results
plt.plot(xpoints, ypoints)
plt.scatter(xpoints, ypoints, s=3, c= 'red')
# plt.xlim(min(xpoints), max(xpoints))
# plt.ylim(min(ypoints), max(ypoints))

plt.xlabel('x (m)')
plt.ylabel('y (m)')
plt.title("Comet's trajectory with Adjustable Step Size")
plt.show()





