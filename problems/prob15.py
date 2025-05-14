def prob15(n):
    if n <= 0:
        return {"error": "n musi być liczbą całkowitą dodatnią"}

    return {"result": f"{n}:{(pow(2, (2**n - 1) * n) - 1) % (2**n - 1)**2 == 0}"}

