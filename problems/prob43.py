from math import gcd
def tetrahedral_number(n):
    return n * (n + 1) * (n+2) // 6

def prob43(limit):
    if limit <= 0:
        return {"error": "n musi być liczbą całkowitą dodatnią"}

    sequence = []
    n = 1
    while len(sequence) < limit:
        tn = tetrahedral_number(n)
        if all(gcd(tn, t) == 1 for t in sequence):
            sequence.append(tn)
        n += 1
    return {"result": sequence}