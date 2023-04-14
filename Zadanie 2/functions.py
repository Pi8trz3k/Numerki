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


# first
# def gauss_seidel(condition_choose, number_choose):
#     array = np.loadtxt("./coefficients.txt", dtype="float", delimiter=",", encoding="utf-8")
#     coefficients_array = get_coefficients(array)
#     result_array = get_constants(array)
#
#     if not (is_diagonally_dominant(coefficients_array)):
#         coefficients_array, result_array = make_diagonally_dominant(coefficients_array, result_array)
#
#     coefficents_array_len = len(coefficients_array)
#     x = np.zeros(coefficents_array_len)
#     x_new = np.zeros(coefficents_array_len)
#
#     match condition_choose:
#         # iterations
#         case 1:
#             for i in range(number_choose):
#                 for j in range(coefficents_array_len):
#                     # tablica A[wiersz j, kolumny do j]; tablica x_new[do kolumny j]
#                     # U*x^i
#                     ux = np.dot(coefficients_array[j, :j], x_new[:j])
#                     # tablica A[wiersz j, kolumny od(j + 1)]; tablica x[kolumny od (j+1)]
#                     # -L*x^(i+1)
#                     lxi_1 = np.dot(coefficients_array[j, j + 1:], x[j + 1:])
#                     x_new[j] = (result_array[j] - ux - lxi_1) / coefficients_array[j, j]
#                     # print("x_new, iteracja j:", j, x_new)
#                 x = x_new
#             return x
#         case 2:
#             while True:
#                 for j in range(coefficents_array_len):
#                     # tablica A[wiersz j, kolumny do j]; tablica x_new[do kolumny j]
#                     # U*x^i
#                     ux = np.dot(coefficients_array[j, :j], x_new[:j])
#                     # tablica A[wiersz j, kolumny od(j + 1)]; tablica x[kolumny od (j+1)]
#                     # -L*x^(i+1)
#                     lxi_1 = np.dot(coefficients_array[j, j + 1:], x[j + 1:])
#                     x_new[j] = (result_array[j] - ux - lxi_1) / coefficients_array[j, j]
#                     # print("x_new, iteracja j:", j, x_new)
#                     if np.allclose(x, x_new, atol=number_choose):
#                         return x_new
#                 x = x_new


# second
def gauss_seidel(A, b, x0, epsilon, max_iterations):
    n = len(A)
    x = x0.copy()

    for i in range(max_iterations):
        x_new = np.zeros(n)
        for j in range(n):
            s1 = np.dot(A[j, :j], x_new[:j])
            s2 = np.dot(A[j, j + 1:], x[j + 1:])
            x_new[j] = (b[j] - s1 - s2) / A[j, j]
        if np.allclose(x, x_new, rtol=epsilon):
            return x_new
        x = x_new
    return x


def start(choice, number):
    print()
    # first method
    # print("One", gauss_seidel(1, 1))
    # print("Two", gauss_seidel(2, 0.000001))

    # second method
    # array = np.loadtxt("./coefficients.txt", dtype="float", delimiter=",", encoding="utf-8")
    # coefficients = get_coefficients(array)
    # constants = get_constants(array)
    # x = np.zeros(len(coefficients))
    # if not(is_diagonally_dominant(array)):
        # coefficients, constants = make_diagonally_dominant(coefficients, constants)
    # gauss_seidel(coefficients, constants, number, 10)


# print("One", gauss_seidel(coefficients, constants, x, 0.001, 100))
# print("Two", gauss_seidel(coefficients, constants, x, 0.000001, 10000))


# print("One", gauss_seidel(coefficients, constants, x, 0.001, 10))

#
# print("One", gauss_seidel(0.001, 10))
# print("Two", gauss_seidel(0.000001, 10))


# print("Two", gauss_seidel(coefficients, constants, 2, 0.001))
