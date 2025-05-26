def prob54(n):
    triplets = []
    for x in range(1, n + 1):
        y = 5 * x + 2
        z = 7 * x + 3
        triplets.append(f"x = {x}, y = {y}, z = {z}, arithmetic progession: ({x**2+x}, {y*(y+1)}, {z*(z+1)})")
    return {"result": triplets}
