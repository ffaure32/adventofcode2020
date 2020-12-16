import os

import day2
from day2 import PasswordInfo


def test_parse_password_info():
    pi = PasswordInfo("1-3 b: cdefg")
    assert pi.min_count == 1
    assert pi.max_count == 3
    assert pi.letter == 'b'
    assert pi.password == "cdefg"
    assert pi.occurrences == 0


def test_parse_valid_password_info():
    pi = PasswordInfo("2-9 c: ccccccc")
    assert pi.min_count == 2
    assert pi.max_count == 9
    assert pi.letter == 'c'
    assert pi.password == "ccccccc"
    assert pi.occurrences == 7


def test_validate_password_info():
    assert PasswordInfo("2-9 c: ccccccc").is_valid()
    assert not PasswordInfo("1-3 b: cdefg").is_valid()


def test_day2():
    result = day2.solution("test_1")
    assert result == 2


def test_day2_real():
    result = day2.solution("inputs")
    assert result == 607


def test_new_validate_password_info():
    assert PasswordInfo("1-3 a: abcde").is_new_valid()
    assert not PasswordInfo("1-3 b: cdefg").is_new_valid()
    assert not PasswordInfo("2-9 c: ccccccccc").is_new_valid()


def test_day2_part2():
    result = day2.solution2("test_1")
    assert result == 1


def test_day2_real_part2():
    result = day2.solution2("inputs")
    assert result == 321
