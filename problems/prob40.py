def prob40(n):
    F = pow(2, pow(2,n)) + 1
    return {"result": pow(2, F, F) == 2}
