from sympy import isprime

def prob120(m,n_range=10):
    results = []

    k = pow(2,m)
    for n in range(1, n_range + 1):
        power = 2 ** n
        value = k * (2 ** power) + 1


        if not isprime(value):
            results.append(f"n = {n}, k = {k}, is composite")

    return {"result": results}
