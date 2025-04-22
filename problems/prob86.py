from sympy import primerange
def prob86(limit, num_of_results = 5):
    counter = 0
    results = []
    primes = list(primerange(limit + 1))

    for n in range(2, limit+1):
        test_case = (n-1)*(n+1)
        for i in range(len(primes)):
            for j in range(i + 1, len(primes)):
                for k in range(j + 1, len(primes)):
                    p = primes[i]
                    q = primes[j]
                    r = primes[k]
                    if test_case == p*q*r:
                        results.append(n)
                        counter += 1
        if counter >= num_of_results:
            break

    return {"result:": results}