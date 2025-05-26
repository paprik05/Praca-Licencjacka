from sympy import isprime, factorint

def has_only_one_prime_factor(x):
    factors = factorint(x)
    return len(factors) == 1

def prob90(limit=100000):
    results = []
    for n in range(2, limit):
        if has_only_one_prime_factor(n) and has_only_one_prime_factor(n + 1):
            results.append(f"n = {n}: {n} = {list(factorint(n).items())[0][0]}^{list(factorint(n).items())[0][1]}, "
                           f"{n+1} = {list(factorint(n+1).items())[0][0]}^{list(factorint(n+1).items())[0][1]}")
    return {"result": results}