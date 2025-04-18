from sympy import isprime
def prob76(limit):
    results_n = []
    for n in range(limit + 1):
        has_prime = False
        if len(results_n) < 3:
            for i in range(n+1, n + 10):
                if isprime(i):
                    has_prime = True
                    break
            if not has_prime:
                results_n.append(n)

    results_m = []
    for m in range(limit + 1):
        has_prime = False
        if len(results_m) < 3:
            for j in range(10*m+1, 10*(m+1)):
                if isprime(j):
                    has_prime = True
                    break
            if not has_prime:
                results_m.append(m)

    return {"result": f"Result for n:'{results_n}, Result for m:'{results_m}'"}