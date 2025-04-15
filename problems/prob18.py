def prob18(r):
    if r <= 0:
        return {"error": "r musi być liczbą całkowitą dodatnią"}

    results = []
    for n in range(1, r + 1):
        if (2**n + 2) % n == 0:
            results.append(n)

    return {"result": results}
