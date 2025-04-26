from sympy import primerange, isprime
def prob135(limit):
    results = []
    primes = list(primerange(1,limit+1))

    for p in primes:
        if isprime(p) and isprime(p+2) and isprime(p+6) and isprime(p+8) and isprime(p+12) and isprime(p+14):
            results.append(p)

    return {"result": results}