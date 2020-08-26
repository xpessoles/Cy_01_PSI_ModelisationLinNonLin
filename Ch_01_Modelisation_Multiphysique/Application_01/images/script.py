import numpy as np
import scipy
from scipy.optimize import brentq
import math as m

import matplotlib.pyplot as plt

def f(x):
    return np.sqrt((-10.5*x*x)**2+(x-5*x*x*x)**2)-1
sol = brentq(f,0,1)
print(sol)

x=np.linspace(0,.5,10000)
y=f(x)
"""plt.plot(x,y)
plt.show()"""

def phi(x):
    return m.degrees(-m.pi/2-m.atan(10*x)-m.atan(.5*x))
    

def mphi(x):
    return m.degrees(-m.pi/2-m.atan(10*x)-m.atan(.5*x))+140
    
print(phi(sol)+180)

sol = brentq(mphi,0,1)
print(sol)
