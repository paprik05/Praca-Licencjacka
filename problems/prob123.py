import time
from sympy import isprime
def prob123(n_range=10,max_time=5):
    results = []

    for i in range(1, n_range+1):
        start_time = time.time()
        value = pow(2, pow(2, i + 1)) + pow(2, pow(2, i)) + 1
        result = value // 3

        if time.time() - start_time > max_time:
            break

        if not isprime(result):
            results.append(i)

    return {"result": results}