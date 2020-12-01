import numpy
from utils import file_utils


def compute(linesStr):
    lines = [to_int(line) for line in linesStr]
    for i in range(len(lines)):
        for j in range(i, len(lines)):
            tuple = (lines[i], lines[j])
            if check_2020(tuple):
                return multiply(tuple)
    return 0


def compute2(linesStr):
    lines = [to_int(line) for line in linesStr]
    for i in range(len(lines)):
        for j in range(i, len(lines)):
            for k in range(j, len(lines)):
                tuple = (lines[i], lines[j], lines[k])
                if check_2020(tuple):
                    return multiply(tuple)
    return 0


def check_2020(numbers):
    return sum(numbers) == 2020


def multiply(numbers):
    return numpy.prod(numbers)


def to_int(int_string):
    return int(int_string.rstrip('\r\n'))


def solution(file_name):
    return compute(file_utils.get_lines("inputs", file_name))


def solution2(file_name):
    return compute2(file_utils.get_lines("inputs", file_name))


if __name__ == "__main__":
    print(solution("input"))
    print(solution2("input"))
