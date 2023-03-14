import horner
import math

def polynominal(x):
    coefficents = [2,5,2]
    return horner.horner(coefficents, len(coefficents),x);

def cos(number):
    return math.cos(number)

def exponential(number):
    return 2 ** number

def polynominal_cos(number):
    return polynominal(cos(number))

def polynmoinal_exponential(number):
    return polynominal(exponential(number))
