def prob14(n):
    if n <= 0:
        return {"error": "n must be a positive integer"}

    return {"result": f"{n}:{((n + 1)**n - 1) % (n**2) == 0}"}

