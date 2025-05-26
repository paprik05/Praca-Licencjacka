from sympy import primerange, isprime
def prob85(n, limit=10000):
    results = []
    primes = list(primerange(3, limit))

    for p in primes:
        if not isprime(p - 2) and not isprime(p + 2):
            results.append(f"Prime {p} is not in any twin prime pair.")
            if len(results) == n:
                break

    return {"result": results}