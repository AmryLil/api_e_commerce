import numpy as np
from scipy.optimize import least_squares

# Data
x_data = np.array([3, 7, 10, 12, 15, 17])
y_data = np.array([31, 151, 304, 436, 679, 871])

# (A) Interpolasi Linier
def linear_interpolation(x, x1, y1, x2, y2):
    return y1 + (x - x1) * (y2 - y1) / (x2 - x1)

x_a = 5
y_a = linear_interpolation(x_a, x_data[0], y_data[0], x_data[1], y_data[1])
print(f"(A) Hasil interpolasi linier pada x = {x_a}: y = {y_a}")

# (B) Interpolasi Lagrange
def lagrange_interpolation(x, x_data, y_data):
    result = 0
    for i in range(len(x_data)):
        term = y_data[i]
        for j in range(len(x_data)):
            if i != j:
                term *= (x - x_data[j]) / (x_data[i] - x_data[j])
        result += term
    return result

x_b = 11
y_b = lagrange_interpolation(x_b, x_data, y_data)
print(f"(B) Hasil interpolasi Lagrange pada x = {x_b}: y = {y_b}")

# (C) Pendekatan Orde-2 dari Least-Square
def quadratic_polynomial(params, x):
    a, b, c = params
    return a * x**2 + b * x + c

def error_function(params, x, y):
    return quadratic_polynomial(params, x) - y

initial_params = [1.0, 1.0, 1.0]  # Nilai awal untuk a, b, dan c

result = least_squares(error_function, initial_params, args=(x_data, y_data))

fit_params = result.x

x_c = 13
y_c = quadratic_polynomial(fit_params, x_c)
print(f"(C) Hasil pendekatan orde-2 dari Least-Square pada x = {x_c}: y = {y_c}")
