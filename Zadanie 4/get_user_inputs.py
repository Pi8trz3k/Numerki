def get_data_from_user():
    print("Wybierz funkcję")
    print("1. 8x + 3")
    print("2. sin(x) - 2")
    print("3. 1 + 1x -2x^2")
    print("4. |x - 5|")
    print("5. x / (1 + x")

    chosen_func = int(input("Podaj numer funkcji: "))
    while chosen_func < 1 or chosen_func > 5:
        chosen_func = int(input("Podaj ponownie numer funkcji: "))

    print("Podaj przedziały funkcji")
    a = float(input("a: "))
    b = float(input("b: "))

    eps = float(input("Podaj dokladnosc w metodzie: "))

    return a, b, eps, chosen_func
