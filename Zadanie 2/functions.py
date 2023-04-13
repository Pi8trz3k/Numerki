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


