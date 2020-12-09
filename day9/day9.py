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
    return [int(line) for line in lines]


def solution(file_name, preamble_size):
    prepared_data = prepare_data(file_name)
    return find_first_weakness(prepared_data, preamble_size)


def solution2(file_name, sum_to_find):
    prepared_data = prepare_data(file_name)
    index = prepared_data.index(sum_to_find)
    removed_tail = prepared_data[:index]
    contiguous_range = find_contiguous_range(removed_tail, sum_to_find)
    return min(contiguous_range)+max(contiguous_range)


def find_contiguous_range(numbers_before_sum_to_find, sum_to_find):
    for i in range(len(numbers_before_sum_to_find), 0, -1):
        current_sum = 0
        j = i-1
        while current_sum < sum_to_find:
            current_sum += numbers_before_sum_to_find[j]
            j -= 1

        if current_sum == sum_to_find:
            contiguous_range = numbers_before_sum_to_find[j + 1:i]
            return contiguous_range
