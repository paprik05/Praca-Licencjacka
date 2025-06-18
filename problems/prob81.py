from sympy import isprime, primerange

def prob81(limit=1000):
    primes = list(primerange(2, limit))
    results = []

    for i, p in enumerate(primes):
        for j in range(i+1, len(primes)):
            q = primes[j]
            for k in range(j+1, len(primes)):
                r = primes[k]
                T1 = p * (p + 1)
                T2 = q * (q + 1)
                T3 = r * (r + 1)
                if 2 * T2 == T1 + T3:
                    results.append(f"p= {p},q= {q},r= {r}")
    return {"result": results}