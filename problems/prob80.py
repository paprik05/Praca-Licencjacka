from sympy import primerange
def prob80(limit):
    solutions = []
    primes = list(primerange(1,limit))

    for r in primes:
        right = r*(r+1)
        for i, p in enumerate(primes):
            if p == r:
                continue
            for q in primes[i:]:
                if q == r:
                    continue
                left = p*(p+1) + q*(q+1)
                if left == right:
                    solutions.append(f"{p}({p} + 1) + {q}({q} + 1)= {r}({r} + 1)")
                    break

    return {"result": solutions}
