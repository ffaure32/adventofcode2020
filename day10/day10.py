from utils import file_utils
from utils import math_utils


def prepare_data(file_name):
    lines = file_utils.get_lines(file_name)
    lines = [int(line) for line in lines]
    lines.sort()
    lines.insert(0, 0)
    lines.append(lines[-1] + 3)
    return lines


def solution(file_name):
    prepared_data = prepare_data(file_name)
    gaps = find_gaps(prepared_data)
    return gaps.count(1) * gaps.count(3)


def solution2(file_name):
    prepared_data = prepare_data(file_name)
    gaps = find_gaps(prepared_data)
    consecutive = 0
    multiples = []
    for gap in gaps:
        if gap == 1:
            consecutive += 1
        else:
            if consecutive == 2:
                multiples.append(2)
            elif consecutive == 3:
                multiples.append(4)
            elif consecutive == 4:
                multiples.append(7)
            consecutive = 0
    return math_utils.prod(multiples)


def find_gaps(prepared_data):
    gaps = []
    for i in range(1, len(prepared_data)):
        gaps.append(prepared_data[i] - prepared_data[i - 1])
    return gaps
