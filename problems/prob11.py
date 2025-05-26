def prob11(n):
    if n <= 0:
        return {"error": "n must be a positive integer"}

    a = 2 ** (2 * n + 1) - 2 ** (n + 1) + 1
    b = 2 ** (2 * n + 1) + 2 ** (n + 1) + 1

    results = {
        "a": a % 5 == 0,
        "b": b % 5 == 0
    }

    return {"result": results}
