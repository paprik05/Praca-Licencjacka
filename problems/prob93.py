from sympy import prime, primerange
from math import prod
from .prob92 import prob92
def prob93(max_k=20):
    results = []

    for k in range(3, max_k + 1):
        primes = list(primerange(1, prime(k) + 1))[:k]
        product = prod(primes)
        qn = prime(k + 1)
        ratio = qn / product
        p92 = prob92(k)
        results.append(f"k={k}, n={product}, q_n={qn}, ratio(q_n/n)={ratio:.6e}, "
                   f"prob92 inequality={p92['result']}, detail: {p92['detail']}")
    return {"result": results}