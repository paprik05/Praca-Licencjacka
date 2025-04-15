import math

def prob68(a, b, n):

    terms = []
    for k in range(0, n+1):
        terms.append(a*k+b)

    relatively_prime_terms = []
    if len(terms) > 0:
        relatively_prime_terms.append(terms[0])

    for i in range(len(terms)):
        is_relatively_prime = True
        for existing_term in relatively_prime_terms:
            if math.gcd(terms[i], existing_term) != 1:
                is_relatively_prime = False
                break
        if is_relatively_prime:
            relatively_prime_terms.append(terms[i])

    return {"result": relatively_prime_terms}