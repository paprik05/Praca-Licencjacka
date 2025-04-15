from sympy import legendre_symbol

def prob57(a, b):
    return {"result": legendre_symbol(b, a) == 1 or b % a == 0}
