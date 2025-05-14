from math import gcd


def prob44(a, b, limit):
    if a == b:
        return {"error": "A and B muszą być od siebie różne"}
    if limit <= 0:
        return {"error": "zmienna limit musi być liczbą całkowitą dodatnią"}

    results = []
    n = 1
    while len(results) < limit:
        if gcd(a+n, b+n) == 1:
            results.append(f"n = {n},because a+n: {a} + {n} = {a+n}, b+n: {b} + {n} = {b+n}")
        n += 1

    return {"result": results}