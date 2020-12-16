from functools import reduce
from utils import file_utils

ANSWERS_SEPARATOR = '*'
ANSWERS_INFO_SEPARATOR = ' '
JOINED_ANSWERS_SEPARATOR = " %s " % ANSWERS_SEPARATOR


def prepare_data(file_name):
    lines = file_utils.get_lines(file_name)
    lines = [line if line else ANSWERS_SEPARATOR for line in lines]
    joined = ANSWERS_INFO_SEPARATOR.join(lines)
    lines = joined.split(JOINED_ANSWERS_SEPARATOR)
    return lines


def solution(file_name):
    answers = prepare_data(file_name)
    lines = [''.join(line.split(ANSWERS_INFO_SEPARATOR)) for line in answers]
    lines = [len(set(line)) for line in lines]
    return sum(lines)


def solution2(file_name):
    answers = prepare_data(file_name)
    lines = [split_line(line) for line in answers]
    lines = [sets_intersection(line) for line in lines]
    return sum(lines)


def split_line(line):
    return [set(line_splitted) for line_splitted in line.split(ANSWERS_INFO_SEPARATOR)]


def sets_intersection(set_list):
    return len(reduce(lambda x, y: set(x.intersection(y)), set_list))
