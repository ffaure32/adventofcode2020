from functools import reduce


def prod(num_list):
    return reduce(lambda x, y: x * y, num_list)


def pgcd(a, b):
    if b == 0:
        return a
    else:
        r = a % b
        return pgcd(b, r)


# https://fr.wikipedia.org/wiki/Algorithme_d%27Euclide_%C3%A9tendu
def euclid_extended_calc(a, b):
    return recursive_euclid_method(a, 1, 0, b, 0, 1)[1:]


def recursive_euclid_method(r, u, v, rp, up, vp):
    if rp == 0:
        return (r, u, v)
    q = (r // rp)
    return recursive_euclid_method(rp, up, vp, r - q * rp, u - q * up, v - q * vp)
