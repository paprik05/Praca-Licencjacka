from sympy import isprime
def prob71(diff=100, length=3, limit=100000):
    results = []

    for start in range(2, limit):
        if isprime(start) and isprime(start + diff) and isprime(start + 2 * diff):
            progression = [start]
            next_term = start + diff
            while isprime(next_term):
                progression.append(next_term)
                next_term += diff
            if len(progression) >= length:
                results.append(progression)

    return {"result": results}