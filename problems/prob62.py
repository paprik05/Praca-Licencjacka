from math import gcd, prod
from sympy import primefactors


def prob62(a, b, m, n_terms):
    P = 1
    Q = 1
    R = 1

    prime_divisors_m = set(primefactors(m))
    prime_divisors_a = set(primefactors(a))
    prime_divisors_b = set(primefactors(b))

    P = 1 if not (prime_divisors_m & prime_divisors_a) else prod(prime_divisors_m & prime_divisors_a)
    Q = 1 if not (prime_divisors_m & prime_divisors_b) else prod(prime_divisors_m & prime_divisors_b)
    R = 1 if not (prime_divisors_m - (prime_divisors_a | prime_divisors_b)) else prod(
        prime_divisors_m - (prime_divisors_a | prime_divisors_b))

    terms = [(a * (k * m + P * R) + b) for k in range(n_terms)]
    return {"result": [t for t in terms if gcd(t, m) == 1]}
