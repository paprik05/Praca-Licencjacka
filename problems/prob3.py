def prob3(r):
    if r <= 0:
        return {"error": "r musi być liczbą całkowitą dodatnią"}

    results = []
    for n in range(1, r + 1):
        if (4*n**2+1) % 5 == 0 and (4*n**2+1) % 13 == 0:
            results.append(n)

    return {"result": results}