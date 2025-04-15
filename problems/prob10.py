def prob10(r):
    if r <= 1:
        return {"error": "r musi być większe od 1"}

    results = []
    for n in range(2, r + 1):
        if sum(i**n for i in range(1, n)) % n == 0:
            results.append(n)

    return {"result": results}
