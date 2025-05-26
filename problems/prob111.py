from sympy import primerange

def is_square(x, limit=1000):
    for n in range(limit):
        if n * n == x:
            return True
    return False

def prob111(limit=100):
    results = []
    primes = list(primerange(1, limit + 1))
    for p in primes:
        divisor_sum = 1 + p + p**2 + p**3 + p**4
        if is_square(divisor_sum):
            results.append(p)
    return {"result": results}
