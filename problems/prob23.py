import sympy

def prob23(p, n_range):
    if p <= 0 or n_range <= 0:
        return {"error": "arguments must be a positive integers"}
    if not sympy.isprime(p):
        return {"error": "p must be a prime number"}

    results = []
    n = 1
    while len(results) < n_range:
        if (n*2**n+1) % p == 0:
            results.append(f"{n}: p|n*2^n+1 = {p}|{n*2**n+1}")
        n += 1

    return {"result": results}
