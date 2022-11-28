#Exercise 10.8 - Calcuate a value for the integral

import numpy as np
from scipy import integrate
import random

#function being evaluated
def f(x): 
    #integral
    return 1.0/((np.exp(x)+1.0)*np.sqrt(x))

def w(x):
    return 0.5/np.sqrt(x)

def inv(x):
    return 1/2*np.sqrt(x)

rng=np.random.default_rng()
N=1000000
x=rng.random(N)
p=inv(x)
q=f(p)/w(p)

print(np.mean(q))
print(integrate.quad(f,0,1))

