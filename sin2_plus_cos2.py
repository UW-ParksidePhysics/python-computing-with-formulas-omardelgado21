#a
import math
x = math.pi/4
val = (math.sin(x)**2) + (math.cos(x)**2)
print(val)

#b
v0 = 3
t = 1
a = 2
s = v0*t + 0.5*a*t**2
print(s)

#c
a = 3;3   
b = 5;3
a2 = a**2
b2 = b**2
eq1_sum = a2 + 2*a*b + b2
eq2_sum = a2 - 2*a*b + b2
eq1_pow = (a + b)**2
eq2_pow = (a - b)**2

print("first equation:" + str(eq1_sum) + str(eq1_pow))
print("second equation:" + str(eq2_sum) + str(eq2_pow))
