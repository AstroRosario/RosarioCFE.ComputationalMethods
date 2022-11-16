#Homework - 6 Brownian Motion

import numpy as np
import matplotlib.pyplot as plt
import random
from random import choice
from matplotlib.animation import FuncAnimation

#setting the brownian random walk
L=101 # boundaries of lattice where particle must remain
x,y= 50,50 #starting points for i,j
X,Y=[],[]
n=1000000
for t in range(n):
    dx,dy=([(1,0),(-1,0),(0,1),(0,-1)]) #random walk particle moving right,left,up,down
    x,y= x+dx, y+dy
    X.append(x)
    Y.append(y)


#setting for animation
fig=plt.figure()
axis=plt.axes(xlim=(0,100), ylim=(0,100))
plt.plot(X,Y, color='purple')
plt.title('Brownian Motion in Lattice')
plt.xlabel('i', fontsize=12)
plt.ylabel('j', fontsize=12)
plt.grid()

line,=axis.plot(X,Y, lw=2)

def init():
    line.set_data([],[])
    return line, 

def animation(i):
    X.append(x)
    Y.append(y)

    plt.title('Brownian Motion in Lattice')
    plt.xlabel('i', fontsize=12)
    plt.ylabel('j', fontsize=12)
    
    return line,

anim=animation.FuncAnimation(fig,animation,init_func=init,frames=500,interval=20, blit=True)
plt.show()


