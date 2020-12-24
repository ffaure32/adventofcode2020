import re

from utils import file_utils

rule_regex = re.compile(r'(\d*): (.*)')
letter_regex = re.compile(r'(\d*): "(\w)"')


def parse_line(line):
    match_letter = letter_regex.match(line)
    if match_letter:
        return LetterRule(int(match_letter.group(1)), match_letter.group(2))
    else:
        return parse_rule(line)


def parse_rule(line):
    match = rule_regex.match(line)
    rule = Rule(match.group(1))
    regex = match.group(2)
    left_and_right = regex.split('|')
    rule.left_indexes = convert_to_indexes(left_and_right[0])
    if len(left_and_right) > 1:
        rule.right_indexes = convert_to_indexes(left_and_right[1])
        rule.has_right = True
    return rule


def convert_to_indexes(rule):
    numbers = rule.split(' ')
    numbers = list(filter(lambda x: x != '', numbers))
    ints = [int(number) for number in numbers]
    return ints


def prepare_data(file_name, regex_generator):
    rules = dict()
    lines = file_utils.get_lines(file_name)
    to_validate_count = 0
    parse_regex = True
    for line in lines:
        if not line:
            parse_regex = False
            first_rule = rules[0]
            raw_regex = regex_generator(rules).replace(' ', '')
            raw_regex = '^'+raw_regex+'$'
            regex = re.compile(raw_regex)
        elif parse_regex:
            rule = parse_line(line)
            rules[rule.index] = rule
        else:
            matched = regex.match(line)
            if matched:
                to_validate_count += 1
    return to_validate_count


def first_rule_part1(rules):
    first_rule = rules[0]
    return first_rule.replace_children(rules)


def first_rule_part2(rules):
    rule_42 = rules[42].replace_children(rules)
    rule_31 = rules[31].replace_children(rules)
    rule_8 = "(?:"+rule_42+"+)"
    rule_11 = "(?:("+rule_42+rule_31+"|"+rule_42+"(?-1)"+rule_31+"))"
    raw_regex = "^(?:"+rule_8+rule_11+")$"
    print(raw_regex)
    return raw_regex



class Rule:
    def __init__(self, index) -> None:
        self.index = int(index)
        self.left_indexes = list()
        self.right_indexes = list()
        self.has_right = False

    def replace_children(self, rules):
        replaced = dict()
        for index in set(self.left_indexes + self.right_indexes):
            result = rules[index].replace_children(rules)
            replaced[index] = result
        regex = ''
        if self.has_right:
            regex += '('
        for index in self.left_indexes:
            regex += replaced[index] + ' '
        if self.has_right:
            regex += '|'
            for index in self.right_indexes:
                regex += ' ' + replaced[index]
            regex += ')'
        return regex


class LetterRule:
    def __init__(self, index, letter) -> None:
        self.index = int(index)
        self.letter = letter

    def replace_children(self, rules):
        return self.letter


def test_regex_groups():
    rule = '121: 23 | 57'
    rule = parse_line(rule)
    assert rule.left_indexes == [23]
    assert rule.right_indexes == [57]


def test_regex_groups_without_pipe():
    rule = '121: 23 57'
    rule = parse_line(rule)
    assert rule.left_indexes == [23, 57]
    assert not rule.has_right


def test_regex_groups_with_pipe_and_pairs():
    rule = '121: 23 57 | 15 21'
    rule = parse_line(rule)
    assert rule.left_indexes == [23, 57]
    assert rule.right_indexes == [15, 21]


def test_prepare_data():
    count = prepare_data('input', first_rule_part1)
    assert 107 == count


def test_prepare_data_part2():
    count = prepare_data('input', first_rule_part2)
    print(count)
    assert 12 == count
