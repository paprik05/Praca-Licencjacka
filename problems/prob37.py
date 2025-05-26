from itertools import product
def prob37(s):

    for length in range(1, s * 2):
        for digits in product(range(10), repeat=length):
            if digits[0] == 0:
                continue
            if sum(digits) == s:
                n = int(''.join(map(str, digits)))
                if n % s == 0:
                    return {"result": f"s = {s}, n = {n}, sum of n digits = {s}"}