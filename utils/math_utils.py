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


def decimal_to_36_bits(num):
    arr = []
    decimal_to_binary(arr, num)
    pad_left(36, arr)
    return arr


def pad_left(length, arr):
    to_pad = len(arr)
    for i in range(length - to_pad):
        arr.insert(0, 0)


def decimal_to_binary(arr, num):
    if num > 1:
        decimal_to_binary(arr, num // 2)
    arr.append(num % 2)


def bits_to_decimal(bit_array):
    to_str = [str(bit_value) for bit_value in bit_array]
    return int(''.join(to_str),2)