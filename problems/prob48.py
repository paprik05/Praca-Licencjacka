from math import gcd

def prob48(n):
    if n <= 16:
        return {"error": "n must be greater than 17"}
    for i in range(2, n - 3):
        for j in range(i+1, n-i-1):
            k = n - i - j
            if k > 1 and i > 1 and j > 1 and gcd(i, j) == 1 and gcd(i,k) == 1 and gcd(j,k) == 1:
                return {"result": f"{n}: {(i, j, k)}"}
    return {"result": []}