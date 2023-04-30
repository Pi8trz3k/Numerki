import math_functions as mf


def newton_interpolation(f_number, fx, x):
    multiplier = 1
    wt = mf.functions(f_number, fx[0])
    h = fx[1] - fx[0]

    for i in range(1, len(fx)):
        multiplier *= t(x, fx[0], h) - (i - 1)
        a_i = progressive_difference(i, f_number, fx) / factorial(i)
        wt += a_i * multiplier
    return wt


def equidistant_nods(interval_beginning, interval_end, number_of_nodes, func_number):
    height = (interval_end - interval_beginning) / (number_of_nodes - 1)
    fx, y = [], []
    for i in range(number_of_nodes):
        fx.append(interval_beginning)
        y.append(mf.functions(func_number, interval_beginning))
        interval_beginning += height

    return height, fx, y


def factorial(n):
    result = 1
    while n > 1:
        result = result * n
        n -= 1
    return result


def t(x, x0, h):
    return (x - x0) / h


def progressive_difference(i, func_number, fx):
    i_difference = 0
    for k in range(0, i + 1):
        i_difference += (-1) ** (i - k) * binomial(i, k) * mf.functions(func_number, fx[k])
    return i_difference


def binomial(n, k):
    return factorial(n) / (factorial(k) * factorial(n - k))
