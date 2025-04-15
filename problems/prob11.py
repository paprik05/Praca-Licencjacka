def prob11(n):
    if n <= 0:
        return {"error": "n musi być liczbą całkowitą dodatnią"}

    a = 2 ** (2 * n + 1) - 2 ** (n + 1) + 1
    b = 2 ** (2 * n + 1) + 2 ** (n + 1) + 1

    results = {
        "a": a % 5 == 0,
        "b": b % 5 == 0
    }

    return {"result": results}
