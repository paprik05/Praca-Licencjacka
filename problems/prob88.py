from sympy import primefactors

def prob88(i):
    proved = True
    if not (len(primefactors(i)) >= 2 or len(primefactors(i+1)) >= 2 or len(primefactors(i+2)) >= 2):
        proved = False
    return {"result:": proved, "How much prime divisors for each integer:": (len(primefactors(i)) ,len(primefactors(i+1)) ,len(primefactors(i+2)))}