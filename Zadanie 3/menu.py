import math_functions as f


def functions(choice, number):
    while choice > 7 or choice < 1:
        print("Podaj swoj wybor: ")
        choice = int(input())

    match choice:
        case 1:
            return f.polynominal(number)
        case 2:
            return f.linear(number)
        case 3:
            return f.cos(number)
        case 4:
            return f.modulus(number)
        case 5:
            return f.modulus_cos(number)
        case 6:
            return f.linear_modulus(number)
        case 7:
            return f.polynominal_linear(number)
        case _:
            print("Cos jest nie tak")

