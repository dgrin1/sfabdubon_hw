import numpy as np

G= float(6.67*10**-11 )
M= float(5.97*10**24)
R= 6371000
pi=np.pi
T_1 = 86400  #once a day
T_2= 5400    #once every 90 min
T_3= 2700    #once every 45 min

#Orbits the Earth once a day 
h_1= float(((G*M*T_1**2)/(4*3.14**2))**(1/3)-R)

print("The altitude of a satellite that orbits the Earth once a day is",h_1,"meters" )


#Orbits the earth once every 90 min
h_2= float(((G*M*T_2**2)/(4*3.14**2))**(1/3)-R)

print("The altitude of a satellite that orbits the Earth once a day is",h_2,"meters" )




#Orbits the earth once every 45 min
h_3= float(((G*M*T_3**2)/(4*3.14**2))**(1/3)-R)

print("The altitude of a satellite that orbits the Earth once a day is",h_3,"meters" )

