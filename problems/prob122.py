from sympy import isprime
def prob122(limit=10):
    results = []

    for k in range(1,11):
        composite = True
        for n in range(1,limit+1):
            result = k * pow(2, pow(2, n)) + 1

            if isprime(result):
                composite = False
                break

        if composite:
            results.append(k)

    return {"result": results}