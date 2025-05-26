def prob35(n):
    if n <= 0:
        return {"error": "n must be a positive integer"}


    pairs = []
    k = 0

    while len(pairs) < n:
        x = 36 * k + 14
        y = (12 * k + 5) * (18 * k + 7)

        if (
            (y * (y + 1)) % (x * (x + 1)) == 0 and  # Condition 1
            y % x != 0 and                          # Condition 2
            y % x + 1 != 0 and                      # Condition 3
            (y + 1) % x != 0 and                    # Condition 4
            (y + 1) % (x + 1) != 0                  # Condition 5
        ):
            pairs.append((x, y))

        k += 1

    return {"result": pairs}