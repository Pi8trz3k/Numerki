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



