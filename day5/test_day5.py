import day5


def test_first_part():
    seat_range = day5.SeatRange()
    seat_range.split_front_back('F')
    assert seat_range.front_back_interval == [0,63]

def test_first_part_2():
    seat_range = day5.SeatRange()
    seat_range.split_front_back('F')
    seat_range.split_front_back('B')
    seat_range.split_front_back('F')
    seat_range.split_front_back('B')
    seat_range.split_front_back('B')
    seat_range.split_front_back('F')
    seat_range.split_front_back('F')
    assert seat_range.front_back_interval == [44,44]


def test_second_part():
    seat_range = day5.SeatRange()
    seat_range.split_right_left('R')
    seat_range.split_right_left('L')
    seat_range.split_right_left('R')
    assert seat_range.right_left_interval == [5,5]


def test_find_input_coords():
    assert day5.SeatRange("BFFFBBFRRR").coords() == (70, 7)
    assert day5.SeatRange("FFFBBBFRRR").coords() == (14, 7)
    assert day5.SeatRange("BBFFBBFRLL").coords() == (102, 4)


def test_find_seat_id():
    assert day5.SeatRange("BFFFBBFRRR").seat_id() == 567
    assert day5.SeatRange("FFFBBBFRRR").seat_id() == 119
    assert day5.SeatRange("BBFFBBFRLL").seat_id() == 820


def test_day5():
    result = day5.solution("test_1")
    assert result == 820


def test_day5_real():
    result = day5.solution("inputs")
    assert result == 928


def test_day5_part2_real():
    result = day5.solution2("inputs")
    assert result == 610
