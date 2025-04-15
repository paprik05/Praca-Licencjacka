from math import gcd
def triangular_number(n):
    return n * (n + 1) // 2

def prob42(limit):
    if limit <= 0:
        return {"error": "n musi być liczbą całkowitą dodatnią"}

    sequence = []
    n = 1
    while len(sequence) < limit:
        tn = triangular_number(n)
        if all(gcd(tn, t) == 1 for t in sequence):
            sequence.append(tn)
        n += 1
    return {"result": sequence}