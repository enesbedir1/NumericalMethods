import math

def f(x):  # write here your given function
    pass

def MullerMethod(x0, x1, x2, f, Expected_Error=None, iteration_number=0):  # f is your function
    if Expected_Error is not None:
        Error_Bool = True
    else: Error_Bool = False
    i = 0

    while True:
        h0 = x1 - x0
        h1 = x2 - x1

        s0 = (f(x1) - f(x0)) / h0
        s1 = (f(x2) - f(x1)) / h1

        a = (s1 - s0) / (h1 + h0)
        b = a * h1 + s1
        c = f(x2)
        delta = b ** 2 - 4 * a * c

        x3 = x2 + -2 * c / max(math.fabs(b + math.sqrt(delta)), math.fabs(b - math.sqrt(delta)))
        E = (math.fabs(x3 - x2) / x3) * 100

        if E < Expected_Error and Error_Bool:
            print("root :", x3)
            print("Expected Error: ", E)
            break

        x0 = x1
        x1 = x2
        x2 = x3

        i += 1
        if i == 0:
            print("Iteration is completed!")
            print("root = ", x3)


if __name__ == "__main__":
    MullerMethod(x0, x1, x2, f, E)
