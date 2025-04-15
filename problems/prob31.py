def prob31(a, b, c):
    def is_divisible_by_3(n):
        return n % 3 == 0

    def satisfies_theorem(a, b, c):
        sum_cubes = a**3 + b**3 + c**3
        divisible_by_9 = (sum_cubes % 9 == 0)

        if divisible_by_9:
            return is_divisible_by_3(a) or is_divisible_by_3(b) or is_divisible_by_3(c)
        return True

    result = satisfies_theorem(a, b, c)
    return {"result": result}
