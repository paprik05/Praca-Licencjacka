from sympy import isprime
def prob98(limit=10):
    results = []

    for n in range(1,limit+1):
        formula = pow(10,n) + 3
        if not isprime(formula):
            results.append(n)

    return {"result:": results}