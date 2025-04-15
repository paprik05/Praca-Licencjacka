def prob39(a, b, c, n):
    if n <= 3:
        return {"error": "n musi być liczbą całkowitą dodatnią większą od 3"}

    for k in range(n + 1):
        if (k + a) % n != 0 and (k + b) % n != 0 and (k + c) % n != 0:
            return {"result": k}
    return {"result": None}
