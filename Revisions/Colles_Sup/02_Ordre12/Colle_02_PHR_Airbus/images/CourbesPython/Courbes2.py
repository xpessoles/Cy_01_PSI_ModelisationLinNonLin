import matplotlib.pyplot as plt
import numpy as np
from math import sqrt
K =23.26
r = 12/4000
tau = 0.51
Kampli = 10
print(-(1/(4*tau**2))+(K*r*Kampli)/(tau))
A = sqrt(-(1/(4*tau**2))+(K*r*Kampli)/(tau))


x=np.linspace(0,10,1000)
p1 = plt.plot(x,
            (
                1
                -np.exp(-x/(2*tau))*np.cos(A*x)
                -(1)/(2*tau*A)*np.exp(-x/(2*tau))*np.sin(A*x)
                ),label="Angle de sortie $\\theta(t)$",lw=2)
p2 = plt.plot(x,
            (
                1+0.*x
                ),label="Angle d'entrée $\\theta_e(t)$",lw=2)



plt.grid(True, which="both", linestyle="dotted")
#plt.title("Fonctions trigonometriques")  
#plt.legend([p1, p2], ["Sinus", "Cosinus"])
plt.legend(loc='lower right', fancybox=True, shadow=True, prop=dict(size=10))
plt.xlabel("Temps en $s$")
plt.ylabel("Angle en $rad$")
#plt.title("Evolution de $\theta$ en fonction du temps pour une entrée échelon de 1V")
plt.show()
fig = plt.figure()
#fig.savefig('temp.pdf', transparent=True)

