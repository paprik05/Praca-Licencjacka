from sympy import isprime, primerange
from math import prod


#?
def prob58(s):
    primes = list(primerange(1, 100))[:s]  # Get first s primes
    P = prod(primes)  # Compute P = P1 * P2 * ... * Ps

    a = []
    for k in range(s):
        pk = primes[k]
        Pk = P // pk
        for ak in range(1, P):
            if ak % Pk == 0 and ak % pk == -1 % pk:
                a.append(ak)
                break

    Q = prod(a)
    return {"result": [k * Q for k in range(1, s + 1)]}
