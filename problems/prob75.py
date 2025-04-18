from sympy import primerange

def prob75(limit):
    primes = list(primerange(2, limit + 1))
    primes_set = set(primes)
    result = []

    for p in primes:
        can_be_sum = any((p - q in primes_set) for q in primes if q <= p // 2)

        can_be_diff = any((q - p in primes_set) for q in primes if q > p)

        print(p)

        if can_be_sum and can_be_diff:
            result.append(p)

    return {"result": f"Primes that can be both sum and difference of two primes in limit '{limit}':'{result}'"}