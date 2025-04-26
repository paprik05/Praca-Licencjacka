from math import gcd
def prob47(n):
    if n <= 0:
        return {"error": "n musi być liczbą całkowitą dodatnią"}
    for i in range(2, n + 1):
        j = n - i
        if i > 1 and j > 1 and gcd(i, j) == 1:
            return {"result": (i, j)}
    return {"result ": None}