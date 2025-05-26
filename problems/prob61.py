from sympy import primerange
from math import prod

def chinese_remainder_theorem(remainders, moduli):
    M = prod(moduli)
    total = sum(r * (M // m) * pow(M // m, -1, m) for r, m in zip(remainders, moduli))
    return total % M

def prob61(a, b, m):
    primes = list(primerange(a + 1, a + 1000))[:m]
    mods = primes
    remainders = [(-a * j - b) % q for j, q in enumerate(primes, start=1)]
    x = chinese_remainder_theorem(remainders, mods)
    terms = [a * (x + j) + b for j in range(1, m + 1)]
    return {
        "result": f"a = {a}, b = {b}, m = {m}, x = {x}, primes = {primes}, composite_terms = {terms}"
    }