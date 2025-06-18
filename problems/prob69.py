from math import gcd
from sympy import primefactors
def is_product_of_s_distinct_primes(n, s):
    factors = primefactors(n)
    product = 1
    for f in factors:
        product *= f
    return len(factors) == s and product == n


def prob69(a, b, s, count=10, limit=100000):
    if gcd(a, b) != 1:
        raise ValueError("a and b must be coprime (gcd(a, b) = 1).")

    results = []
    k = 0
    while len(results) < count and k * a + b < limit:
        term = a * k + b
        if term > 1 and is_product_of_s_distinct_primes(term, s):
            results.append(term)
        k += 1
    return {"result": results}