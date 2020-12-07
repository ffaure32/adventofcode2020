import re
from utils import file_utils

ROOT_COLOR = "shiny gold"
PARSE_COLOR_REGEX = "\s(\d)\s(.*) bag"


def parse_rule(rule_string):
    result = []
    split = rule_string.split("contain")

    container = split[0][:-6]
    contained_split = split[1].split(',')
    for contained_bag in contained_split:
        colors = re.findall(PARSE_COLOR_REGEX, contained_bag)
        for color in colors:
            count = int(color[0])
            contained = color[1]
            result.append(Rule(container, contained, count))
    return result


def prepare_data(file_name):
    lines = file_utils.get_lines("inputs", file_name)
    rules = set()
    for line in lines:
        rules.update(parse_rule(line))
    return rules


def find_parents(prepared_data, color):
    return set(filter(lambda rule: rule.contained == color, prepared_data))


def solution(file_name):
    prepared_data = prepare_data(file_name)
    parents = find_parents(prepared_data, ROOT_COLOR)
    new_parents = parents
    while len(new_parents) > 0:
        next_new_parents = set()
        for parent in new_parents:
            next_new_parents.update(find_parents(prepared_data, parent.container))
        parents.update(next_new_parents)
        new_parents = next_new_parents
    unique_parents = set([parent.container for parent in parents])
    return len(unique_parents)


def count_direct_children(prepared_data, parent):
    children = find_direct_children(prepared_data, parent)
    total = 1
    for child in children:
        total += count_direct_children(prepared_data, child.contained) * child.count
    return total


def find_direct_children(prepared_data, color):
    return set(filter(lambda rule: rule.container == color, prepared_data))


def solution2(file_name):
    prepared_data = prepare_data(file_name)
    total = count_direct_children(prepared_data, ROOT_COLOR)
    return total - 1


class Rule:
    def __init__(self, container, contained, count):
        self.container = container
        self.contained = contained
        self.count = count
