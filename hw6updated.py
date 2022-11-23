#Excercise 10.3: Brownian motion

import numpy as np
import matplotlib.pyplot as plt
from matplotlib import animation
import random

import time as clock 

start=clock.time()

fig, ax = plt.subplots(figsize=(8,8))
bound = 50
n = 1000#000

ax.set_xlim(-bound,bound)
ax.set_ylim(-bound,bound)
ax.set_title('Brownian Motion in Lattice; n = '+str(n)+' steps')
ax.set_xlabel('i', fontsize=12)
ax.set_ylabel('j', fontsize=12)
ax.grid() 

# define the possible moves at each step of the random walk
dirs = np.array([[0,1],[0,-1],[1,0],[-1,0]]) # up, down, right, left

#define a numpy array to hold the locations visited on the random walk
locations=np.zeros((1,2))#2D array of zeros for x and y data

#define a function to make the animation 
def run(i):
    global locations
    global bound

    #first frame
    if i==0:
        line, =ax.plot([],[], lw=2)
        ax.plot(0,0,'ro')
        return line

    #generating a step of the random walk
    r=random.randrange(4) #4 directional options
    move= dirs[r] #pick random direction
    nextloc = [locations[-1] + move] # take previous location and move randomly
    locations=np.append(locations, nextloc, axis=0) #updated location

    #set the plot data
    xdata=locations[:,0] #current location in x
    ydata=locations[:,1] #current location in y

    ax.cla() #clearing the previous plot 

    #update the plot limits

    ax.set_xlim(min(-bound, min(xdata)-1), max(bound,max(xdata)+1))
    ax.set_ylim(min(-bound,min(ydata)-1), max(bound,max(ydata)+1))

    #redraw the plot
    line, = ax.plot([],[], lw=2, color='purple')
    line.set_data(xdata, ydata) #append current location

    #plot current position of random walk
    ax.plot(locations[-1,0], locations[-1,1], color='red', marker='o')
    ax.set_title('Brownian Motion in Lattice; n = '+str(n)+' steps')
    ax.set_xlabel('i', fontsize=12)
    ax.set_ylabel('j', fontsize=12)
    ax.grid() 

    return line 

anim=animation.FuncAnimation(fig, run, frames=n, interval=100)
anim.save('Brownian_motion.mp4', fps=30,extra_args=['-vcodec', 'libx264'])
plt.show()

end=clock.time()
runtime=end-start
if runtime>60:
    print('runtime took ', runtime/60, 'minutes')
else:
    print('runtime took ', runtime, 'seconds')


