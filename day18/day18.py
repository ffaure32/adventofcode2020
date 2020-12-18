import re

from utils import file_utils

range_regex = re.compile(r"(\d* \W \d*)(.*)")


def calculate_left_to_right(operation):
    end = False
    while not end:
        match = range_regex.match(operation)
        if not match:
            return int(operation)
        groups = match.groups()
        op = groups[0]
        result = calculate_2_operands(op)
        if groups[1]:
            operation = str(result) + groups[1]
        else:
            return result


simple_regex = re.compile(r"(\d*) (\W) (\d*)")


def calculate_2_operands(operation):
    match = simple_regex.match(operation)
    groups = match.groups()
    left = int(groups[0])
    right = int(groups[2])
    op = groups[1]
    if op == '+':
        return left + right
    else:
        return left * right


def calculate_inverse_precedence(operation):
    nb_plus = operation.count('+')
    for i in range(nb_plus):
        pluses = find_indexes(operation, '+')
        prods = find_indexes(operation, '*')
        operators = pluses + prods
        operators.sort()
        index_of_operation = operators.index(pluses[0])
        prev_op = 0
        next_op = len(operation) + 1
        if index_of_operation > 0:
            prev_op = operators[index_of_operation - 1] + 2
        if index_of_operation < len(operators) - 1:
            next_op = operators[index_of_operation + 1]
        result = calculate_2_operands(operation[prev_op:next_op - 1])
        operation = operation[:prev_op] + str(result) + operation[next_op - 1:]
    return calculate_left_to_right(operation)


def find_indexes(operation, operator):
    return [i for i, x in enumerate(operation) if x == operator]


def calculate_with_parenthesis(operation):
    return calculate_with_parenthesis_and_operator(operation, calculate_left_to_right)


def calculate_with_parenthesis_and_operator(operation, calculator):
    for i in range(operation.count(')')):
        first_closing = operation.index(')')
        left = operation[:first_closing]
        corresponding_open = left.rfind('(')
        to_calculate = left[corresponding_open + 1:]
        inside_result = calculator(to_calculate)
        operation = operation[:corresponding_open] + str(inside_result) + operation[first_closing + 1:]
    return operation


def solution(file_name):
    operations = file_utils.get_lines(file_name)
    return sum([calculate_left_to_right(calculate_with_parenthesis_and_operator(operation, calculate_left_to_right)) for
                operation in operations])


def solution2(file_name):
    operations = file_utils.get_lines(file_name)
    return sum(
        [calculate_inverse_precedence(calculate_with_parenthesis_and_operator(operation, calculate_inverse_precedence))
         for operation in
         operations])


def test_solution():
    result = solution('input')
    print(result)
    assert 12918250417632 == result


def test_solution2():
    result = solution2('input')
    print(result)
    assert 171259538712010 == result


def test_find_parenthesis():
    assert 51 == calculate_left_to_right(calculate_with_parenthesis('1 + (2 * 3) + (4 * (5 + 6))'))


def test_calculate_inverse():
    assert 231 == calculate_inverse_precedence('1 + 2 * 3 + 4 * 5 + 6')


def test_input():
    assert 13 == calculate_left_to_right(calculate_with_parenthesis('2 + (4 + 3) + 4'))
    assert 26 == calculate_left_to_right(calculate_with_parenthesis('2 * 3 + (4 * 5)'))
    assert 437 == calculate_left_to_right(calculate_with_parenthesis('5 + (8 * 3 + 9 + 3 * 4 * 3)'))
    assert 13632 == calculate_left_to_right(
        calculate_with_parenthesis('((2 + 4 * 9) * (6 + 9 * 8 + 6) + 6) + 2 + 4 * 2'))


def test_input2():
    assert 51 == calculate_inverse_precedence(
        calculate_with_parenthesis_and_operator('1 + (2 * 3) + (4 * (5 + 6))', calculate_inverse_precedence))
    assert 46 == calculate_inverse_precedence(
        calculate_with_parenthesis_and_operator('2 * 3 + (4 * 5)', calculate_inverse_precedence))
    assert 1445 == calculate_inverse_precedence(
        calculate_with_parenthesis_and_operator('5 + (8 * 3 + 9 + 3 * 4 * 3)', calculate_inverse_precedence))
    assert 669060 == calculate_inverse_precedence(
        calculate_with_parenthesis_and_operator('5 * 9 * (7 * 3 * 3 + 9 * 3 + (8 + 6 * 4))',
                                                calculate_inverse_precedence))
    assert 23340 == calculate_inverse_precedence(
        calculate_with_parenthesis_and_operator('((2 + 4 * 9) * (6 + 9 * 8 + 6) + 6) + 2 + 4 * 2',
                                                calculate_inverse_precedence))


def test_simple_add():
    assert 7 == calculate_left_to_right('4 + 3')


def test_simple_prod():
    assert 12 == calculate_left_to_right('4 * 3')


def test_3_add():
    result = calculate_left_to_right('4 + 3 + 10')
    print(result)
    assert 17 == result


def test_3_add_and_prod():
    result = calculate_left_to_right('4 + 3 * 10')
    print(result)
    assert 70 == result


def test_4_add_and_prod():
    result = calculate_left_to_right('1 + 2 * 3 + 4 * 5 + 6')
    print(result)
    assert 71 == result
