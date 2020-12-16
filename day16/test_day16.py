import day16


def test_parse_ranges():
    field_range = day16.FieldRange('departure location: 36-269 or 275-973')

    assert 'departure location' == field_range.name
    assert (36, 269) == field_range.first_range
    assert (275, 973) == field_range.second_range


def test_prepare_data():
    input = day16.prepare_data('test_1')
    assert len(input.fields) == 3
    assert len(input.other_tickets) == 4


def test_solution():
    errors_sum = day16.solution('test_1')
    assert 71 == errors_sum


def test_solution_real():
    errors_sum = day16.solution('input')
    assert 22073 == errors_sum


def test_solution2_real():
    result = day16.solution2('input')
    assert 1346570764607 == result
