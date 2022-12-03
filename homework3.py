#Rosario Cecilio-Flores-Elie 
#Homework 3 - Exercise 5.21 Computational Methods - Fall 22

import numpy as np
import matplotlib.pyplot as plt

#Return the potential due to charge q at the origin.
def potential(q, r0, x, y, k=1):
    dis = np.hypot(x-r0[0], y-r0[1])
    return q*k/(dis+0.001)

# making the grid points and meshes for the 2D visualization.

nx,ny=100,100
x = np.linspace(-50, 50, nx)
y = np.linspace(-50, 50, ny)
X, Y = np.meshgrid(x, y)

charges = [(-1,(5,0)), (1,(-5,0))] #charge 1 and 2 with distance from origin
V=np.zeros((ny,nx))
# Calculating the potential due to charges.
for charge in charges: 
    ev = potential(*charge, x=X, y=Y)
    V+=ev
    #print(V)

#Plot for Electric Potential
fig=plt.figure(figsize=(7,7))
plt.pcolormesh(X,Y,V)
plt.title('Electric Potential')
plt.colorbar()
plt.show()

#Gradient of the Potential 
Ey, Ex= np.gradient(V,x,y)
#print(Ey,Ex)

fig, ax=plt.subplots(figsize=(6,6))

ax.streamplot(X,Y,Ex,Ey)
ax.set_aspect('equal')
ax.plot(-5,0,'-or')
ax.plot(5,0, 'ob')
ax.set_title('Electric Field in the xy plane')

plt.show()