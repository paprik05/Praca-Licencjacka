def prob31(a, b, c):
    def is_divisible_by_3(n):
        return n % 3 == 0

    def satisfies_theorem(a, b, c):
        sum_cubes = a**3 + b**3 + c**3
        divisible_by_9 = (sum_cubes % 9 == 0)

        divisible_numbers = []
        if is_divisible_by_3(a):
            divisible_numbers.append('a')
        if is_divisible_by_3(b):
            divisible_numbers.append('b')
        if is_divisible_by_3(c):
            divisible_numbers.append('c')

        if divisible_by_9:
            result = len(divisible_numbers) > 0
            return result, divisible_numbers
        return True, []

    result, divisible_by = satisfies_theorem(a, b, c)
    return {"result": f"{result}, {divisible_by} is divisible by 3"}
