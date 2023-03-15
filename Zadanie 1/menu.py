import functions
import matplotlib


def get_interval():
    print("Wpisz przedział:")

    print("a:")
    a = float(input())

    print("b:")
    b = float(input())

    return a, b


def choose():
    global foo
    print("Wybierz funkcję:")
    print("[1] Wielomian 2 + 5x + 2x^2")
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


mathematical_function, stop_condition_number, stop_condition = choose()

a, b = get_interval()

# print("a:", a, ", b: ", b)
poly = functions.choice(mathematical_function, stop_condition_number, stop_condition, a, b)
print(poly)
