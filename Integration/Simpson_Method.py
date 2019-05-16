import math

def I(t):
    return (60 - t)**2 + (60 - t)*math.sin(math.sqrt(t))

def simpson_even(a,b,n,f):
    if (n % 2 != 0):
        return -1

    h = (b - a)/n
    total = f(a)+f(b)

    for i in range(n):
        x = a + i*h

        if x == a or x == b:
            continue

        if i % 2 == 1:
            total += 4*f(x)

        elif i % 2 == 0:
            total += 2*f(x)

    total = (h/3) * total
    return total

def simpson_triple(a, b, n, f):
    if (n %3 != 0):
        return -1

    h = (b - a) / n
    total = f(a) + f(b)

    for i in range(n):
        x = a + i * h

        if x == a or x == b:
            continue

        if i % 3 == 0:
            total += 2 * f(x)

        else:
            total += 3 * f(x)

    total = (3*h/8) * total
    return total

area1 = simpson_even(0,40,4,I)
area2 = simpson_triple(40,70,3,I)

print("Area: ", area)


