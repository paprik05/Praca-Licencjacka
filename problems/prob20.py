def prob20(r):
    if r <= 1:
        return {"error": "r musi być liczbą całkowitą dodatnią większą od 1"}

    results = []
    for n in range(2, r):
        if (2**n - 1) % n == 0:
            results.append(n)

    return {"result": results}
