def prob16(r):
    if r <= 0:
        return {"error": "r musi być liczbą całkowitą dodatnią"}

    results = []
    for n in range(1, r + 1):
        if (2**n + 1) % n == 0:
            results.append(n)

    return {"result": results}

# prime_num = []
# for p in numbers:
#     if sympy.isprime(p):
#         prime_num.append(p)
