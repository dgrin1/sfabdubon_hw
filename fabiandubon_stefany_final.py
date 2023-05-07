

import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import math
from math import factorial, sin
from pylab import plot,xlabel,show
import numpy as np
from numpy import linspace,sin,cos,ones,copy,tan,pi,array,arange, power, argmin
from scipy.integrate import solve_ivp
import warnings
warnings.filterwarnings("ignore")



#defining constants
x0=0#defining initial x-value
y0=0 #defining initial y-value
z0=0
v_x0= 25 #defining initial v_x value given in problem (initial velocity in x-direction)
v_y0=50 ##defining initial v_y given in problem (initial velocity in y-direction), in m/yr
v_z0=100 #defininf the initial v_z value
sigma= 10  #used in the equation
R=7 

def r_s(t):
    # define r0 here as a function of t
    return 0

def f(r, t):
    x = r[0] # x position
    v_x = r[1]  #x component of velocity
    y = r[2] #y position
    v_y = r[3] # y velocity
    z = r[4]  #z position
    v_z = r[5] #z component of velocity 
    # rad_ = np.sqrt(x ** 2 + y ** 2 + z ** 2)
    # c = 3 * 10 ** 8 #speed of light
    # gamma = 1 / np.sqrt(1 - (rad_ / c) ** 2)
    f_r = (np.tanh(sigma*(r_s(t)+R))-np.tanh(sigma*(r_s(t)-R)))/(2*np.tanh(sigma*R)) #geodesic function
    dx_dt = v_x
    dy_dt = v_y
    dz_dt = v_z
    u1=1                         #u[1]
    dvx_dt = f_r * u1**2 * dx_dt #u[2]
    dvy_dt = 0                   #u[3]
    dvz_dt = 0                   #u[4]

    return np.array([dx_dt, dvx_dt, dy_dt, dvy_dt, dz_dt, dvz_dt], float)


x_values, vx_values=[], [] #creating empty arrays for x values and x components of velocity to be stored in
y_values, vy_values=[], [] #creating empty array for y values and y components of velocity to be stored in
z_values, vz_values=[], [] #creating empty array for z values and z components of velocity to be stored in
r=array([x0, v_x0, y0, v_y0, z0, v_z0 ], float) #r vector with the first component giving the initial x coordinate, second giving the initial v_x velocity value, third giving initial y coordinate, fourth giving initial v_y velocity value
#T=2*np.pi*np.sqrt(x_0**3/(G*M))
#h=T/2000000000 #calculating step size between data points
T=200
N=5000000
h=T/N #calculating timestep
timepoints=arange(0, T, h) #creating an array of time values within the range defined by limits of integration above

for t in timepoints: #for loop to perform calculations of fourth-order Runge-Kutta method
    x_values.append(r[0]) #adds current x value (corresponding to index 0/the 0th term in the x array) to empty array defined above
    vx_values.append(r[1]) #adds current v1 value (corresponding to index 1/the 1st term in the r1 array) to empty array defined above
    y_values.append(r[2]) #adds current y value (corresponding to index 0/the 0th term in the y array) to empty array defined above
    vy_values.append(r[3]) #adds current v2 value (corresponding to index 0/the 0th term in the y array) to empty array defined above
    z_values.append(r[4]) #adds current z value (corresponding to index 0/the 0th term in the z array) to empty array defined above
    vz_values.append(r[5]) #adds current v3 value (corresponding to index 0/the 0th term in the z array) to empty array defined above
    #Runge-Kutta fourth-order calculations for f()
    k1=h*f(r, t) #calculating k1 in Runge-Kutta fourth-order method
    k2=h*f(r+0.5*k1,t+0.5*h) #calculating k2 in Runge-Kutta fourth-order method
    k3=h*f(r+0.5*k2,t+0.5*h) #calculating k3 in Runge-Kutta fourth-order method
    k4=h*f(r+k3,t+h) #calculating k4 in Runge-Kutta fourth-order method
    r+=(k1+2*k2+2*k3+k4)/6 #calculating r using k1,k2,k3,k4 and adding it to the current r value

print("z", z_values)
plt.figure(1) #creating first figure
plt.plot( array(x_values), array(y_values), color='purple') #plotting x and y values generated with fixed step size
plt.title('Modeling the Alcubierre Metric') #naming figure
plt.xlabel('x (km)') #labelling axes
plt.ylabel('y (km)')
# plt.savefig('orbitaldynamics.png') #saving figure with given name
# plt.show()
plt.figure(2) #creating fsecondfigure
plt.plot(  x_values, z_values, color='purple') #plotting x and z values generated with fixed step size
plt.title('Modeling the Alcubierre Metric') #naming figure
plt.xlabel('x (km)') #labelling axes
plt.ylabel('z (km)')
# create a 3D scatter plot
fig = plt.figure(3)
ax = fig.add_subplot(projection='3d')
ax.scatter(x_values, y_values, z_values, c=z_values, cmap='viridis')
ax.set_title("Modeling the Alcubierre Metric ")
ax.set_xlabel('x (km)')
ax.set_ylabel('y (km)')
ax.set_zlabel('z (km)')
plt.show()

