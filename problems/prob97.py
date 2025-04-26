from sympy import isprime
def prob97(limit=100,num_of_results=1):
    counter = 0
    results = []

    for n in range(1,limit+1):
        formula = pow(n,4)+pow((n+1),4)
        if not isprime(formula):
            results.append(n)
            counter +=1
        if counter >= num_of_results:
            break

    return {"result": results}