def prob20(r):
    if r <= 1:
        return {"error": "r must be a positive integer greater than 1"}

    results = []
    for n in range(2, r):
        if (2**n - 1) % n == 0:
            results.append(f"{n}: n|2^n-1 = {n}|{2**n-1}")

    return {"result": results}
