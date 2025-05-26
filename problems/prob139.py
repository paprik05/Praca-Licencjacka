def prob139(limit):
    results = []
    x, y = 2, 3

    for _ in range(limit):
        results.append(f"x = {x}, y = {y}, ")
        x, y = 2 * y + 3 * x, 3 * y + 4 * x

    return {"result": results}
