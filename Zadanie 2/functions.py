import numpy as np


# checking if matrix is diagonally dominant
def is_diagonally_dominant(array_input):
    tab_len = len(array_input)
    for i in range(tab_len):
        row_sum = np.sum(abs(array_input[i]))
        print(row_sum)
        diagonal_number = abs(array_input[i][i])
        row_sum_without_diagonal_number = row_sum - diagonal_number
        if diagonal_number <= row_sum_without_diagonal_number:
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


def make_diagonally_dominant(coefficients_array):
    array_len = len(coefficients_array)

    for i in range(array_len):
        row_sum = np.sum(np.abs(coefficients_array[i]) - np.abs(coefficients_array[i][i]))
        if np.abs(coefficients_array[i, i]) <= row_sum:
            max_index = np.argmax(np.abs(coefficients_array[i, :]))
            coefficients_array[[i, max_index], :] = coefficients_array[[max_index, i], :]
    return coefficients_array


array = np.loadtxt("./coefficients.txt", dtype="int", delimiter=",")
coefficients = get_coefficients(array)
constants = get_constants(array)

print(make_diagonally_dominant(coefficients))
print(constants)
