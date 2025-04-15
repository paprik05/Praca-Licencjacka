from math import gcd


def fibonacci(u):

    if u == 1 or u == 2:
        return 1

    else:
        return fibonacci(u-1) + fibonacci(u-2)


def prob50(r):
    results = {}
    for i in range(1, r+1):
        if gcd(fibonacci(i), fibonacci(i+1)) == 1:
            results[i] = i+1
    return {"result": results}
