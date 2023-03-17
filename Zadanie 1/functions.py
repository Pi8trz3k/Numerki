import horner
import math


def polynominal(number):
    # coefficents = [2, 5, 2]
    # coefficents = [-100,10,0,1]
    # -3 + 3x + 4x^3
    coefficents = [-3, 3, 0, 4]
    # coefficents = [-1, -1, 1]
    return horner.horner(coefficents, len(coefficents), number)


def deriv_polynominal(number):
    return 3 + 12 * (number ** 2)


def cos(number):
    return math.cos(number)


def deriv_cos(number):
    return -1 * math.sin(number)


def exponential(number):
    return 2 ** number


def deriv_exponential(number):
    return (2 ** number) * math.log(2, math.e)


def polynominal_cos(number):
    return polynominal(cos(number))


def deriv_polynominal_cos(number):
    return -6 * math.sin(number)


def polynominal_exponential(number):
    return polynominal(exponential(number))


def deriv_polynominal_exponential(number):
    return 3 * (2 ** number + 2 ** (3 * number + 2)) * math.log(2, math.e)


def choice(func_number, stop_condition_number, stop_condition, a, b):
    match func_number:
        # # variant B -> |f(xi)| < e
        # case 1:
        #     return 0
        # # user defined iterations
        # case 2:
        #     return 0
        case 1:
            bisection = bisection_method(polynominal, stop_condition_number, stop_condition, a, b)
            # newton = newton_method(polynominal, deriv_polynominal, stop_condition_number, stop_condition, )
            return bisection
        case 2:
            bisection = bisection_method(cos, stop_condition_number, stop_condition, a, b)
            return bisection
        case 3:
            bisection = bisection_method(exponential, stop_condition_number, stop_condition, a, b)
            return bisection
        case 4:
            bisection = bisection_method(polynominal_cos, stop_condition_number, stop_condition, a, b)
            return bisection
        case 5:
            bisection = bisection_method(polynominal_exponential, stop_condition_number, stop_condition, a, b)
            return bisection
        case _:
            return "Cos sie popsulo"


def bisection_method(function, stop_condition_number, stop_condition, a, b):
    results = []
    print("Metoda bisekcji: ")
    # dokładność
    if stop_condition_number == 1:
        x = (a + b) / 2
        while abs(function(x)) >= stop_condition:
            if function(x) == 0:
                return x
            print("X:", x, "| function: ", function(x))
            if function(a) * function(b) > 0:
                print("Zły przedział")
                quit()
            elif function(x) * function(a) < 0:
                b = x
            elif function(x) * function(b) < 0:
                a = x
            x = (a + b) / 2
        print("ABS: ", abs(b-a), "a, b: ", a, b)
    # liczba iteracji
    elif stop_condition_number == 2:
        for _ in range(1, stop_condition):
            x = (a + b) / 2.0
            if function(x) == 0:
                return x
            print("X:", x, "| function: ", function(x))
            if function(a) * function(b) > 0:
                print("Zły przedział")
                quit()
            elif function(x) * function(a) < 0:
                b = x
            elif function(x) * function(b) < 0:
                a = x
        print("ABS: ", abs(b - a), "a, b: ", a, b)
    return results


def newton_method(function, funcderiv, stop_condition_number, stop_condition_type, x):
    results = []

    # dokładność
    if (stop_condition_number == 1):
        return 0
    # liczba iteracji
    elif (stop_condition_number == 2):
        for iter in range(1, stop_condition_type):
            i = x - (function(x)/funcderiv(x))

    return results
