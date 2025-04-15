from math import gcd

def prob51(n):
    if n <= 0:
        return {"error": "n musi być liczbą całkowitą dodatnią"}

    x = pow(2,pow(2,n)) + 1

    if gcd(n, x) == 1:
        return {"result": True}
    else:
        return {"result": False}
