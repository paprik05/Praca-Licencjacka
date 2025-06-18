from math import gcd

fib_cache = {1: 1, 2: 1}


def fibonacci(n):
    if n in fib_cache:
        return fib_cache[n]
    fib_cache[n] = fibonacci(n - 1) + fibonacci(n - 2)
    return fib_cache[n]


def generate_fib_sequence(n):
    return [fibonacci(i) for i in range(1, n + 1)]


def find_3_term_aps(fibs):
    triplets = []
    length = len(fibs)
    for i in range(length):
        for j in range(i + 1, length):
            a, b = fibs[i], fibs[j]
            c = 2 * b - a
            if c in fibs:
                k = fibs.index(c)
                if j < k:
                    triplets.append((a, b, c))
    return triplets


def check_4_term_aps(fibs):
    length = len(fibs)
    for i in range(length):
        for j in range(i + 1, length):
            diff = fibs[j] - fibs[i]
            third = fibs[j] + diff
            fourth = fibs[j] + 2 * diff
            if third in fibs and fourth in fibs:
                j_index = j
                third_index = fibs.index(third)
                fourth_index = fibs.index(fourth)
                if j_index < third_index < fourth_index:
                    return (fibs[i], fibs[j], third, fourth)
    return None


def prob64(n=100):
    fibs = generate_fib_sequence(n)
    result_output = ["3-term arithmetic progressions:"]

    aps_3 = find_3_term_aps(fibs)
    for triplet in aps_3:
        result_output.append(str(triplet))

    aps_4 = check_4_term_aps(fibs)
    if aps_4:
        result_output.append("4-term arithmetic progression found:")
        result_output.append(str(aps_4))
    else:
        result_output.append("No 4-term arithmetic progression found.")

    return {"result": result_output}