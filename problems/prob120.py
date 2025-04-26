import time
from sympy import isprime

def prob120(m,n_range=10, max_time=5):
    results = []

    k = pow(2,m)
    for n in range(1, n_range + 1):
        start_time = time.time()
        power = 2 ** n
        value = k * (2 ** power) + 1

        if time.time() - start_time > max_time:
            break

        if not isprime(value):
            results.append(f"n = {n}, k = {k}, is composite")

    return {"result": results}
