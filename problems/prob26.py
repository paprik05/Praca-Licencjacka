def prob26(r):
    if r <= 1:
        return {"error": " musi być liczbą całkowitą dodatnią większą od 1"}

    def is_divisible_by_5(n):
        return (2**n - 3) % 5 == 0

    def is_divisible_by_13(n):
        return (2**n - 3) % 13 == 0

    def is_divisible_by_65(n):
        return (2**n - 3) % 65 == 0

    divisible_by_5 = []
    divisible_by_13 = []
    divisible_by_65 = []

    for n in range(2, r):
        if is_divisible_by_5(n):
            divisible_by_5.append(n)
        if is_divisible_by_13(n):
            divisible_by_13.append(n)
        if is_divisible_by_65(n):
            divisible_by_65.append(n)

    results = {
        "divisible_by_5": divisible_by_5,
        "divisible_by_13": divisible_by_13,
        "divisible_by_65": divisible_by_65,
    }

    return {"result": results}
