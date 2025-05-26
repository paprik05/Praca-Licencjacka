import sympy

def generate_sequence(n):
    return int('3' * n + '1')

def prob96(limit=100, required_composites=6):
    composites = []

    for n in range(limit):
        term = generate_sequence(n)
        if term == 1:
            continue
        if not sympy.isprime(term):
            composites.append(term)
            if len(composites) >= required_composites:
                break

    first_composite = composites[0] if composites else None
    return {"result": f"First composite:{first_composite}, All composites {composites}"}