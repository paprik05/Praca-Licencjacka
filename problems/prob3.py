def prob3(r):
    if r <= 0:
        return {"error": "r musi być liczbą całkowitą dodatnią"}

    results = []
    n = 1
    while len(results) < r:
        val = 4 * n ** 2 + 1
        if val % 5 == 0 and val % 13 == 0:
            results.append(n)
        n += 1

    return {"result": results}