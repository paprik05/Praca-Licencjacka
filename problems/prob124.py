from sympy import isprime

def prob124(n_range=10):
    results = []

    for i in range(1, n_range+1):
        value = (pow(2,2*i) + 1)**2 + pow(2,2)

        if not isprime(value):
            results.append(f"n = {i}, \\( \\left(2^{{2*{i} + 1}}\\right)^2 + 2^2 \\) = {value}")

    return {"result": results}