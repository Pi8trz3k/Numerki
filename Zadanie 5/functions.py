import horner as h
import numpy as np


def choose(x, choice):
    if choice == 1:
        return 8 * x + 3
    elif choice == 2:
        return np.sin(x)
    elif choice == 3:
        coef = [12, 4, -1]
        return h.horner(coef, len(coef), x)
    elif choice == 4:
        return 1 * np.fabs(x)
    elif choice == 5:
        return 8 * np.sin(15 * x) + 3
    elif choice == 6:
        return np.fabs(8 * x - 2)
