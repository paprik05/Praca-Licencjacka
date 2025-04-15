def prob4(r):
    if r <= 0:
        return {"error": "r musi być liczbą całkowitą dodatnią"}

    results = []
    for n in range(1, r):
        if (3**(3*n+3)-26*n-27)%169 == 0:
            results.append(n)

    return {"result": results}
