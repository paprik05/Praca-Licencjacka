def prob54(n):
    triplets = []
    for y in range(1, n):
        x = y - (y + 1) // 2
        z = y + (y + 1) // 2
        if x > 0 and z > 0:
            triplets.append((x, y, z))
    return {"result": triplets}