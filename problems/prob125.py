from sympy import isprime
def prob125(a):
    if a < 1 or a > 100:
        return {"error": "a musi byc liczbą dodatnią, w przedziale 1-100"}

    results = []
    for n in range(1,7):
        value = pow(a,pow(2,n)) + 1

        if not isprime(value):
            results.append((a,n))


    return {"result": results}