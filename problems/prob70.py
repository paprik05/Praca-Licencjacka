def prob70():
    from sympy import isprime

    p = 3
    progression = [p + 10 * i for i in range(3)]
    if all(isprime(x) for x in progression):
        fourth = p + 30
        if isprime(fourth):
            {"result": False}
        else:
            return {"result": progression}
    return {"result": False}