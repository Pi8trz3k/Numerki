import functions as f
import matplotlib.pyplot as plt
import numpy as np

def choose():
    global foo
    print("Wybierz funkcję:")
    print("[1] Wielomian -3 + 3x + 4x^3")
    print("[2] cos(x)")
    print("[3] 2^x")
    print("[4] Złożenie funkcji 1 i 2")
    print("[5] Złożenie funkcji 1 i 3")
    print("[0] Wyjdź")
    func = int(input())

    while func > 6 or func < 0:
        print("Wybrałeś złą funkcję, spróbuj jeszcze raz")
        func = int(input())

    if func == 0:
        quit()

    print("Wybierz warunek stopu:")
    print("[1] Dokładność")
    print("[2] Liczba iteracji")
    stop = int(input())

    while stop < 1 or stop > 2:
        print("Wybrałeś zły warunek stopu, spróbuj jeszcze raz")
        stop = int(input())

    if stop == 1:
        print("Podaj dokladnosc z ktora chcesz obliczyc rozwiazanie")
        foo = float(input())
    elif stop == 2:
        print("Podaj liczbe iteracji")
        foo = int(input())

    return func, stop, foo


def get_interval():
    print("Wpisz przedział:")

    print("a:")
    a = float(input())

    print("b:")
    b = float(input())

    return a, b


def get_guess():
    print("Wpisz liczbe do metody Newtona(stycznych):")
    guess = float(input())
    return guess


def draw(func_number, a, b):
    poly = f.choice(mathematical_function, stop_condition_number, stop_condition, a, b, c)
    match func_number:
        case 1:
            print(poly[0], f.polynominal(poly[0]), poly[1], f.polynominal(poly[0]))
            get_drawing(poly, f.polynominal, a, b)
            return
        case 2:
            print(poly[0], f.cos(poly[0]), poly[1], f.cos(poly[0]))
            f1 = np.vectorize(f.cos)
            get_drawing(poly, f1, a, b)
            return
        case 3:
            print(poly[0], f.exponential(poly[0]), poly[1], f.exponential(poly[0]))
            f1 = np.vectorize(f.exponential)
            get_drawing(poly, f1, a, b)
            return
        case 4:
            print(poly[0], f.polynominal_cos(poly[0]), poly[1], f.polynominal_cos(poly[0]))
            f1 = np.vectorize(f.polynominal_cos)
            get_drawing(poly, f1, a, b)
            return
        case 5:
            print(poly[0], f.polynominal_exponential(poly[0]), poly[1], f.polynominal_exponential(poly[0]))
            f1 = np.vectorize(f.polynominal_exponential)
            get_drawing(poly, f1, a, b)
            return
        case _:
            return "Cos sie popsulo"


def get_drawing(numbers, func, a, b):
    x = np.linspace(a, b)
    y = func(x)
    plt.plot(x, y)
    plt.scatter(numbers[0], func(numbers[0]), edgecolors="red")
    plt.scatter(numbers[1], func(numbers[1]), edgecolors="green")
    plt.grid()
    plt.show()
    return


mathematical_function, stop_condition_number, stop_condition = choose()

a, b = get_interval()
c = get_guess()

draw(mathematical_function, a, b)
