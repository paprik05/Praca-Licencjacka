def prob18(r):
    if r <= 0:
        return {"error": "r must be a positive integer"}

    results = []
    n = 1
    while len(results) < r:
        if (2**n + 2) % n == 0:
            results.append(f"{n}: n|2^n+2 = {n}|{2**n+2}")
        n += 1

    return {"result": results}
