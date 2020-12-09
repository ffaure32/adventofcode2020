import day9


def test_day9():
    arr = [i+1 for i in range(25)]
    assert day9.is_valid(arr, 26)
    assert day9.is_valid(arr, 49)
    assert not day9.is_valid(arr, 100)
    assert not day9.is_valid(arr, 50)


def test_find_first_weakness():
    result = day9.solution("test_1", 5)
    assert 127 == result


def test_day9_real():
    result = day9.solution("input", 25)
    assert 127 == result


def test_day9_part2():
    result = day9.solution2("test_1")
    pass
    # assert result == 32


def test_day9_real_part2():
    result = day9.solution2("input")
    pass
    # assert result == 421550
