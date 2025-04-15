from math import gcd


def prob41(k):
    gcd_2k1_9k4 = gcd(2 * k + 1, 9 * k + 4)
    relatively_prime = gcd_2k1_9k4 == 1

    results = {
        "relatively_prime_2k1_9k4": relatively_prime,
        "gcd_2k1_9k4": gcd_2k1_9k4
    }

    return {"result": results}
