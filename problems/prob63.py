def starts_with(number, prefix):
    return str(number).startswith(str(prefix))

def prob63(a, b, prefix):
    s = len(str(prefix))

    n = 1
    while 10 ** n <= 2 * a:
        n += 1

    from math import ceil

    left_expr = prefix * (10 ** n) / a - b / a
    k = ceil(left_expr)
    term = a * k + b

    return {
        "result": f"k = {k}, term = {term}, prefix = {prefix}, starts_with_prefix = {starts_with(term, prefix)}"
    }