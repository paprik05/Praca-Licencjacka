def prob32(r):
    for a1 in range(r + 1):
        for a2 in range(r + 1):
            for a3 in range(r + 1):
                for a4 in range(r + 1):
                    for a5 in range(r + 1):
                        sum_of_cubes = (a1**3 + a2**3 + a3**3 + a4**3 + a5**3) % 9
                        if sum_of_cubes == 0:
                            product = (a1 * a2 * a3 * a4 * a5) % 3
                            if product != 0:
                                return {"result": False}
    return {"result": True}
