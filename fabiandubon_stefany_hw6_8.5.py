import numpy as np
import math
import matplotlib.pyplot as plt

g =9.81 
l =0.1
theta = 0.0
C = 2.0

theta_0 = 0
omega_0 = 0
def f(r,t):
    theta = r[0]
    omega = r[1]
    ftheta = omega
    fomega = -(g/l)*np.sin(theta)+C*np.cos(theta)*np.sin(5*t)
    return np.array ([ftheta,fomega], float)

a = 0.0
b = 100.0
N= 100000
h = (b-a)/N

tpoints = np.arange(a,b,h)

thetapoints = []

r = np.array([0.0, 0.0], float)

for t in tpoints:   # uses the fourth-order Runge-Kutta
    thetapoints.append(r[0])
    k1 = h * f(r, t)
    k2 = h * f(r + 0.5 * k1, t + 0.5 * h)
    k3 = h * f(r + 0.5 * k2, t + 0.5 * h)
    k4 = h * f(r + k3, t + h)
    r += (k1 + 2 * k2 + 2 * k3 + k4) / 6
# print("t",thetapoints)
#plot
plt.plot(tpoints, thetapoints)
plt.xlabel( "Time (s)")
plt.ylabel("Angle (rad) ")
plt.title(" Angle of Pendulum with Horizontal Driving Force")
plt.show()


# perform the integration for part (b)


# def d(r,t):
#     theta = r[0]
#     omega = r[1]
#     ftheta = omega
#     fomega = -(g/l)*np.sin(theta)+C*np.cos(theta)*np.sin(omega*t)
#     return np.array ([ftheta,fomega], float)
# Part (b): Finding the value of omega that makes the pendulum resonate
omega_vals = np.linspace(0, 100, 100000)
max_amplitude = -np.inf
amplitude_points = []
for t in tpoints:
    amplitude_points.append(0.0) # Initialize amplitude_points to all zeros
for omega in omega_vals:
    r = np.array([theta_0, omega], float) # Use omega as the initial value for omega_0
    for i, t in enumerate(tpoints):
        amplitude_points[i] = r[0] # Update the amplitude_points list
        k1 = h*f(r, t)
        k2 = h*f(r+0.5*k1, t+0.5*h)
        k3 = h*f(r+0.5*k2, t+0.5*h)
        k4 = h*f(r+k3, t+h)
        r += (k1+2*k2+2*k3+k4)/6
    max_amplitude_current = max(amplitude_points)
    if max_amplitude_current > max_amplitude:
        max_amplitude = max_amplitude_current
        resonant_omega = omega
        print("a", max_amplitude)
        print("m",max_amplitude_current)
        print("r",resonant_omega)
    
# Plot the resonant frequency result
print("Resonant frequency: {:.3f} Hz".format(resonant_omega/(2*np.pi)))
plt.plot(omega_vals, amplitude_points)
plt.xlabel("Time (s)")
plt.ylabel("Angle (radians)")
plt.title("Pendulum with Driven Force (Resonant Frequency) of {:.3f} Hz".format(resonant_omega/(2*np.pi)) )
plt.show()