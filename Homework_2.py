#Rosario Cecilio-Flores-Elie
#Homework_2-Exercise 5.3

import numpy as np
import matplotlib.pyplot as plt

#Integrating uzing trapezoid rule
def f(x):
    return np.e**(-x**2)

#setting ranges
from numpy import arange

a=0.0
b=3.0
N=100
x=np.linspace(a,b,N) #number of points in number of slices 

#defining trapezoid rule
def trapezoid(a,b,h=1.e-5):
    N = int((b-a)//h)
    s=0.5*(f(a)+f(b))
    for k in range(1,N):
        s+=f(a+k*h)

    return h*s

#Finding the value of function
print(trapezoid(a,b))
E=np.zeros(len(x))
for i in range(N):
    E[i] = trapezoid(a,x[i])

#plotting a graph
#plt.figure(figsize=(6,3))
plt.plot(x,E, color='purple')
plt.xlabel('x')
plt.ylabel('E(x)')
plt.title('E(x) vs. x')
plt.xlim(x[0],x[-1])
plt.show()