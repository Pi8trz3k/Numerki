import horner
import math


def polynominal(number):
    # -3 + 3x + 4x^3
    coefficents = [-3, 3, 0, 4]
    return horner.horner(coefficents, len(coefficents), number)


def linear(number):
    # 3x - 5
    return 3 * number - 5


def cos(number):
    # cos(x - 0.1) + 2
    return math.cos(number - 0.1) + 2


def modulus(number):
    # |x - 1|
    return abs(number - 1)


def modulus_cos(number):
    # |cos(x - 0.1) + 2 - 1|
    return modulus(cos(number))


def linear_modulus(number):
    # 3 * |x - 1| - 5
    return linear(modulus(number))


def polynominal_linear(number):
    # -3 + 3 * ( 3x - 5 ) + 4( 3x - 5)^3
    return polynominal(linear(number))


def functions(func_number, factor):
    match func_number:
        case 1:
            return polynominal(factor)
        case 2:
            return linear(factor)
        case 3:
            return cos(factor)
        case 4:
            return modulus(factor)
        case 5:
            return modulus_cos(factor)
        case 6:
            return linear_modulus(factor)
        case 7:
            return polynominal_linear(factor)
        case _:
            print("Cos jest nie tak")
