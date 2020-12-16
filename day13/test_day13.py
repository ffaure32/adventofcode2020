import day13
from utils import math_utils


def test_print():
    assert 295 == day13.solution('test_1')


def test_print_real():
    assert 4938 == day13.solution('inputs')


def test_sol2():
    assert 1068781 == day13.solution2('test_1')


def test_sample1():
    bus_by_ids = day13.build_gaps_by_bus_id('17,x,13,19')
    assert 3417 == day13.calculate_with_chinese_remainder(bus_by_ids)


def test_sample2():
    bus_by_ids = day13.build_gaps_by_bus_id('67,7,59,61')
    assert 754018 == day13.calculate_with_chinese_remainder(bus_by_ids)


def test_sample3():
    bus_by_ids = day13.build_gaps_by_bus_id('67,x,7,59,61')
    assert 779210 == day13.calculate_with_chinese_remainder(bus_by_ids)


def test_sample4():
    bus_by_ids = day13.build_gaps_by_bus_id('67,7,x,59,61')
    assert 1261476 == day13.calculate_with_chinese_remainder(bus_by_ids)


def test_sample5():
    bus_by_ids = day13.build_gaps_by_bus_id('1789,37,47,1889')
    assert 1202161486 == day13.calculate_with_chinese_remainder(bus_by_ids)


def test_sol2_real():
    assert 230903629977901 == day13.solution2('inputs')


def test_euclid():
    assert 2 == math_utils.euclid_extended_calc(3, 35)[1] % 3
    assert 1 == math_utils.euclid_extended_calc(5, 21)[1] % 5
    assert 1 == math_utils.euclid_extended_calc(7, 15)[1] % 7


def test_calcul_e():
    assert 70 % day13.calculate_e(3, 105) == 0
    assert 21 % day13.calculate_e(5, 105) == 0
    assert 15 % day13.calculate_e(7, 105) == 0
