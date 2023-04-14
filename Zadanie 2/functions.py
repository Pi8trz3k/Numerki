import numpy as np


# checking if matrix is diagonally dominant
def is_diagonally_dominant(array_input):
    tab_len = len(array_input) - 1
    for i in range(tab_len):
        row_sum = np.sum(abs(array_input[i]))
        # print(row_sum)
        diagonal_number = abs(array_input[i][i])
        row_sum_without_diagonal_number = row_sum - diagonal_number
        if diagonal_number <= row_sum_without_diagonal_number:
            print("Macierz nie jest dominujaca przekatniowo")
            return False
    return True


# returning array that don't contain result numbers(last numbers in every row is rejected)
def get_coefficients(array_input):
    array_len = len(array_input)
    coefficients_array = np.zeros((array_len, array_len))

    for i in range(array_len):
        for j in range(array_len):
            coefficients_array[i][j] = array_input[i][j]
    return coefficients_array


# getting result of equations to array
def get_constants(array_input):
    array_len = len(array_input)
    constat_array = np.zeros(array_len)

    for i in range(array_len):
        constat_array[i] = array_input[i][array_len]
    return constat_array


def make_diagonally_dominant(coefficients_array, results):
    array_len = len(coefficients_array)
    print("Przekształcam macierz oraz tablice wyrazów wolnych")
    for i in range(array_len):
        row_sum = np.sum(np.abs(coefficients_array[i]) - np.abs(coefficients_array[i][i]))
        if np.abs(coefficients_array[i, i]) <= row_sum:
            max_index = np.argmax(np.abs(coefficients_array[i, :]))
            coefficients_array[[i, max_index], :] = coefficients_array[[max_index, i], :]
            # chaning rows of results also
            cp = results[i]
            results[i] = results[max_index]
            results[max_index] = cp
    return coefficients_array, results


def get_diagonal_reversed(array_input):
    array_len = len(array_input)
    return_array = np.zeros((array_len, array_len))

    for i in range(array_len):
        return_array[i][i] = 1 / array_input[i][i]

    return return_array


def get_under_diagonal(array_input):
    array_len = len(array_input)
    return_array = np.zeros((array_len, array_len))

    for i in range(array_len):
        for j in range(array_len):
            if j < i:
                return_array[i][j] = array_input[i][j]
    return return_array


def get_over_diagonal(array_input):
    array_len = len(array_input)
    return_array = np.zeros((array_len, array_len))

    for i in range(array_len):
        for j in range(array_len):
            if j > i:
                return_array[i][j] = array_input[i][j]
    return return_array


def gauss_seidl(choice, number):
    array = np.loadtxt("./coefficients.txt", dtype="float", delimiter=",", encoding="utf-8")
    coefficients = get_coefficients(array)
    constants = get_constants(array)

    if not (is_diagonally_dominant(coefficients)):
        coefficients, constants = make_diagonally_dominant(coefficients, constants)
        if not (is_diagonally_dominant(coefficients)):
            print(coefficients)
            print("Macierz nie jest dominująca przekątniowo, program zostaje zakonczony")
            quit()

    array_len = len(coefficients)

    x = np.zeros(array_len)

    diagonal_reversed = get_diagonal_reversed(coefficients)
    under_diagonal = get_under_diagonal(coefficients)
    over_diagonal = get_over_diagonal(coefficients)

    db = np.dot(diagonal_reversed, constants)
    dl = np.dot(diagonal_reversed, under_diagonal)
    du = np.dot(diagonal_reversed, over_diagonal)

    x_new = np.zeros(array_len)

    match choice:
        # iterations
        case 1:
            for i in range(number):

                for k in range(len(db)):
                    dl_numbers = 0
                    du_numbers = 0
                    for col in range(array_len):
                        dl_numbers = dl_numbers + (-1 * dl[k][col] * x[col])
                        du_numbers = du_numbers + (-1 * du[k][col] * x_new[col])
                    x_new[k] = (db[k] + dl_numbers + du_numbers)
                    x = x_new.copy()
        # epsilon
        case 2:
            diff = number + 1
            while diff > number:
                for k in range(array_len):
                    dl_numbers = 0
                    du_numbers = 0
                    for col in range(array_len):
                        dl_numbers = dl_numbers + (-1 * dl[k][col] * x[col])
                        du_numbers = du_numbers + (-1 * du[k][col] * x_new[col])
                    x_new[k] = (db[k] + dl_numbers + du_numbers)
                for i in range(array_len):
                    foo = abs(x_new[i] - x[i])
                    if foo < diff:
                        diff = foo
                x = x_new.copy()

    return x
