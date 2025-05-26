def prob39(a, b, c, n):
    if n <= 3:
        return {"error": "n must be a positive integer greater than 1"}

    k = 0
    while (k + a) % n == 0 or (k + b) % n == 0 or (k + c) % n == 0:
        k += 1
    return {"result": f"k: {k}"}
