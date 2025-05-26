from math import gcd

def prob51a(n_range):
    if n_range <= 0:
        return {"error": "n must be a positive integer"}

    results = []

    n = 1
    while len(results) < n_range:
        x = pow(2, n) - 1
        if gcd(n, x) > 1:
            results.append(f"{n}: ({n},{2**n-1}) > 1, {gcd(n, x) > 1}")
        n += 1

    return {"result": results}
