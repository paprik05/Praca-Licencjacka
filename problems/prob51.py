from math import gcd

def prob51(n):
    if n <= 0:
        return {"error": "n must be a positive integer"}

    x = pow(2,pow(2,n)) + 1

    if gcd(n, x) == 1:
        return {"result": f"({n},{2**(2**n)+1}) == 1, {True}"}
    else:
        return {"result": f"({n},{2**(2**n)+1}) == 1, {False}"}
