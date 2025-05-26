from sympy import isprime

def prob77(n):
    results = []
    p = 5
    while len(results) < n:
        if p % 4 == 1 and isprime(p):
            found = False
            for a in range(1, int(p**0.5) + 1):
                b_squared = p - a*a
                b = int(b_squared**0.5)
                if b*b == b_squared:
                    x = abs(a*a - b*b)
                    y = 2*a*b
                    results.append(f"{x}^2 + {y}^2 = {p}^2")
                    found = True
                    break
            if not found:
                results.append(f"No representation found for {p}")
        p += 2
        return {"result": results}
