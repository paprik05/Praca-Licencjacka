from sympy import isprime
def prob123(n_range=10):
    results = []

    for i in range(1, n_range+1):
        value = pow(2, pow(2, i + 1)) + pow(2, pow(2, i)) + 1
        result = value // 3

        if not isprime(result):
            results.append(f"n = {i}, \\( \\frac{{1}}{{3}}\\left(2^{{2^{{{i + 1}}}}} + 2^{{2^{i}}} + 1\\right) \\) = {result}")

    return {"result": results}