import numpy as np


# checking if matrix is diagonally dominant
def is_diagonally_dominant(array):
    tab_len = len(array)
    for i in range(tab_len):
        row_sum = np.sum(abs(array[i]))
        print(row_sum)
        for j in range(tab_len):
            if i == j:
                diagonal_number = array[i][j]
                row_sum_without_diagonal_number = row_sum - diagonal_number
                if diagonal_number < row_sum_without_diagonal_number:
                    return False
                print("BBB", row_sum_without_diagonal_number, "| diagonall", diagonal_number)
                # print(diagonal_number)
                # sum of row - last number in row that is result of the equation -

            # print(table[i][j])
    # print(tab_len)



