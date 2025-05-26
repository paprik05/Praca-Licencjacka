def prob22(r):
    if r <= 0:
        return {"error": "r must be a positive integer"}

    results = []
    for n in range(1, r + 1):
        if (n*2**n+1) % 3 == 0:
            results.append(f"{n}: 3|n*2**n+1 = 3|{n*2**n+1}")

    return {"result": results}
