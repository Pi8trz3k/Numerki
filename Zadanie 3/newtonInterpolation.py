import numpy as np


def equidistant_nods(a_interval_beg_point, b_interval_end_point, number_of_points):
    length = (b_interval_end_point - a_interval_beg_point) / (number_of_points - 1)
    x = np.zeros(number_of_points)
    for i in range(number_of_points):
        x[i] = a_interval_beg_point + i * length

    return x

