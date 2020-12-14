import day14
from utils import math_utils


def test_bit_conversion():
    print(math_utils.decimal_to_36_bits(73))


def test_apply_mask():
    mask = 'XXXXXXXXXXXXXXXXXXXXXXXXXXXXX1XXXX0X'
    result = day14.apply_mask(mask, 11)
    assert 73 == result


def test_parse_mem():
    input = "mem[7] = 101"
    result = day14.parse_mem(input)
    assert result[0] == 7
    assert result[1] == 101


def test_parse_mem_error():
    input = "mask = XXXXXXXXXXXXXXXXXXXXXXXXXXXXX1XXXX0X"
    result = day14.parse_mem(input)
    assert not result


def test_solution():
    assert 165 == day14.solution("test_1")


def test_solution_real():
    assert 11501064782628 == day14.solution("input")


def test_calculate_masks():
    assert 4 == len(day14.calculate_masks("000000000000000000000000000000X1001X"))
    assert 8 == len(day14.calculate_masks("00000000000000000000000000000000X0XX"))


def test_solution2():
    assert 208 == day14.solution2("test_2")


def test_solution2_real():
    assert 5142195937660 == day14.solution2("input")
