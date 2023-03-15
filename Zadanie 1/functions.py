import horner
import math


def polynominal(x):
    coefficents = [2, 5, 2]
    # coefficents = [-3,-3,1,1]
    return horner.horner(coefficents, len(coefficents), x)


def cos(number):
    return math.cos(number)


def exponential(number):
    return 2 ** number


def polynominal_cos(number):
    return polynominal(cos(number))


def polynmoinal_exponential(number):
    return polynominal(exponential(number))


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
            bisection = bisection_method(polynmoinal_exponential, stop_condition_number, stop_condition, a, b)
            return bisection
        case _:
            return "Cos sie popsulo"


def bisection_method(function, stop_condition_number, stop_condition, a, b):
    results = []
    print("Metoda bisekcji: ")
    # dokładność
    if(stop_condition_number == 1):
        while not(abs(b - a) < stop_condition):
            x = (a + b) / 2
            if function(x) == 0:
                results.append(x)
            print("X:", x, "| function: ", function(x))
            if function(x) * function(a) < 0:
                b = x
            else:
                a = x
    #liczba iteracji
    elif (stop_condition_number == 2):
        for iter in range(1, stop_condition):
            x = (a + b) / 2
            if function(x) == 0:
                results.append(x)
            print("X:", x, "| function: ", function(x))
            if function(x) * function(a) < 0:
                b = x
            else:
                a = x
    return results


def newton_method():
    return 0
