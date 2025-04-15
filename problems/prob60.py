import math

def power_of_integer(n):
    if n <= 1:
        return False

    for b in range(2, int(math.log2(n))):
        a = round(n** (1 / b))
        if pow(a, b, n) == 0:
            return True
    return False


def prob60(start, end):
    for i in range(start, end - 3):
        if power_of_integer(i) and power_of_integer(i+1) and power_of_integer(i+2) and power_of_integer(i+3):
            return {"result": False, "list of integers": [i, i+1, i+2, i+3]}
    return{"result": True}