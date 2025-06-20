
def prob1(r, max_time=5):
    if r <= 0:
        return {"error": "r must be a positive integer"}

    results = []

    for n in range(1, r + 1):

        if (n**2 + 1) % (n + 1) == 0:
            results.append(n)

    return {"result": results}
