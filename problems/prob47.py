from math import gcd
def prob47(n):
    if n <= 0:
        return {"error": "n must be a positive integer"}
    for i in range(2, n + 1):
        j = n - i
        if i > 1 and j > 1 and gcd(i, j) == 1:
            return {"result": f"{n}: {(i, j)}"}
    return {"result ": None}