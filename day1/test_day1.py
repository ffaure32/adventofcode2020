import os

import day1


def test_check_2020_false():
    result = day1.check_2020((0, 0))
    assert result == False

def test_check_2020_true():
    result = day1.check_2020((1000, 1020))
    assert result == True

def test_convert_line():
    result = day1.to_int("12\n")
    assert result == 12

def test_compute():
    lines = ["1010"]
    result = day1.compute(lines)
    assert result == 1010*1010

def test_day1():
    print(os.getcwd())
    result = day1.solution("test_1")
    assert result == 514579

def test_day1_real():
    result = day1.solution("input")
    assert result == 270144

def test_day1_part2():
    result = day1.solution2("test_1")
    assert result == 241861950

def test_day1_real_part2():
    result = day1.solution2("input")
    assert result == 261342720