from sympy import isprime
def prob99(limit=10):
    results=[]

    for n in range(2, limit+1):
        formula = int(1/5 * (pow(2,4*n+2) + 1))
        if not isprime(formula):
            results.append(f"n = {n}, $$\\frac{{1}}{{5}}(2^{{4*{n}+2}} + 1) = {formula}$$")

    return {"result": results}