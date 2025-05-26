def prob21(r):
    if r <= 0:
        return {"error": "r must be a positive integer"}

    results = []
    for n in range(1,r + 1):
        if n % 2 == 1 and (3**n+1) % n == 0:
            results.append(f"{n}: n|3^n+1 = {n}|{3**n+1}")

    return {"result": results}
