import numpy as np
import math
import matplotlib.pyplot as plt
#defined constants 
g = 9.81
l = 0.1 
theta = (179 *np.pi)/180 #initial angle
def f(r,t):
    theta = r[0]
    omega = r[1]
    ftheta = omega
    fomega = -(g/l)*np.sin(theta)
    return np.array ([ftheta,fomega], float)
 
#initial values
a= 0.0
b= 10.0
N=1000
h = (b-a)/N

#time points
tpoints = np.arange(a,b,h)

thetapoints = []
r = np.array([theta, 0.0], float)


for t in tpoints:   # uses the fourth-order Runge-Kutta
    thetapoints.append(r[0])
    k1 = h * f(r, t)
    k2 = h * f(r + 0.5 * k1, t + 0.5 * h)
    k3 = h * f(r + 0.5 * k2, t + 0.5 * h)
    k4 = h * f(r + k3, t + h)
    r += (k1 + 2 * k2 + 2 * k3 + k4) / 6

#plot
plt.plot(tpoints, thetapoints)
plt.xlabel( "Time (s)")
plt.ylabel("Angle (rad) ")
plt.title(" Angle as a function of time")
plt.show()

#animation
