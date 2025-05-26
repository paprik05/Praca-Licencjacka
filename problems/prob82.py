from sympy import isprime
def prob82(limit):
    results = []

    for n in range(1, limit):
        if isprime(n+1) and isprime(n+3) and isprime(n+7) and isprime(n+9) and isprime(n+13) and isprime(n+15):
            results.append(f"n = {n}: {n+1,n+3,n+7,n+9,n+13,n+15}")

    return {"result": results}

