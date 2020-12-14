from utils import math_utils, file_utils
import re


def apply_mask(mask, value):
    return apply_mask_real(mask, value, change_output_v1)


def apply_mask_v2(mask, value):
    return apply_mask_real(mask, value, change_output_v2)


def apply_mask_real(mask, value, change_output_function):
    bin_value = math_utils.decimal_to_36_bits(value)
    output = [0 for i in range(36)]
    for i in range(36):
        change_output_function(bin_value, i, mask, output)
    return math_utils.bits_to_decimal(output)


def change_output_v1(bin_value, i, mask, output):
    if mask[i] == 'X':
        output[i] = bin_value[i]
    else:
        output[i] = int(mask[i])


def change_output_v2(bin_value, i, mask, output):
    if mask[i] == '1':
        output[i] = 1
    elif mask[i] == 'Z':
        output[i] = 0
    else:
        output[i] = bin_value[i]


def prepare_data(file_name):
    lines = file_utils.get_lines("inputs", file_name)
    return lines


def solution(file_name):
    memories = dict()
    lines = prepare_data(file_name)
    mask = None
    for line in lines:
        if line.startswith('mask'):
            splitted = line.split((" = "))
            mask = splitted[1]
        else:
            parsed_mem = parse_mem(line)
            memories[parsed_mem[0]] = apply_mask(mask, parsed_mem[1])
    return sum(memories.values())


def solution2(file_name):
    memories = dict()
    lines = prepare_data(file_name)
    masks = None
    for line in lines:
        if line.startswith('mask'):
            splitted = line.split((" = "))
            masks = calculate_masks(splitted[1])
        else:
            parsed_mem = parse_mem(line)
            for mask in masks:
                memories[apply_mask_v2(mask, parsed_mem[0])] = parsed_mem[1]
    return sum(memories.values())


mem_regex = re.compile(r"mem\[(\d*)\] = (\d*)")


def parse_mem(input):
    match = mem_regex.match(input)
    if match:
        return (int(match.group(1)), int(match.group(2)))


def calculate_masks(input_mask):
    masks = [input_mask]
    x_indexes = [pos for pos, char in enumerate(input_mask) if char == 'X']
    for index in x_indexes:
        new_masks = []
        for mask in masks:
            new_masks.append(replace_char_at_index(mask, index, 'Z'))
            new_masks.append(replace_char_at_index(mask, index, '1'))
            masks = new_masks
    return masks


def replace_char_at_index(org_str, index, replacement):
    new_str = org_str
    if index < len(org_str):
        new_str = org_str[0:index] + replacement + org_str[index + 1:]
    return new_str
