def prob36(s):
    if s <= 0:
        return {"error": "s musi być liczbą całkowitą dodatnią"}

    def sum_of_digits(num):
        return sum(int(digit) for digit in str(num))

    i = s
    while True:
        if sum_of_digits(i) == s and i % s == 0:
            return {"result":f"{s}: {i}"}
        i += 1
