import math

# Question 4
Ti = 2.54 
om = 1


Krinv= Ti *90e-3*(math.sqrt(1+Ti**2))/(math.sqrt(1+0.05**2))*(1)/(math.sqrt((1-0.01**2)**2+0.1**2))

Kr = 1/Krinv
print(Kr)

lKr = 1- math.log10(math.sqrt(Ti*Ti+1))+math.log(Ti)
print(10**lKr)