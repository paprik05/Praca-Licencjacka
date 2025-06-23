def prob5(r):
    if r <= 0:
        return {"error": "r must be a positive integer"}

    results = []

    for k in range(0, r + 1):
        if (2**(2**(6*k + 2)) + 3) % 19 == 0:
            results.append(k)

    return {"result": results}
