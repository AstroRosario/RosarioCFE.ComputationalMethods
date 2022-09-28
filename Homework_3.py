'''Rosario Cecilio-Flores-Elie Homework 3 - Exercise 5.21 Computational Methods - Fall 22'''

import numpy as np
import matplotlib.pyplot as plt

#Return the potential due to charge q at the origin.
def potential(q, r0, x, y, k=1):
    dis = np.hypot(x-r0[0], y-r0[1])
    return q*k/(dis+0.001)

# making the grid points and meshes for the 2D visualization.
x = np.linspace(-50, 50, 100)
y = np.linspace(-50, 50, 100)
X, Y = np.meshgrid(x, y)

charges = [(-1,(5,0)), (1,(-5,0))] #charge 1 and 2 with distance from origin

# Calculating the potential due to charges.
for charge in charges: 
    ev = potential(*charge, x=X, y=Y)
    V +=ev
    print(V)

#Plot for Electric Potential
fig=plt.figure(figsize=(7,7))
plt.pcolormesh(X,Y,V)
plt.title('Electric Potential')
plt.colorbar()
plt.show()

#Gradient of the Potential 
Ey, Ex= np.gradient(V,x,y)
print(Ey,Ex)

#Plot for Electric Field
fig,ax=plt.subplots(figsize=(7,7))
color = np.log(np.hypot(Ex, Ey)) 
ax.streamplot(X,Y,Ex,Ey,color=color, linewidth=0.6, density=1)
ms=15
ax.set_aspect('equal')
ax.plot(-5,0, '-or', markersize=ms)
ax.plot(5,0, '-ob', markersize=ms)
plt.title('Electric Field')
plt.tight_layout()
plt.show()