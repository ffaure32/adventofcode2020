import numpy

from utils import file_utils

def compute(lines):
    for i in range(len(lines)):
        for j in range(i, len(lines)):
            tuple = (to_int(lines[i]), to_int(lines[j]))
            if check_2020(tuple):
                return multiply(tuple)
    return 0


def compute2(lines):
    for i in range(len(lines)):
        for j in range(i, len(lines)):
            for k in range(j, len(lines)):
                tuple =(to_int(lines[i]), to_int(lines[j]), to_int(lines[k]))
                if check_2020(tuple):
                    return multiply(tuple)
    return 0

def check_2020(numbers):
    return sum(numbers) == 2020

def multiply(numbers):
    return numpy.prod(numbers)

def to_int(int_string):
    return int(int_string.rstrip('\r\n'))

def solution(path_name, file_name):
    return compute(file_utils.get_lines(path_name, file_name))


def solution2(path_name, file_name):
    return compute2(file_utils.get_lines(path_name, file_name))


if __name__ == "__main__":
    print(solution("inputs", "input"))
    print(solution2("inputs", "input"))
