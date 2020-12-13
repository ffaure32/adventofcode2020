from functools import reduce


def prod(num_list):
    return reduce(lambda x, y: x * y, num_list)


def pgcd(a, b):
    if b == 0:
        return a
    else:
        r = a % b
        return pgcd(b, r)


def gcdExtended(a, b):
    # Base Case
    if a == 0:
        return b, 0, 1

    gcd, x1, y1 = gcdExtended(b % a, a)

    # Update x and y using results of recursive
    # call
    x = y1 - (b // a) * x1
    y = x1

    return gcd, x, y


def eucl(r, u, v, rp, up, vp):
    if rp == 0:
        return (r, u, v)
    return eucl(rp, up, vp, r-(r//rp)*rp, u-(r//rp)*up, v-(r//rp)*vp)

def euclid(a,b):
    return eucl(a, 1, 0, b, 0, 1)[1:]