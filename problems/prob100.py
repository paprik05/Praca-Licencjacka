import math
import sympy
def prob100(m):
    factorial_m = math.factorial(m)
    composites = []

    for k in range(2, m + 1):
        n = factorial_m + k
        term = pow(2, n) - 1
        if sympy.isprime(term):
            return False, None
        else:
            composites.append(f"(n = {n}, term = {term})")

    return {"result": composites}