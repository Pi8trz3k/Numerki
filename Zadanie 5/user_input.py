def get_functions():
    print("Wybierz aproksymowana funkcje: ")
    print("1. 8 * x + 3" )
    print("2. sin(15 * x)")
    print("3. 12 + 4 * x - x^2")
    print("4. |x - 5|")
    print("5. 8 * sin(15 * x) + 3")
    print("6. |8 * x - 2|")

    function = int(input("Podaj numer funkcji: "))

    while function < 1 or function > 6:
        print("Podaj funkcje jeszcze raz")
        function = int(input())

    return function


def get_interval():
    print("Podaj przedział aproksymacji")
    a = float(input("a: "))
    b = float(input("b: "))
    return a, b


def get_nodes():
    print("Podaj liczbę węzłów kwadratury Gaussa: ")
    nodes_number = int(input())

    while nodes_number < 2 or nodes_number > 5:
        print("Podaj jeszcze raz: ")
        nodes_number = int(input())

    return nodes_number


def get_polynominal_degree():
    return int(input("Podaj stopień wielomianu aproksymującego: "))


