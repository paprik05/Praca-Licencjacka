from math import gcd

def unique(a, b, c, d):
    numbers = [a, b, c, d]
    if len(numbers) != len(set(numbers)):
        raise ValueError("Wszystkie liczby muszą być inne")
    return True

def prob46(a, b, c, d, max_n):
    try:
        if unique(a, b, c, d):
            if max_n <= 0:
                return {"error": "n musi być liczbą całkowitą dodatnią"}

            results = []
            for n in range(1, max_n + 1):
                nums = [a + n, b + n, c + n, d + n]
                if all(gcd(nums[i], nums[j]) == 1 for i in range(len(nums)) for j in range(i + 1, len(nums))):
                    results.append(n)
            return {"result": results}
    except ValueError as e:
        return {"error": str(e)}