from functools import reduce


def prod(num_list):
    return reduce(lambda x, y: x * y, num_list)
