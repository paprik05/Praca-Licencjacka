from sympy import primerange
def prob83(limit=10, num_of_results=5):
    counter = 0
    results = []
    primes = list(primerange(2, limit + 1))

    for p in primes:
        for i in range(p):
            for j in range(i,p):
                if pow(i,4) + pow(j,4) == p:
                    results.append(f"p = {p}: {p} = {i}^4 + {j}^4")
                    counter += 1
        if counter >= num_of_results:
            break

    return {"result": results}