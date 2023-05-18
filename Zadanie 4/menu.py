import numerical_integration as ni
import get_user_inputs

a, b, eps, chosen_func = get_user_inputs.get_data_from_user()

print("Metoda Simpsona", ni.simpson(a, b, chosen_func, eps))
print("Kwadratura Gaussa Legendre'a dla 2 wezłów: ", ni.gaussa_legendre(a, b, chosen_func, 2))
print("Kwadratura Gaussa Legendre'a dla 3 wezłów: ", ni.gaussa_legendre(a, b, chosen_func, 3))
print("Kwadratura Gaussa Legendre'a dla 4 wezłów: ", ni.gaussa_legendre(a, b, chosen_func, 4))
print("Kwadratura Gaussa Legendre'a dla 5 wezłów: ", ni.gaussa_legendre(a, b, chosen_func, 5))
