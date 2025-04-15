def prob13(x, max_n, iterations):
    if x <= 1 or max_n <= 0 or iterations <= 0:
        raise ValueError("x, max_n, iterations muszą być liczbami całkowitymi dodatnimi")

    if x % 2 != 0:
        raise ValueError("x must be even number")

    results = []
    for n in range(1, max_n + 1):
        current_x = x
        current_term = current_x + 1
        all_divisible = True

        for _ in range(iterations + 1):
            if current_term % n != 0:
                all_divisible = False
            else:
                all_divisible = True
            current_x = pow(current_x, x)
            current_term = current_x + 1

        if not all_divisible:
            results.append(n)

    return {"result": results}
