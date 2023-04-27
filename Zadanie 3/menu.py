import math_functions as f
import newtonInterpolation


def show():
    print("1. Wielomian        -3 + 3x + 4x^3")
    print("2. Liniowa          3x - 5")
    print("3. Trygonometryczna cos(x - 0.1) + 2")
    print("4. Moduł            |x - 1|")
    print("5. Złożenie f4(f3)  |cos(x - 0.1) + 2 - 1|")
    print("6. Złożenie f2(f4)  3(|x - 1|)- 5")
    print("7. Złożenie f1(f2)  -3 + 3 * ( 3x - 5 ) + 4( 3x - 5)^3")


def functions(factor):
    choice = 0
    show()
    while choice > 7 or choice < 1:
        print("Podaj swoj wybor: ")
        choice = int(input())

    match choice:
        case 1:
            return f.polynominal(factor)
        case 2:
            return f.linear(factor)
        case 3:
            return f.cos(factor)
        case 4:
            return f.modulus(factor)
        case 5:
            return f.modulus_cos(factor)
        case 6:
            return f.linear_modulus(factor)
        case 7:
            return f.polynominal_linear(factor)
        case _:
            print("Cos jest nie tak")


def get_nodes():
    return int(input("Podaj liczbę punktów: "))


nodes = get_nodes()
functions(nodes)