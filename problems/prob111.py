from sympy import primerange
def help(x ,limit = 1000):
    for n in range(limit):
        if x == n**2:
            return n

def prob111(limit = 100):
    results=[]
    primes = list(primerange(limit+1))
    for p in primes:
        sum = 0
        for n in range(1,limit):
            if pow(p,4) % n == 0:
                sum += n
        if help(sum):
            results.append(p)

    return {"result:": results}
