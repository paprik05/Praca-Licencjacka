def prob34(a, b):
    if (a**2 + b**2) % 7 == 0:
        if a % 7 == 0 and b % 7 == 0:
            return {"result": True}
    return {"result": False}
