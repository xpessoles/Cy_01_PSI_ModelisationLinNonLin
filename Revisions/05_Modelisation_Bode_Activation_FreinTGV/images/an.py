import math
import cmath

from scipy import *
from pylab import *
from scipy.optimize import bisect 
import matplotlib.pyplot as plt

# Question 4
Ti = 2.54 
omega = 1


Krinv= Ti *90e-3*(math.sqrt(1+Ti**2))/(math.sqrt(1+0.05**2))*(1)/(math.sqrt((1-0.01**2)**2+0.1**2))

Kr = 1/Krinv
print(Kr)

lKr = 1- math.log10(math.sqrt(Ti*Ti+1))+math.log10(Ti)
print(10**lKr)

Kr = 10**lKr


# Question 5

def h1(om):
    return (2000)/(1+om*0.1j-0.01*om*om)
def m(om):
    return 1/(1+om*0.05j)
def h2(om):
    return 45e-6/(om*1j)
def c(om):
    return Kr*(1+1/(Ti*om*1j))
    
def BO(om):
   return c(om)*h1(om)*h2(om)*m(om)
def BOnc(om):
   return h1(om)*h2(om)*m(om)
   
def argBO(om):
    return cmath.phase(BO(om))        
def argBOnc(om):
    return cmath.phase(BOnc(om))

def gBO(om):
    return 20*math.log10(abs(BO(om)))
def gBOnc(om):
    return  20*math.log10(abs(BOnc(om)))



zero1 = bisect(argBO, 0.01, 100) 
print(zero1)




ome = linspace(00.1,100,10000)

### TRACé DU MODULE
"""
ph = [math.degrees(argBO(x)) for x in ome]
pph =[ph[0]]
for i in range(len(ph)-1):
    if abs(pph[i]-ph[i])>90:
        pph.append( ph[i]-360)
    else : 
        pph.append(ph[i])
    
plt.semilogx(ome,pph)

ph = [math.degrees(argBOnc(x)) for x in ome]
pph =[ph[0]]
for i in range(len(ph)-1):
    if abs(pph[i]-ph[i])>90:
        pph.append( ph[i]-360)
    else : 
        pph.append(ph[i])
    
plt.semilogx(ome,pph)

plt.grid()
plt.show()
"""
### TRACé DU gain
gain = [gBO(x) for x in ome]    
plt.semilogx(ome,gain,".")

gain = [gBOnc(x) for x in ome]        
plt.semilogx(ome,gain)

plt.grid()
plt.show()
