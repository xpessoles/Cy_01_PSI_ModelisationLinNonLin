import math as m
R  = 10
L  = 2.2e-3
kc = 2.1
ke = 2.1
Cr = 0.2
fv = 0.04
Jeq = 7e-3


Km = kc/(ke*kc+R*fv)
a2 = Jeq*L/(ke*kc+R*fv)
a1 = (R*Jeq+L*fv)/(ke*kc+R*fv)

a = 3.1e-6
b = 14.5e-3
c = 1
delta = b*b - 4 * a *c

p1 = (-b-m.sqrt(delta))/(2*a)
p2 = (-b+m.sqrt(delta))/(2*a)

T = (R*Jeq)/(ke*kc+R*fv)
