from math import gcd


def prob49(m, e):
    if m <= 0 :
        return {"error": "n must be a positive integer"}
    if e % 2 != 0:
        return {"error": "n must be an even number"}

    for i in range(2, e + 1):
        j = e - i
        if i > 1 and j > 1 and gcd(i, m) == 1 and gcd(j, m) == 1:
            return {"result": f"m: {m}, 2k: {e}, difference: {i} - {j}"}
    return {"result": None}
