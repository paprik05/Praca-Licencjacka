import sympy

def prob30(a):
    if a <= 0:
        return {"error": "a musi być liczbą całkowitą dodatnią większą od 1"}

    n = 4

    while True:
        if sympy.isprime(n) == False and (a**n-a) % n == 0:
            return {"result": f"{n}: {n}|{a**n-a} = {(a**n-a) / n}"}
        n += 1

