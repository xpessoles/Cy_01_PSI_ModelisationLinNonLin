import matplotlib.pyplot as plt
import numpy as np
from math import sqrt
K =23.26
r = 12/4000
tau = 0.51

x=np.linspace(0,10,1000)
p1=plt.plot(x,
            (
                K*r*(-tau+x+tau*np.exp(-x/tau))
                ),label="$\omega_0 = 10$, $z=1,1$")




plt.grid(True, which="both", linestyle="dotted")
#plt.title("Fonctions trigonometriques")  
#plt.legend([p1, p2], ["Sinus", "Cosinus"])
#plt.legend(loc='lower right', fancybox=True, shadow=True, prop=dict(size=10))
plt.xlabel("Temps en $s$")
plt.ylabel("$ theta(t)$ en $rad$")
#plt.title("Evolution de $\theta$ en fonction du temps pour une entrée échelon de 1V")
plt.show()
fig = plt.figure()
fig.savefig('temp.pdf', transparent=True)

