import numpy
from utils import file_utils


def compute(lines):
    return real_compute(lines, lambda line: line.is_valid())


def compute2(lines):
    return real_compute(lines, lambda line: line.is_new_valid())


def real_compute(lines, filter_function):
    valid_lines = len([line for line in lines if filter_function(line)])
    return valid_lines


def to_int(int_string):
    return int(int_string.rstrip('\r\n'))


def solution(file_name):
    return compute(prepare_data(file_name))


def solution2(file_name):
    return compute2(prepare_data(file_name))


def prepare_data(file_name):
    lines = file_utils.get_lines("inputs", file_name)
    lines = [PasswordInfo(line) for line in lines]
    return lines


class PasswordInfo:

    def __init__(self, line):
        parts = line.split()
        counts = parts[0].split('-')
        self.min_count = int(counts[0])
        self.max_count = int(counts[1])
        self.letter = parts[1][0]
        self.password = parts[2]
        self.occurrences = self.password.count(self.letter)

    def is_valid(self):
        return self.min_count <= self.occurrences <= self.max_count

    def is_new_valid(self):
        letters = [self.password[self.min_count - 1], self.password[self.max_count - 1]]
        return len([letter for letter in letters if letter == self.letter]) == 1


if __name__ == "__main__":
    print(solution("input"))
    print(solution2("input"))
