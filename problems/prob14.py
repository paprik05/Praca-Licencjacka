def prob14(n):
    if n <= 0:
        return {"error": "n musi być liczbą całkowitą dodatnią"}

    return {"result": ((n + 1)**n - 1) % (n**2) == 0}
