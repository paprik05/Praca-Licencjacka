def prob19(r):
    if r <= 0:
        return {"error": "r musi być liczbą całkowitą dodatnią"}

    results = []
    for a in range(1, r + 1):
        if (a**10 + 1) % 10 == 0:
            results.append(f"{a}: 10|a^10+1 = 10|{a**10+1}")

    return {"result": results}
