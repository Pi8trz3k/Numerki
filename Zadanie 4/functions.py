import horner as h
import math


def choose(x, choice):
    match choice:
        case 1:
            return 8 * x + 3
        case 2:
            return math.sin(x) - 2 * math.cos(x - 5)
        case 3:
            coef = [12, 4, -1]
            return h.horner(coef, len(coef), x)
        case 4:
            return math.fabs(x - 5)
        case 5:
            return math.cos(x) / x
        case _:
            print("Nieprawidłowa wartosc")
