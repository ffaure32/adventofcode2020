import re
from utils import file_utils, math_utils


def prepare_data(file_name):
    fields = list()
    your_ticket = None
    other_tickets = list()
    lines = file_utils.get_lines(file_name)
    preparing_fields = True
    parsing_ticket = False
    for line in lines:
        if not line:
            if parsing_ticket:
                parsing_ticket = False
            if preparing_fields:
                preparing_fields = False
                parsing_ticket = True
        else:
            if preparing_fields:
                fields.append(FieldRange(line))
            elif parsing_ticket:
                if line != 'your ticket:':
                    your_ticket = Ticket(line)
            else:
                if line != 'nearby tickets:':
                    other_tickets.append(Ticket(line))

    return Input(fields, your_ticket, other_tickets)


def solution(input):
    parsed = prepare_data(input)
    return sum(parsed.scan_errors())


def valid_value(field, values):
    for value in values:
        if not field.value_in_ranges(value):
            return False
    return True


def find_valid_values_for_field(field, values_per_index):
    valid_indexes = list()
    for i in range(len(values_per_index)):
        if valid_value(field, values_per_index[i]):
            valid_indexes.append(i)
    return valid_indexes


def solution2(input):
    parsed = prepare_data(input)
    valid_tickets = parsed.remove_errors()
    num_values = len(parsed.fields)
    values_per_index = group_ticket_values_by_index(num_values, valid_tickets)

    valid_index_by_field = get_valid_index_by_field(parsed, values_per_index)
    return math_utils.prod([parsed.your_ticket.values[i] for i in dict(filter(lambda field: field[1].startswith('departure'), valid_index_by_field.items())).keys()])


def group_ticket_values_by_index(num_values, valid_tickets):
    values_per_index = [list() for i in range(num_values)]
    for valid_ticket in valid_tickets:
        for i in range(num_values):
            values_per_index[i].append(valid_ticket.values[i])
    return values_per_index


def get_valid_index_by_field(parsed, values_per_index):
    fields = parsed.fields
    valid_index_by_field = dict()
    while len(fields) > 0:
        for i in range(len(parsed.fields)):
            valid_indexes = find_valid_values_for_field(fields[i], values_per_index)
            if len(valid_indexes) == 1:
                found_index = valid_indexes[0]
                valid_index_by_field[found_index] = fields[i].name
                del fields[i]
                values_per_index[found_index] = [-1]
                break
    return valid_index_by_field


# departure location: 36-269 or 275-973
range_regex = re.compile(r"(.*): (\d*)-(\d*) or (\d*)-(\d*)")


class Input:
    def __init__(self, fields, your_ticket, other_tickets) -> None:
        self.fields = fields
        self.your_ticket = your_ticket
        self.other_tickets = other_tickets

    def scan_errors(self):
        errors = list()
        for ticket in self.other_tickets:
            for value in ticket.values:
                if not self.find_value(value):
                    errors.append(value)
        return errors

    def remove_errors(self):
        return list(filter(lambda ticket: self.is_valid(ticket), self.other_tickets))

    def is_valid(self, ticket):
        for value in ticket.values:
            if not self.find_value(value):
                return False
        return True

    def find_value(self, value):
        for field in self.fields:
            if field.value_in_ranges(value):
                return True
        return False


class Ticket:
    def __init__(self, input) -> None:
        split = input.split(',')
        self.values = [int(num) for num in split]


class FieldRange:
    def __init__(self, input) -> None:
        match = range_regex.match(input)

        self.name = match.group(1)
        self.first_range = (int(match.group(2)), int(match.group(3)))
        self.second_range = (int(match.group(4)), int(match.group(5)))

    def value_in_ranges(self, value):
        return self.first_range[0] <= value <= self.first_range[1] or self.second_range[0] <= value <= \
               self.second_range[1]
