from sympy import isprime
def prob116(limit=10):
    k_list = [6*t-1 for t in range(1, limit+1)]
    for k in k_list:
        composite = True
        for n in range(1, limit+1):
            result = pow(2,pow(2,n)) + k
            if isprime(result):
                composite = False
                break


    return {"result:": composite}