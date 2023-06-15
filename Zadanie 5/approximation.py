# some materials
# https://www.youtube.com/watch?v=e59Zu1TXHzY
# https://en.wikipedia.org/wiki/Legendre_polynomials?useskin=vector
from functions import choose


def gauss_legendre(a, b, func_choice, nodes, k):
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
        integral += wi * choose(xi_mapped, func_choice) * legendre(k, xi)

    integral *= (b - a) / 2
    return integral


def legendre(n, x):
    if n == 0:
        return 1
    elif n == 1:
        return x
    else:
        p = [1, x]
        for k in range(2, n + 1):
            p.append(((2 * k - 1) * x * p[k - 1] - (k - 1) * p[k - 2]) / k)
        return p[n]


def get_polynominal_coefficients(a, b, func_number, nodes_number, k):
    tab = []
    for i in range(k + 1):
        tab.append(get_aproximation_coefficients(a, b, func_number, nodes_number, i))
    return tab


def get_aproximation_coefficients(a, b, func_number, nodes_number, k):
    return (2 * k + 1) / 2 * gauss_legendre(a, b, func_number, nodes_number, k)


def get_polynominal_values(k, x, tab):
    poly = 0
    for i in range(k + 1):
        poly += tab[i] * legendre(i, x)
    return poly


def error(func_number, k, tab, nodes):
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
        x, w = coefficients[nodes][i]
        integral += w * (choose(x, func_number) - get_polynominal_values(k, x, tab)) ** 2
    return integral
