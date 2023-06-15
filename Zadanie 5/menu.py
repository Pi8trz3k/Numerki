from approximation import *
from functions import *
import user_input
import numpy as np
import matplotlib.pyplot as plt


def get_polynominal_string(tab):
    text = ""
    x = len(tab) - 1
    for i in tab:
        if i != 0:
            char = ""
            if i > 0:
                char = " +"

            if x == 1:
                append = "x"
            elif x == 0:
                append = ""
            else:
                append = "x^" + str(x) + char + " "

            text += str(i) + append
        x -= 1

    return text


func_choice, nodes, polynominal_degree = \
    user_input.get_functions(), user_input.get_nodes(), user_input.get_polynominal_degree()

a, b = user_input.get_interval()

wsp = get_polynominal_coefficients(a, b, func_choice, nodes, polynominal_degree)
message = get_polynominal_string(wsp)


print("Wielomian: ", message)
err = error(func_choice, polynominal_degree, wsp, nodes)
print("Błąd: ", err)

space = np.linspace(a, b, 1000)
plt.plot(space, choose(space, func_choice), c='black', ls='-')
plt.plot(space, get_polynominal_values(polynominal_degree, space, wsp), c='red')
plt.legend(['Funkcja aproksymowana', 'Aproksymacja'])
plt.show()
