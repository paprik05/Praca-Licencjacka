def prob53(k, length=5, max_search=100000):
    matches = []

    for n in range(1, max_search):
        div_count = 0
        for i in range(1, int(n**0.5) + 1):
            if n % i == 0:
                div_count += 2 if i != n // i else 1

        if div_count % k == 0:
            matches.append(n)
            if len(matches) >= length:
                diffs = [matches[i+1] - matches[i] for i in range(-length, -1)]
                if all(d == diffs[0] for d in diffs):
                    return {"result": f"k = {k}, progression: {matches[-length:]}, common difference = {diffs[0]}"}

    return {"error": f"Failed to find such a progression within {max_search} numbers."}