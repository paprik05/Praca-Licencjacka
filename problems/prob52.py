import math

def prob52(m):
    arithmetic_progression = [math.factorial(m)*k+1 for k in range(1, m+1)]

    for i in range(len(arithmetic_progression)):
        for j in range(i+1, len(arithmetic_progression)):
            if math.gcd(arithmetic_progression[i], arithmetic_progression[j]) != 1:
                return False
    return {"result": f"{True}, arithmetic_progression: {arithmetic_progression}"}