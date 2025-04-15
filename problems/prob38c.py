def prob38c(n):
    counter1 = 0
    counter2 = 0

    results = []

    for i in range(1, n+1):
        for d in range(1, i + 1):
            if i % d == 0:
                if d % 4 == 1:
                    counter1 += 1
                elif d % 4 == 3:
                    counter2 += 1
        if counter1 > counter2:
            results.append(i)
        counter1 = 0
        counter2 = 0

    return{"result": results}