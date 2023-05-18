# example [1, 1, 2] => 1 + x + 2x^2
def horner(coefficients, len_table, x):
    i = len_table - 1
    result = coefficients[i]
    while i > 0:
        i = i - 1
        result = result * x + coefficients[i]
    return result
