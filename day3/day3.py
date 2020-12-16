from utils import file_utils, math_utils

TREE = '#'


def cell_at(line, x_pos):
    if x_pos >= len(line):
        return line[x_pos % len(line)]
    return line[x_pos]


def count_trees_on_slope(map_lines, slope):
    x = 0
    y = 0
    count_trees = 0
    while y < len(map_lines)-slope[1]:
        x += slope[0]
        y += slope[1]
        cell = cell_at(map_lines[y], x)
        if cell == TREE:
            count_trees += 1
    return count_trees


def solution(file_name):
    slope = (3, 1)
    map_lines = prepare_data(file_name)
    return count_trees_on_slope(map_lines, slope)


def solution2(file_name):
    slopes = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]
    map_lines = prepare_data(file_name)
    trees_on_slope = [count_trees_on_slope(map_lines, slope) for slope in slopes]
    return math_utils.prod(trees_on_slope)


def prepare_data(file_name):
    lines = file_utils.get_lines(file_name)
    return lines


if __name__ == "__main__":
    print(solution("input"))
    print(solution2("input"))
