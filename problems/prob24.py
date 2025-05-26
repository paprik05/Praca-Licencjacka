def prob24(n):
    x = n + 1
    while True:
        x_pow = x ** x
        y = 2 * x
        try:
            y_pow = y ** y
        except OverflowError:
            x += 1
            continue
        if y_pow % x_pow == 0:
            return {"result":f"n = {n}, x = {x}, y = {y}, {x}^{x} | {y}^{y}"}

        x += 1