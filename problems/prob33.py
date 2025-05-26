from math import gcd

def prob33(x, y, z):

    left_side = x ** 2 + y ** 2
    right_side = z ** 4

    if left_side != right_side:
        return {"result": f"Condition x^2 + y^2 = z^4 not satisfied"}

    d = gcd(x, y)
    coprime = d == 1

    if (x * y) % 7 == 0:
        return {
            "result": f"x = {x}, y = {y}, z = {z}, {True}, " +
                      ("necessary condition satisfied" if coprime else "necessary condition NOT satisfied")
        }
    else:
        return {"result": f"7 does NOT divide xy = {x * y}"}


