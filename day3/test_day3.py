import day3


def test_parse_line_basic():
    line = "...#.."

    assert day3.cell_at(line, 3) == '#'


def test_parse_line_repeated():
    line = "...#.."

    assert day3.cell_at(line, 9) == '#'


def test_parse_line_repeated_twice():
    line = "...#.."

    assert day3.cell_at(line, 15) == '#'


def test_parse_line_repeated_divisor():
    line = "...#...#"

    assert day3.cell_at(line, 15) == '#'


def test_parse_line_just_after_length():
    line = "...#...#"

    assert day3.cell_at(line, 8) == '.'


def test_day3():
    result = day3.solution("test_1")
    assert result == 7


def test_day3_real():
    result = day3.solution("input")
    assert result == 173


def test_day3_part2():
    result = day3.solution2("test_1")
    assert result == 336


def test_day3_real_part2():
    result = day3.solution2("input")
    assert result == 4385176320

