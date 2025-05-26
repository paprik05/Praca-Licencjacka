from sympy import primerange
def prob79(n=50):
    primes = list(primerange(2, n))
    results = []
    found_solution = False

    for i, p in enumerate(primes):
        for j, q in enumerate(primes):
            if j == i:
                continue
            lhs = p * p + q * q
            for k, r in enumerate(primes):
                if k == i or k == j:
                    continue
                for l, s in enumerate(primes):
                    if l == i or l == j or l == k:
                        continue
                    for m, t in enumerate(primes):
                        if m == i or m == j or m == k or m == l:
                            continue
                        rhs = r * r + s * s + t * t
                        if lhs == rhs:
                            def mod8(x):
                                return (x * x) % 8

                            lhs_mod = (mod8(p) + mod8(q)) % 8
                            rhs_mod = (mod8(r) + mod8(s) + mod8(t)) % 8
                            if lhs_mod != rhs_mod:
                                continue

                            results.append(f"Counterexample found: {p}, {q}, {r}, {s}, {t}")
                            found_solution = True
                            break
                    if found_solution:
                        break
                if found_solution:
                    break
            if found_solution:
                break
        if found_solution:
            break

    if not found_solution:
        results.append(f"No solution with primes p,q,r,s,t found up to {n}.")

    return {"result": results}