from sympy import primefactors

def prob88(i):
    proved = True
    pf_i = primefactors(i)
    pf_i1 = primefactors(i + 1)
    pf_i2 = primefactors(i + 2)
    if not (len(primefactors(i)) >= 2 or len(primefactors(i+1)) >= 2 or len(primefactors(i+2)) >= 2):
        proved = False
    return {"result": f"{proved}, prime divisors of {i}: {pf_i}, prime divisors of {i+1}: {pf_i1}, prime divisors of {i+2}: {pf_i2}"}