import math
def prob8(m, a):
    if m <= 0 or a <= 1:
        return {"error": "m must be a positive integer and a must be greater than 1."}

    numerator = a ** m - 1
    denominator = a - 1
    value = numerator // denominator

    left_gcd = math.gcd(value, a - 1)
    right_gcd = math.gcd(a - 1, m)

    return {"result": f"GCD(({a}^{m} - 1)/({a} - 1), {a} - 1) =  {left_gcd}, GCD({a} - 1, {m}) = {right_gcd}, {left_gcd == right_gcd}"}