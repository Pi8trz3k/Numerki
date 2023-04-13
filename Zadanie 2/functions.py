import numpy as np


# checking if matrix is diagonally dominant
def is_diagonally_dominant(array):
    tab_len = len(array)
    for i in range(tab_len):
        row_sum = np.sum(abs(array[i]))
        print(row_sum)
        diagonal_number = abs(array[i][i])
        row_sum_without_diagonal_number = row_sum - diagonal_number
        if diagonal_number <= row_sum_without_diagonal_number:
            return False
    return True


# returning array that don't contain result numbers(last numbers in every row is rejected)
def get_array_without_results_numbers(array):
    array_len = len(array)
    coefficients = np.zeros((array_len, array_len))

    for i in range(array_len):
        for j in range(array_len):
            coefficients[i][j] = array[i][j]
    return coefficients


def make_diagonally_dominant(array):
    array_len = len(array)
    # array that have ones inside, used later
    # zeros_array = np.ones(array_len)
    #
    # for i in range(array_len):
    #     row_sum = np.sum(abs(array[i]))
    #     diagonal_number = abs(array[i][i])
    #     if diagonal_number < row_sum - diagonal_number:
    #         zeros_array[i] = 0
    #
    # print(zeros_array)
    for i in range(array_len):
        row_sum = np.sum(np.abs(array[i]) - np.abs(array[i][i]))
        if np.abs(array[i, i]) <= row_sum:
            max_index = np.argmax(np.abs(array[i, :]))
            array[[i, max_index], :] = array[[max_index, i], :]
    return array


coefficients_with_results = np.loadtxt("./coefficients.txt", dtype="int", delimiter=",")
coefficients_only = get_array_without_results_numbers(coefficients_with_results)
# print(is_diagonally_dominant(coefficients_only))
# print(coefficients_only)
print(make_diagonally_dominant(coefficients_only))
