def prob38c(n):
    counter1 = 0
    counter2 = 0
    results = []
    i = 1

    while len(results) < n:
        for d in range(1, i + 1):
            if i % d == 0:
                if d % 4 == 1:
                    counter1 += 1
                elif d % 4 == 3:
                    counter2 += 1
        if counter1 > counter2:
            results.append(f"{i}: 4k+1 dividors count: {counter1}, 4k+3 dividors count: {counter2}")
        counter1 = 0
        counter2 = 0
        i += 1

    return {"result": results}