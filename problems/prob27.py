def prob27():
    def is_composite(num):
        if num < 4:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return True
        return False

    def satisfies_conditions(n):
        return (pow(2, n, n) == 2) and (pow(3, n, n) == 3)

    found = []
    n = 4
    while len(found) < 2:
        if is_composite(n) and satisfies_conditions(n):
            found.append(f"{n}: n|2^n-2 = {n}|{2**n-2} and n|3^n-3 = {n}|{3**n-3}")
        n += 1

    return {"result": found}
