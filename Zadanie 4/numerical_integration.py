import math

import numpy as np

from functions import choose


def simpson(a, b, func_choice, eps):
    subinterval = 1
    length_all = b - a
    result = 0
    result_previous = eps + 1

    while abs(result - result_previous) > eps:
        subinterval *= 2
        length_sub = length_all / subinterval
        result_previous = result
        result = 0

        x = np.linspace(a, b, subinterval + 1)

        for i in range(0, math.floor(subinterval/2)):
            result += choose(x[2*i], func_choice)
            result += 4*choose(x[2*i+1], func_choice)
            result += choose(x[2*i+2], func_choice)

        result *= length_sub / 3
    return result

def gaussa_legendre(a, b, func_choice, nodes):
    coefficients = {
        1: [],
        2: [(-0.5773502691896257, 1), (0.5773502691896257, 1)],
        3: [(-0.7745966692414834, 0.5555555555555556), (0, 0.8888888888888888),
            (0.7745966692414834, 0.5555555555555556)],
        4: [(-0.8611363115940526, 0.3478548451374538), (-0.33998104358485626, 0.6521451548625461),
            (0.33998104358485626, 0.6521451548625461), (0.8611363115940526, 0.3478548451374538)],
        5: [(-0.906179845938664, 0.23692688505618908), (-0.5384693101056831, 0.47862867049936647),
            (0, 0.5688888888888889),
            (0.5384693101056831, 0.47862867049936647), (0.906179845938664, 0.23692688505618908)]
    }

    integral = 0
    for i in range(nodes):
        xi, wi = coefficients[nodes][i]
        xi_mapped = ((b - a) * xi + (a + b)) / 2
        integral += wi * choose(xi_mapped, func_choice)

    integral *= (b - a) / 2

    return integral
