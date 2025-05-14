def prob38a(n):
    counter1 = 0
    counter2 = 0

    for d in range(1, n + 1):
        if n % d == 0:
            if d % 4 == 1:
                counter1 += 1
            elif d % 4 == 3:
                counter2 += 1

    return {"result": f"{n}: {counter1 >= counter2}, 4k+1 dividors count: {counter1}, 4k+3 dividors count: {counter2}"}
