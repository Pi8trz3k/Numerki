# choosing between number of iterations and accuracy
def stop_condition_choose():
    print("Wybierz warunek stopu: ")
    print("1. Ilość iteracji")
    print("2. Dokładność")

    stop_choice = int(input())

    while stop_choice < 1 or stop_choice > 2:
        print("Wybrałeś zły warunek stopu, spróbuj jeszcze raz!")
        stop_choice = int(input())

    return stop_choice


# choosing number of iterations or accuracy, need number with chosen stop condition -> stop_condition_choose()
def stop_number_choose(stop_condition_number):
    if stop_condition_number == 1:
        print("Podaj liczbe iteracji:")
        number_choice = int(input())
    elif stop_condition_number == 2:
        print("Podaj dokladnosc:")
        number_choice = float(input())

    return number_choice


stop_condition = stop_condition_choose()
stop_condition_number = stop_number_choose(stop_condition)


