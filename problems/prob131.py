from sympy import isprime
def prob131(limit):
    result = 0
    highest_counter = 0

    for k in range(1, limit+1):
        counter = 0

        counter += sum(isprime(k + i) for i in range(1, 11))

        if counter > highest_counter:
            highest_counter = counter
            result = k

    return {"result": f"k = {result}"}