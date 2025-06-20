from math import gcd

def prob74(n):
    results = []
    for i in range(8,n+1,2):
        p = 3
        q = 5
        if gcd(i-p,i-q) == 1:
            results.append(f"{i}: {gcd(i-p,i-q) == 1}")

    return{"result": results}