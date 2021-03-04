import math
M = .067
p = 1.038
c = 3.7
K = .0054
Tw = 100
To = 4
Ty = 70
t = ((M**(2/3)*c*p**(1/3))/(K*math.pi**2*((4*math.pi)/3)**(2/3)))*(math.log(.76*((To-Tw)/(Ty-Tw))))
print(t)
To = 20
t = ((M**(2/3)*c*p**(1/3))/(K*math.pi**2*((4*math.pi)/3)**(2/3)))*(math.log(.76*((To-Tw)/(Ty-Tw))))
print(t)
