import day13
from utils import math_utils


def test_print():
    assert 295 == day13.solution('test_1')


def test_print_real():
    assert 4938 == day13.solution('input')

def test_sol2():
    assert 1068781 == day13.solution2('test_1')

def test_sol2_real():
    assert 230903629977901 == day13.solution2('input')


def test_euclid():
    assert 2 == math_utils.euclid(3, 35)[1]%3
    assert 1 == math_utils.euclid(5, 21)[1]%5
    assert 1 == math_utils.euclid(7, 15)[1]%7


def test_calcul_e():
    assert 70 % day13.calculate_e(3, 105) == 0
    assert 21 % day13.calculate_e(5, 105) == 0
    assert 15 % day13.calculate_e(7, 105) == 0
