from math import gcd


def unique(a,b,c):
    numbers = [a,b,c]
    if len(numbers) != len(set(numbers)):
        return {"error": "All numbers must be different"}
    return True


def prob45(a, b, c, n):
    try:
        if unique(a,b,c):
            if n <= 0:
                return {"error": "n must be a positive integer"}

            results = []
            k = 1
            while len(results) < n:
                nums = [a+k, b+k, c+k]
                if all(gcd(nums[i], nums[j]) == 1 for i in range(len(nums)) for j in range(i + 1, len(nums))):
                    results.append(f"n: {k}")
                k += 1
            return {"result": results}
    except ValueError as e:
        return {"error": e}
