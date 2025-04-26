#dokonczyc
from sympy import primerange
def prob91(limit=1000):
    results = []
    primes = list(primerange(2,limit+1))

    for n in range(19): # nie przekroczy miliona
        form = pow(2,n) - 1
        for i in range(len(primes)):
            for j in range(i+1,len(primes)):
                p = primes[i]
                q = primes[j]

                if form == p*q:
                    results.append((p, q, form))

    return {"result": results}
