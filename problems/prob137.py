def prob137(limit):
    results = []

    x, y = 3, 2

    for _ in range(limit):
        results.append(f"x = {x}, y = {y}, ")

        x, y = 55 * x + 84 * y, 36 * x + 55 * y

    return {"result": results}
