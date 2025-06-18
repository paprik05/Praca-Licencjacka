from sympy import isprime

def prob72(length=10, max_start=10000, max_diff=1000):
    result = None
    min_last_term = float('inf')

    for start in range(2, max_start):
        if not isprime(start):
            continue
        for d in range(1, max_diff):
            sequence = [start + i * d for i in range(length)]
            if all(isprime(term) for term in sequence):
                last_term = sequence[-1]
                if last_term < min_last_term:
                    min_last_term = last_term
                    result = sequence
    return {"result": result}