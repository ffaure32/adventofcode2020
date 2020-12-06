import day6


def test_day6():
    result = day6.solution("test_1")
    assert result == 11


def test_day6_real():
    result = day6.solution("input")
    assert result == 6542


def test_day6_part2():
    result = day6.solution2("test_1")
    assert result == 6


def test_day6_real_part2():
    result = day6.solution2("input")
    assert result == 3299
