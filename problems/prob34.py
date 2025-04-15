def prob34():
    for a in range(7):
        for b in range(7):
            if (a**2 + b**2) % 7 == 0:
                if a % 7 != 0 or b % 7 != 0:
                    return {"result": False}
    return {"result": True}
