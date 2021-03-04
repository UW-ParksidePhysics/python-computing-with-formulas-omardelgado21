import math
g = 9.81
Cd = .2
m = .43
a = .11
d = 1.2
V1 = 33.3
V2 = 2.78
A = math.pi*a**2

Fd = .5*Cd*d*A*V1**2
print(int(Fd))
Fd = .5*Cd*d*A*V2**2
print(int(Fd))
