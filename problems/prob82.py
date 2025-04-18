from sympy import isprime
def prob82(limit):
    results = []

    for n in range(1, limit):
        if isprime(n+1) and isprime(n+3) and isprime(n+7) and isprime(n+9) and isprime(n+13) and isprime(n+15):
            results.append(n)

    return {"result": results}

