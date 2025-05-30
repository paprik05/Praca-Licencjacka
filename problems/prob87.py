from sympy import primerange
def prob87(limit=10, num_of_results = 5):
    counter = 0
    results = []
    primes = list(primerange(limit + 1))

    for n in range(2, limit + 1):
        test_case = pow(n,2) + 1
        for i in range(len(primes)):
            for j in range(i + 1, len(primes)):
                for k in range(j + 1, len(primes)):
                    p = primes[i]
                    q = primes[j]
                    r = primes[k]
                    if test_case == p * q * r:
                        results.append(f"n = {n}, n^2-1 = {test_case} = {p} * {q} * {r}")
                        counter += 1
        if counter >= num_of_results:
            break

    for n in range(2, limit+1):
        test_case = pow(n,2) + 1
        for i in range(len(primes)):
            if primes[i] % 2 == 1:
                p = primes[i]
            else:
                continue
            for j in range(i + 1, len(primes)):
                if primes[j] % 2 == 1:
                    q = primes[j]
                else:
                    continue
                for k in range(j + 1, len(primes)):
                    if primes[k] % 2 == 1:
                        r = primes[k]
                    else:
                        continue
                    if test_case == p*q*r:
                        results.append(f"Three different odd primes, n = {n}, n^2-1 = {test_case} = {p} * {q} * {r}")
                        break


    return {"result": results}

