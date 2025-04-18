from sympy import primerange
def prob78(limit, num_of_solutions = 4):
    solutions = []
    count = 0
    primes = list(primerange(1,limit))

    while count < num_of_solutions:
        for p in primes:
            left = pow(p,2) + 1
            for i, q in enumerate(primes):
                if q == p:
                    continue
                for r in primes[i:]:
                    if r == p:
                        continue
                    right = pow(q,2) + pow(r,2)
                    if left == right:
                        solutions.append(f"{p}^2 + 1 = {q}^2 + {r}^2")
                        count += 1
                        break
                if count >= num_of_solutions:
                    break

    return {"result": solutions}
