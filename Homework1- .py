#This is exercise 3.2: Curve plotting - HW #1 

#1a.Make a plot of the so-called deltoid curve, which is defined parametrically by the equations,
#  x = 2 cos θ + cos 2θ, y = 2 sin θ − sin 2θ, where 0 ≤ θ < 2π. 
# Take a set of values of θ between zero and 2π and calculate x and y for each from the equations above,
#  then plot y as a function of x.

from cmath import cos, pi
from turtle import color
import numpy as np
import matplotlib.pyplot as plt 
import math
N=1000
#parameters we are setting for theta
theta=np.linspace(0,2*math.pi, N)
x=2*np.cos(theta)+np.cos(2*theta)
y=2*np.sin(theta)-np.sin(2*theta)


#1b. make a polar plot r=f(theta) for some function f by calculating r for a range of values of theta, 
#converting r and theta to cartesian coordinates using the standard eq. x=rcos(theta), y=rsin(theta)
#use method to make plot of the Galilaena spiral r=(theta)^2 for 0<=theta<=10pi

N=1000
theta2=np.linspace(0,10*math.pi,N)
r=theta2**2
x2=r*np.cos(theta2)
y2=r*np.sin(theta2)



#1c: using same method make a polar plot of "Fey's Function"
N2=4000
theta3=np.linspace(0,24*math.pi,N2)
r2=math.e**(np.cos(theta3))-2*np.cos(4*theta3)+(np.sin(theta3/12))**5
x3=r2*np.cos(theta3)
y3=r2*np.sin(theta3)

#plots
fig, axes=plt.subplots(nrows=1,ncols=3,figsize= (8,4), dpi=300)
plt.subplots_adjust(wspace=0.5)
axes[0].plot(x,y, color='orange')
axes[0].set_box_aspect(1)
axes[0].set_title('Deltoid curve')
axes[1].plot(x2,y2, color='green')
axes[1].set_box_aspect(1)
axes[1].set_title('Galilean Spiral')
axes[2].plot(x3,y3, color='purple',linewidth=0.7)
axes[2].set_box_aspect(1)
axes[2].set_title('Fey\'s Function')
fig.suptitle('Exercise 3.2: Curve Plotting',fontsize=14)
fig.text(0.5, 0.1, 'x', ha='center')
fig.text(0.05, 0.5, 'y', va='center', rotation='vertical')
plt.show()


