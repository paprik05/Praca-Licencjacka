from math import gcd


def prob44(a, b, limit):
    if a == b:
        return {"error": "A and B muszą być od siebie różne"}
    if limit <= 0:
        return {"error": "zmienna limit musi być liczbą całkowitą dodatnią"}

    results = []
    for n in range(1, limit + 1):
        if gcd(a+n, b+n) == 1:
            results.append(n)

    return {"result": results}