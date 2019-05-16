import numpy as np
import matplotlib.pyplot as plt
import math

# Sample Points
x_vector = [5 ,10, 15, 20 ,25, 30, 35 ,40, 45 ,50]
y_vector = [17 ,24 ,31 ,33 ,37 ,37 ,40 ,40 ,42 ,41]
n = 10 # Number of points

def total(liste,exp):
    total = 0
    for i in liste:
        total += i**exp
    return total

def total_2(liste1,exp1,liste2,exp2):
    total = 0
    for i in range(len(liste1)):
        total += (liste1[i]**exp1)*(liste2[i]**exp2)
    return total

x_total = total(x_vector, 1)
x2_total = total(x_vector, 2)
x3_total = total(x_vector, 3)
x4_total = total(x_vector, 4)
y1_total = total(y_vector, 1)
y2_total = total(y_vector, 2)
xy_total = total_2(x_vector, 1, y_vector, 1)
x2y_total = total_2(x_vector, 2, y_vector, 1)

a = np.array([[n,x_total,x2_total],
              [x_total,x2_total,x3_total],
              [x2_total,x3_total,x4_total]])
b = np.array([y1_total,xy_total,x2y_total])

[a0,a1,a2] = np.linalg.solve(a, b)

def f(a0,a1,a2,x):
    return a2*(x**2)+a1*x+a0

for x in x_vector:
    print("f({}):".format(x), round(f(a0,a1,a2,x),4))

r = (n*xy_total-x_total*y1_total)/(math.sqrt(n*x2_total-x_total**2)*math.sqrt(n*y2_total-y1_total**2))
print("r : ", r)

a = []
b = []

print("a0: ",a0)
print("a1: ",a1)
print("a2: ",a2)

for x in range(5,50,1):
    y=a2*x**2+a1*x+a0
    a.append(x)
    b.append(y)

fig= plt.figure()
axes=fig.add_subplot(111)
axes.plot(a,b)
plt.show()
