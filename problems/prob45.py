from math import gcd


def unique(a,b,c):
    numbers = [a,b,c]
    if len(numbers) != len(set(numbers)):
        raise ValueError("Wszystkie liczby muszą być inne")
    return True


def prob45(a, b, c, n):
    try:
        if unique(a,b,c):
            if n <= 0:
                return {"error": "n musi być liczbą całkowitą dodatnią"}

            for n in range(1, n + 1):
                nums = [a+n, b+n, c+n]
                if all(gcd(nums[i], nums[j]) == 1 for i in range(len(nums)) for j in range(i + 1, len(nums))):
                    return {"result": n}
            return {"result": None}
    except ValueError as e:
        return {"error": e}
