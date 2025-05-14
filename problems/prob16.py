import sympy

def prob16(r):
    if r <= 0:
        return {"error": "r musi być liczbą całkowitą dodatnią"}

    results = []
    prime_results = []
    n = 1

    while len(results) < r:
        if (2 ** n + 1) % n == 0:
            results.append(f"{n}: n|2^n+1 = {n}|{2**n+1}")
            if sympy.isprime(n):
                prime_results.append(n)
        n += 1

    return {"result": f"{results}, All such prime numbers of results: {prime_results}"}
