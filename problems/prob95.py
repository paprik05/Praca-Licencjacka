from sympy import primerange
from math import prod

def prime_factors_distinct(n):
    factors = set()
    x = n
    for p in primerange(2, int(n**0.5) + 1):
        if x % p == 0:
            factors.add(p)
            while x % p == 0:
                x //= p
    if x > 1:
        factors.add(x)
    return factors

def is_product_of_s_distinct_primes(n, s):
    factors = prime_factors_distinct(n)
    return len(factors) == s and prod(factors) == n

def prob95(s, start_n=10, end_n=100):
    results = []
    for n in range(start_n, end_n + 1):
        found = False
        for candidate in range(n, 2 * n + 1):
            if is_product_of_s_distinct_primes(candidate, s):
                results.append(f"For n={n}, found {candidate} as product of {s} distinct primes")
                found = True
                break
        if not found:
            results.append(f"For n={n}, no product of {s} distinct primes found in [{n}, {2*n}]")
    return {"result": results}