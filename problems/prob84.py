from sympy import isprime, nextprime

def prob84(n):
    results = []
    p = 2
    count = 0

    while count < n:
        q = nextprime(p)
        gap = q - p
        if gap != 2:
            results.append(f"Consecutive primes {p} and {q} have gap {gap} ≠ 2 (not twins)")
            count += 1
        p = q

    return {"result": results}