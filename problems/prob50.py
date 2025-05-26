from math import gcd


fib_cache = {1: 1, 2: 1}


def fibonacci(u):
    if u in fib_cache:
        return fib_cache[u]
    fib_cache[u] = fibonacci(u-1) + fibonacci(u-2)
    return fib_cache[u]


def prob50(r):
    results = []
    for i in range(1, r+1):
        if gcd(fibonacci(i), fibonacci(i+1)) == 1:
            results.append(f"n = {i}, {fibonacci(i)} and {fibonacci(i+1)} are relatively prime")
    return {"result": results}
