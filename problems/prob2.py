def prob2(min_val, max_val):
    results = []
    for x in range(min_val, max_val):
        if x == 3:
            continue
        elif (x**3 - 3) % (x - 3) == 0:
            results.append(x)
    return {"result": results}
