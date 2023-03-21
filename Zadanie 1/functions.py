import horner
import math


def polynominal(number):
    # -3 + 3x + 4x^3
    coefficents = [-3, 3, 0, 4]
    return horner.horner(coefficents, len(coefficents), number)


def first_deriv_polynominal(number):
    return 3 + 12 * (number ** 2)


def second_deriv_polynominal(number):
    return 24 * number


def cos(number):
    return math.cos(number)


def first_deriv_cos(number):
    return -1 * math.sin(number)


def second_deriv_cos(number):
    return -1 * math.cos(number)


def exponential(number):
    return 2 ** number


def first_deriv_exponential(number):
    return (2 ** number) * math.log(2, math.e)


def second_deriv_exponential(number):
    return (2 ** number) * (math.log(2, math.e)) ** 2


def polynominal_cos(number):
    return polynominal(cos(number))


def first_deriv_polynominal_cos(number):
    return -6 * math.sin(number) - 3 * math.sin(3 * number)


def second_deriv_polynominal_cos(number):
    return -6 * math.cos(number) - 9 * math.cos(3 * number)


def polynominal_exponential(number):
    return polynominal(exponential(number))


def first_deriv_polynominal_exponential(number):
    return 3 * (2 ** number + 2 ** (3 * number + 2)) * math.log(2, math.e)


def second_deriv_polynominal_exponential(number):
    return 3 * (math.log(2, math.e)) ** 2 * (3 * 2 ** (3 * number + 2) + 2 ** number)


def choice(func_number, stop_condition_number, stop_condition, a, b):
    match func_number:
        case 1:
            bisection = bisection_method(polynominal, stop_condition_number, stop_condition, a, b)
            newton = newton_method(polynominal, first_deriv_polynominal, second_deriv_polynominal, stop_condition_number
                                   , stop_condition, a, b)
            return bisection, newton
        case 2:
            bisection = bisection_method(cos, stop_condition_number, stop_condition, a, b)
            newton = newton_method(cos, first_deriv_cos, second_deriv_cos, stop_condition_number, stop_condition, a, b)
            return bisection, newton
        case 3:
            bisection = bisection_method(exponential, stop_condition_number, stop_condition, a, b)
            newton = newton_method(exponential, first_deriv_exponential, second_deriv_exponential, stop_condition_number
                                   , stop_condition, a, b)
            return bisection, newton
        case 4:
            bisection = bisection_method(polynominal_cos, stop_condition_number, stop_condition, a, b)
            newton = newton_method(polynominal_cos, first_deriv_polynominal_cos, second_deriv_polynominal_cos,
                                   stop_condition_number, stop_condition, a, b)
            return bisection, newton
        case 5:
            bisection = bisection_method(polynominal_exponential, stop_condition_number, stop_condition, a, b)
            newton = newton_method(polynominal_exponential, first_deriv_polynominal_exponential,
                                   second_deriv_polynominal_exponential, stop_condition_number, stop_condition, a, b)
            return bisection, newton
        case _:
            return "Cos sie popsulo"


def bisection_method(function, stop_condition_number, stop_condition, a, b):
    print("Metoda bisekcji: ")

    # dokładność
    if stop_condition_number == 1:
        x = (a + b) / 2
        i = 0
        print("X:", x, "| function: ", function(x))
        while abs(function(x)) >= stop_condition:
            i = i + 1
            if function(x) == 0:
                return x
            # print("X:", x, "| function: ", function(x))
            if function(a) * function(b) > 0:
                print("Zły przedział")
                quit()
            elif function(x) * function(a) < 0:
                b = x
            elif function(x) * function(b) < 0:
                a = x
            x = (a + b) / 2
            print("X:", x, "| function: ", function(x))
        print("Liczba iteracji metodą bisekcji: ", i)
        print("ABS: ", abs(b - a), "a, b: ", a, b)
    # liczba iteracji
    elif stop_condition_number == 2:
        for i in range(0, stop_condition):
            x = (a + b) / 2.0
            if function(x) == 0:
                return x
            if function(a) * function(b) > 0:
                print("Zły przedział")
                quit()
            elif function(x) * function(a) < 0:
                b = x
            elif function(x) * function(b) < 0:
                a = x
            print("X:", x, "| function: ", function(x))

        print("ABS: ", abs(b - a), ";a, b: ", a, b)

    return x


def newton_method(function, first_funcderiv, second_funcderiv, stop_condition_number, stop_condition_type, a, b):
    results = []
    print("Metoda Newtona:")
    if function(a) * function(b) > 0:
        print("Zły przedział")
        quit()

    if function(a) * second_funcderiv(a) >= 0:
        x = a
    elif function(b) * second_funcderiv(b) >= 0:
        x = b
    else:
        print("a: ", function(a) * second_funcderiv(a))
        print("b: ", function(b) * second_funcderiv(b))
        x = 1

    # dokładność
    if stop_condition_number == 1:
        i = 0
        while abs(function(x)) >= stop_condition_type:
            i = i + 1
            xi = x - (function(x) / first_funcderiv(x))
            x = xi
            print("newton x: ", x)
        print("Liczba iteracji metodą Newtona:", i)
    # liczba iteracji
    elif stop_condition_number == 2:
        for i in range(0, stop_condition_type):
            xi = x - (function(x) / first_funcderiv(x))
            x = xi
            print("newton x: ", xi)

    return x
