from math import gcd

def prob51a(n_range):
    if n_range <= 0:
        return {"error": "n musi być liczbą całkowitą dodatnią"}

    results = []

    for n in range(1, n_range+1):
        x = pow(2, n) - 1
        if gcd(n, x) > 1:
            results.append(n)

    return {"result": results}
