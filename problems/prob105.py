from sympy import primerange

def prob105(limit=1000,num_of_results=1):
    results = []
    counter = 0
    primes = list(primerange(1,limit+1))

    for p in primes:
        div1 = set([i for i in primes if (p-1)%i == 0])
        div2 = set([i for i in primes if (p+1)%i == 0])

        dif = div1.symmetric_difference(div2)

        if len(div1) >= 3 and len(div2) >= 3 and len(dif) >= 3:
            results.append(p)
            counter += 1

        if counter >= num_of_results:
            break

    return {"result": results}