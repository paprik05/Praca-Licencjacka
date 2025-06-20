def prob12(n, max_x, iterations):
    if n <= 0 or max_x <= 0 or iterations <= 0:
        raise ValueError("n, max_x, iterations must be a positive integers")

    for x in range(1, max_x + 1):
        current_x = x
        current_term = current_x + 1
        all_divisible = True

        for _ in range(iterations + 1):
            if current_term % n != 0:
                all_divisible = False
                break
            current_x = pow(current_x, x)
            current_term = current_x + 1

        if all_divisible:
            return {"result": x}

    return {"result": False}