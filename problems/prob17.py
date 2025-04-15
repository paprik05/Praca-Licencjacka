def prob17(a, r):
    if a <= 0 and r <= 0:
        return {"error": "a, r muszą być liczbami całkowitymi dodatnimi"}
    results = []
    for n in range(1, r + 1):
        if (a**n + 1) % n == 0:
            results.append(n)
    return {"result": results}
