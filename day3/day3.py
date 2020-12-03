import math
from functools import reduce

from utils import file_utils

TREE = '#'


def cell_at(line, x_pos):
    if x_pos >= len(line):
        return line[x_pos % len(line)]
    return line[x_pos]


def compute(lines):
    return compute2(lines, (3, 1))


def compute2(lines, step):
    x = 0
    y = 0
    count_trees = 0
    while y < len(lines)-1:
        x += step[0]
        y += step[1]
        if y < len(lines):
            cell = cell_at(lines[y], x)
            if cell == TREE:
                count_trees += 1
    return count_trees


def solution(file_name):
    return compute(prepare_data(file_name))


def solution2(file_name):
    steps = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]
    lines = prepare_data(file_name)
    computed_steps = [compute2(lines, step) for step in steps]
    product = reduce(lambda x, y: x * y, computed_steps)
    return product


def prepare_data(file_name):
    lines = file_utils.get_lines("inputs", file_name)
    lines = [line.rstrip('\r\n') for line in lines]
    return lines


if __name__ == "__main__":
    print(solution("input"))
    print(solution2("input"))
