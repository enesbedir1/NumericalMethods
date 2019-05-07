import numpy as np
import math

"""
my equations:
4 * x1 +x2 - x3 +x4 = -2
x1 + 4 * x2 - x3 - x4 = -1
-1 * x1 - x2 + 5 * x3 + x4 = 0
x1 - x2 + x3 + 3*x4 = 1
"""

m = np.array([[4, 1, -1, 1, -2],
              [1, 4, -1, -1, -1],
              [-1, -1, 5, 1, 0],
              [1, -1, 1, 3, 1]])

Es = 0.001
i = 0
x = [0,0,0,0]

def Gauss_Seidel_Method(m,  Error_tolerance, inital_value_vector):
    x = inital_value_vector
    magnitude_prev = 0
    while True:
        for i in range(len(m)):
            a = 0
            for j in range(len(m[1, :])):
                if j == len(m[1, :]) - 1:
                    b = m[i, j]
                elif i == j:
                    coefficient = m[i, j]
                    continue
                elif i != j:
                    a += -1 * x[j] * m[i, j]
            x[i] += b
            x[i] = (a + b) / coefficient
            a = 0

        magnitude = np.linalg.norm(x)
        E = math.fabs((magnitude - magnitude_prev) / magnitude)

        if E < Error_tolerance:
            print("Error: ", E)
            print("vector: ", x)
            print("magnitude: ", magnitude)
            break

        magnitude_prev = magnitude


if __name__ == "__main__":
    Gauss_Seidel_Method(m, Es, x)
