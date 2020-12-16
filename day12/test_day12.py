import day12


def test_init_ship():
    ship = day12.Ship()
    assert ship.direction == 'E'
    assert ship.position == (0, 0)


def test_front_move():
    ship = day12.Ship()
    ship.move("F10")
    assert ship.direction == 'E'
    assert ship.position == (10, 0)


def test_solution():
    result = day12.solution("test_1")
    assert result == 25


def test_solution_real():
    result = day12.solution("inputs")
    assert result == 508


def test_solution2():
    result = day12.solution2("test_1")
    assert result == 286

def test_solution22():
    result = day12.solution2("test_2")
    assert result == 332


def test_solution2_real():
    result = day12.solution2("inputs")
    assert result == 30761
