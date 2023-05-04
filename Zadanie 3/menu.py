import math_functions as f
import newtonInterpolation as nI
import draw


def choose_function():
    print("1. Wielomian        -3 + 3x + 4x^3")
    print("2. Liniowa          3x - 5")
    print("3. Trygonometryczna cos(x - 0.1)")
    print("4. Moduł            |x - 1|")
    print("5. Złożenie f4(f3)  |cos(x - 0.1) - 1|")
    print("6. Złożenie f2(f4)  3(|x - 1|)- 5")
    print("7. Złożenie f1(f2)  -3 + 3 * ( 3x - 5 ) + 4( 3x - 5)^3")
    print("Podaj swoj wybor: ")
    choice = int(input())
    while choice > 7 or choice < 1:
        print("Podałeś zły wybór, spróbuj jeszcze raz: ")
        choice = int(input())
    return choice


def get_nodes():
    choice = int(input("Podaj liczbę punktów: "))
    while choice < 1:
        print("Podaj większą liczbę węzłów")
        choice = int(input("Podaj liczbę punktów: "))
    return choice


def get_interval():
    start = float(input("Podaj początek przedziału: "))
    end = float(input("Podaj koniec przedziału: "))
    while end < start:
        print("Podałeś zły przedziały, spróbuj jeszcze raz: ")
        start = float(input("Podaj początek przedziału: "))
        end = float(input("Podaj koniec przedziału: "))

    return start, end


chosen_func = choose_function()
nodes = get_nodes()
a, b = get_interval()
h, fx, y = nI.equidistant_nods(a, b, nodes, chosen_func)

calculated_x, calculated_y, real_x, real_y = [], [], [], []
h /= 50
while a <= b:
    calculated_x.append(a)
    calculated_y.append(nI.newton_interpolation(chosen_func, fx, a))
    real_x.append(a)
    real_y.append(f.functions(chosen_func, a))
    a += h

draw.graph(fx, y, calculated_x, calculated_y, real_x, real_y)