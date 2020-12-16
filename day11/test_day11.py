import day11


def test_neighbours():
    lines = day11.prepare_data("test_1")
    seat_finder = day11.SeatFinder(lines)
    neighbours = seat_finder.find_direct_neighbours(1, 2)
    assert neighbours.count('.') == 3
    assert neighbours.count('L') == 5


def test_neighbours_first_line():
    lines = day11.prepare_data("test_1")
    seat_finder = day11.SeatFinder(lines)
    neighbours = seat_finder.find_direct_neighbours(0, 2)
    assert neighbours.count('.') == 1
    assert neighbours.count('L') == 4


def test_neighbours_first_edge():
    lines = day11.prepare_data("test_1")
    seat_finder = day11.SeatFinder(lines)
    neighbours = seat_finder.find_direct_neighbours(0, 0)
    assert neighbours.count('.') == 1
    assert neighbours.count('L') == 2


def test_neighbours_last_edge():
    lines = day11.prepare_data("test_1")
    seat_finder = day11.SeatFinder(lines)
    neighbours = seat_finder.find_direct_neighbours(9, 9)
    assert neighbours.count('.') == 1
    assert neighbours.count('L') == 2


def test_solution():
    assert 37 == day11.solution("test_1")


def test_solution_real():
    assert 2453 == day11.solution("inputs")


def test_solution2():
    assert 26 == day11.solution2("test_1")


def test_solution2_real():
    assert 2159 == day11.solution2("inputs")