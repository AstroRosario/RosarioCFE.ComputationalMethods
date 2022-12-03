#Rosario Cecilio-Flores-Elie
#Homework 8 - Excercise 8.7 Trajectory of a cannonball w. and w/o air resistance

import numpy as np
import matplotlib.pyplot as plt

#define the function of what were are trying to calculate
def f(r,t,R,rho,m): #equation of motion with respect to time
    g = 9.8
    C = 0.47
    x, y, vx, vy = r
    v = np.sqrt(vx ** 2 + vy ** 2)
    d = (np.pi * (R ** 2) * rho * C) * 0.5
    dvx = -d * vx * v / m
    dvy = (-d * vy * v / m) - g
    
    return(np.array([vx, vy, dvx, dvy]))

    return (np.array([vx,vy,F_vx,F_vy]))

#defining Runge-Kutta for each value
def rk4(f,r,R,rho,m,a,b,N=1000):
    h=(b-a)/N
    t_points=np.linspace(a,b,N)
    sol=np.empty((len(t_points),4))
    for i,t in enumerate(t_points):
        sol[i,:]=r
        k1=h*f(r,t,R,rho,m)
        k2=h*f(r+(0.5*k1),t+ (0.5*h),R,rho,m)
        k3=h*f(r+(0.5*k2),t+ (0.5*h),R,rho,m)
        k4=h*f(r+k3,t+h,R,rho,m)
        r+= (k1+ (2*k2) + (2*k3) + k4)/6
    
    return sol

rho=1.22
R=0.08
g=-9.8
vi=100 #m/s initial velocity
theta=30*np.pi/180 #initial angle converted to radians
m=np.arange(1,40,10)
for i in m:
    r=np.array([0,0,(vi*np.cos(theta)), (vi*np.sin(theta))])
    z=rk4(f,r,R,rho,i,0,10)
    x=z[:,0]
    y=[j for j in z[:,1] if j>0]
    plt.plot(x[:len(y)],y, label="Mass= {}kg".format(i))

t=np.linspace(0,11,10000)
x_0=(vi*np.cos(theta))* t
y_0=(vi*np.sin(theta) *t) + (0.5*g*t*t)
z_0=[i for i in y_0 if i>0]

plt.plot(x_0[:len(z_0)], z_0, color="black", label='No air resistance')
plt.xlabel('Y(m)')
plt.ylabel('Y(m)')
plt.title('Displacement of a Cannonball with Different Maasses')
plt.legend(fontsize='small')
plt.show()