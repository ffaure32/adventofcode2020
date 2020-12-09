from utils import file_utils


def is_valid(array, to_test):
    for i in range(len(array)):
        for j in range(i + 1, len(array)):
            sum_ints = array[i] + array[j]
            if sum_ints == to_test:
                return True
    return False


def find_first_weakness(input_data, preamble_size):
    for i in range(len(input_data) - preamble_size):
        start = i
        end = i+preamble_size
        preamble = input_data[start:end]
        to_test = input_data[end]
        if not is_valid(preamble, to_test):
            return to_test


def prepare_data(file_name):
    lines = file_utils.get_lines("inputs", file_name)
    int_lines = [int(line) for line in lines]
    return int_lines


def solution(file_name, preamble_size):
    prepared_data = prepare_data(file_name)
    return find_first_weakness(prepared_data, preamble_size)


def solution2(file_name):
    prepared_data = prepare_data(file_name)
    return len(prepared_data)
