def prob55(limit):
    triangles = []
    r = 1
    while 5 * r <= limit:
        triangles.append((3 * r, 4 * r, 5 * r))
        r += 1
    return {"result": triangles}