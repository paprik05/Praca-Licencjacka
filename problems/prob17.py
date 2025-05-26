def prob17(a, r):
    if a <= 0 and r <= 0:
        return {"error": "a and r must be a positive integers"}
    results = []
    n = 1
    while len(results) < r:
        if (a**n + 1) % n == 0:
            results.append(f"{n}: n|a^n+1 = {n}|{a**n+1}")
        n+=1
    return {"result": results}
