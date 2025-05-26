from sympy import isprime
def prob125(a):
    if a < 1 or a > 100:
        return {"error": "a must be a positive number in the range 1–100"}

    results = []
    for n in range(1,7):
        value = pow(a,pow(2,n)) + 1

        if not isprime(value):
            results.append(f"n = {n}, \\(a^{{2^{{n+1}}}} = {value}\\)")

    return {"result": results}