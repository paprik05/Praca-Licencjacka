def prob1(r):
    if r <= 0:
        return {"error": "r musi być liczbą całkowitą dodatnią"}

    results = []
    for n in range(1, r + 1):
        if (n**2 + 1) % (n + 1) == 0:
            results.append(n)

    return {"result": results}