def prob9(n):
    if n <= 0:
        return {"error": "n must be a positive integer"}

    sum1 = sum(i**5 for i in range(1, n+1))
    sum2 = sum(i**3 for i in range(1, n+1))

    return {"result": f"{n}:{(3 * sum1) % sum2 == 0}"}
