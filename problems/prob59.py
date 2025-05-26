def is_perfect_power(n):
    for b in range(2, int(n**0.5) + 2):
        a = round(n ** (1 / b))
        if a ** b == n:
            return True
    return False

def prob59(max_start=1000, max_diff=1000, max_length=10):
    for start in range(1, max_start):
        for diff in range(1, max_diff):
            count = 0
            for i in range(max_length):
                term = start + i * diff
                if is_perfect_power(term):
                    count += 1
                else:
                    break
            if count == max_length:
                return {"result": f"start = {start}, diff = {diff}, progression = {[start + i * diff for i in range(max_length)]}"}

    return {"result": f"No arithmetic progression of {max_length} perfect powers found with start < {max_start} and diff < {max_diff}"}