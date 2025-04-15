def prob28():
    def is_composite(num):
        if num < 4:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return True
        return False

    def satisfies_conditions(n):
        return (pow(2, n, n) == 2) and (pow(3, n, n) != 3)

    n = 4
    while True:
        if is_composite(n) and satisfies_conditions(n):
            return {"result": n}
        n += 1