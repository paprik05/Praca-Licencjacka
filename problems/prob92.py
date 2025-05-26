from sympy import prime, primerange
from .prob47 import prob47

def prob92(k):
    if k < 3:
        return {"error": "k must be greater than or equal to 3"}

    primes = list(primerange(1, prime(k) + 1))[:k]
    product = 1
    for p in primes:
        product *= p

    pk1 = prime(k+1)
    pk2 = prime(k+2)

    coprime_pair = prob47(product)["result"]
    inequality = pk1 + pk2 <= product

    return {"result": f"{inequality}, {pk1} + {pk2} <= {product}"}


