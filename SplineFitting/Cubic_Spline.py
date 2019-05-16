from matplotlib.pyplot import plot, show
import numpy as np
from scipy.interpolate import CubicSpline

# (x,y) = (0,12) (1,14) (2,22) (3,39) (4,58) (5,77)
x = np.array([1, 2,3 ,5, 7])
y = np.array([3,6 ,19,99,291])

# calculate natural cubic spline polynomials
cs = CubicSpline(x,y,bc_type='natural')

print(cs.c)

# Polynomial coefficients for 0 <= x <= 1
a0 = cs.c.item(3,0)
b0 = cs.c.item(2,0)
c0 = cs.c.item(1,0)
d0 = cs.c.item(0,0)

# Polynomial coefficients for 1 < x <= 2
a1 = cs.c.item(3,1)
b1 = cs.c.item(2,1)
c1 = cs.c.item(1,1)
d1 = cs.c.item(0,1)

# Polynomial coefficients for 0 <= x <= 1
a2 = cs.c.item(3,2)
b2 = cs.c.item(2,2)
c2 = cs.c.item(1,2)
d2 = cs.c.item(0,2)

# Polynomial coefficients for 1 < x <= 2
a3 = cs.c.item(3,3)
b3 = cs.c.item(2,3)
c3 = cs.c.item(1,3)
d3 = cs.c.item(0,3)

# Print polynomial equations for different x regions
print('S0(1<=x<=2) = ', a0, ' + ', b0, '(x-1) + ', c0, '(x-1)^2  + ', d0, '(x-1)^3')
print('S1(2< x<=3) = ', a1, ' + ', b1, '(x-2) + ', c1, '(x-2)^2  + ', d1, '(x-2)^3')
print('S2(3<=x<=5) = ', a2, ' + ', b2, '(x-3) + ', c2, '(x-3)^2  + ', d2, '(x-3)^3')
print('S3(5< x<=7) = ', a3, ' + ', b3, '(x-5) + ', c3, '(x-5)^2  + ', d3, '(x-5)^3')
# print('S5(4< x <=5) = ', a4, ' + ', b4, '(x-4) + ', c4, '(x-4)^2  + ', d4, '(x-4)^3')


def f(x):
    global a0,b0,c0,d0,a1,b1,c1,d1,a2,b2,c2,d2,a3,b3,c3,d3
    if (1 <= x <= 2):
        return a0 + b0 * (x-1) + c0 * (x-1) ** 2 + d0 * (x-1) ** 3
    elif (2 < x <= 3) :
        return a1 + b1 * (x-2) + c1 * (x-2) ** 2 + d1 * (x-2) ** 3    
    elif (3 <= x <= 5):
        return a2 + b2 * (x-3) + c2 * (x-3) ** 2 + d2 * (x-3) ** 3
    elif (5 < x <= 7):
        return a3 + b3 * (x-5) + c3 * (x-5) ** 2 + d3 * (x-5) ** 3


x0 = np.arange(1, 7, 0.01)
y0 = []

print("f(2.2):", round(f(2.2),5))
print("f(3.4):", round(f(3.4),5))

for i in range(len(x0)):
    y0.append(f(x0[i]))

plot(x0, y0)
show()

