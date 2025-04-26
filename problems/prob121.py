from sympy import isprime
def prob121(k, limit=100):
    if k > 10:
        return {"error": "k musi byc liczbą dodatnią, nie większą niż 10"}

    for n in range(1, limit+1):
        result = k * pow(2,pow(2,n)) + 1

        if not isprime(result):
            return {"result": n}
