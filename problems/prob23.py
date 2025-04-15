import sympy

def prob23(p_range, n_range):
    if p_range <= 0 or n_range <= 0:
        return {"error": "argumenty muszą być liczbami całkowitymi dodatnimi"}

    results = {}
    primes = [p for p in range(1, p_range + 1) if sympy.isprime(p) and p % 2 == 1]

    for p in primes:
        divisible_n = [n for n in range(1, n_range + 1) if (n * 2**n + 1) % p == 0]
        if divisible_n:
            results[p] = divisible_n  # Store n values under corresponding prime p

    return {"result": results}
