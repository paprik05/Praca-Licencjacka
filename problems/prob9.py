def prob9(n):
    if n <= 0:
        return {"error": "n musi być liczbą całkowitą dodatnią"}

    sum1 = sum(i**5 for i in range(1, n+1))
    sum2 = sum(i**3 for i in range(1, n+1))

    return {"result": (3 * sum1) % sum2 == 0}
