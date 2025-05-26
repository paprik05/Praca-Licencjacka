from sympy import primerange, factorint

def prob94(n_min=5, n_max=100):
    results = []

    for n in range(n_min, n_max + 1):
        interval = range(n + 1, 2 * n + 1)

        has_two_distinct = False
        has_three_distinct = False

        for x in interval:
            factors = factorint(x)
            distinct_count = len(factors)

            if distinct_count >= 2:
                has_two_distinct = True
            if distinct_count >= 3:
                has_three_distinct = True

            if has_two_distinct and (n <= 15 or has_three_distinct):
                break

        results.append(f"n: {n}, exists_two_distinct_prime_factors: {has_two_distinct}, exists_three_distinct_prime_factors: {has_three_distinct if n > 15 else "N/A (n<=15)"}")

    return {"result": results}