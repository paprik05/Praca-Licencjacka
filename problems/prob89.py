# zapytac sie o koncowke jak to zrobic
from sympy import primerange

def prob89(limit=1000, num_of_results=5):
    counter = 0
    results = []
    consecutive = []
    primes = list(primerange(2,limit+1))

    for n in range(limit):
        git = 0
        found = False
        for i in range(len(primes)):
            for j in range(i+1,len(primes)):
                p = primes[i]
                q = primes[j]

                if n == p * q or n + 1 == p * q or n + 2 == p * q:
                    git += 1

                if git == 3:
                    results.append(n)
                    if n%4 == 0:
                        consecutive.append({n, n+1, n+2, n+3})
                    counter += 1
                    found = True
                    break

            if found:
                break
        if counter >= num_of_results:
            break

        for i in range(len(results) - 3):
            if results[i + 1] == results[i] + 1 and results[i + 2] == results[i] + 2 and results[i + 3] == results[i] + 3:
                consecutive.append({results[i], results[i + 1], results[i + 2], results[i + 3]})

    return {"result": f"Pierwsze pięć liczb dla któych warunek jest spełniony: {results}, Consecutive: {consecutive}"}