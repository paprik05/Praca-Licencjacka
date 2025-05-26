from sympy import primerange, isprime, factorint

def prob91():
    results = []

    for n in range(2, 20):  # bo 2^20 > 1_000_000
        num = 2 ** n - 1

        if isprime(num):
            continue

        factors = factorint(num)
        total_factors = sum(factors.values())

        if total_factors == 2:
            primes = list(factors.keys())
            results.append(f"n = {n}: {num} = {primes[0]} * {primes[1]}")
        elif n % 2 == 0 and n > 4 and total_factors >= 3:
            results.append(f"n = {n}: {num} is a product of at least 3 integers > 1")

    return {"result": results}
