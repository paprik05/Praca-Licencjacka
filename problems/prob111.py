from sympy import primerange
def square(x ,limit = 1000):
    for n in range(limit):
        if x == n**2:
            return n


def prob111(limit = 100):
    results = []
    primes = list(primerange(limit+1))
    for p in primes:
        sum = 1 + p + p**2 + p**3 + p**4
        if square(sum, limit):
            results.append(p)

    return {"result": results}
