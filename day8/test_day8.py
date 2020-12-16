import day8


def test_parse_line():
    input = 'jmp -613'
    result = day8.parse_line(input)

    assert result.operation == 'jmp'
    assert result.argument == -613


def test_prepare_data():
    boot_code = day8.prepare_data('test_1')
    assert len(boot_code.instructions) == 9
    assert boot_code.accumulator == 0
    assert boot_code.current_position == 0
    assert not boot_code.visited_positions


def test_execute_instruction():
    boot_code = day8.prepare_data('test_1')
    boot_code.execute_next_instruction()
    assert boot_code.accumulator == 0
    assert boot_code.current_position == 1
    assert boot_code.visited_positions == [0]


def test_execute_2_instruction():
    boot_code = day8.prepare_data('test_1')
    boot_code.execute_next_instruction()
    boot_code.execute_next_instruction()
    assert boot_code.accumulator == 1
    assert boot_code.current_position == 2
    assert boot_code.visited_positions == [0, 1]


def test_execute_3_instruction():
    boot_code = day8.prepare_data('test_1')
    boot_code.execute_next_instruction()
    boot_code.execute_next_instruction()
    boot_code.execute_next_instruction()
    assert boot_code.accumulator == 1
    assert boot_code.current_position == 6
    assert boot_code.visited_positions == [0, 1, 2]


def test_execute_all_instructions():
    boot_code = day8.prepare_data('test_1')
    boot_code.execute_all_instructions()
    assert boot_code.accumulator == 5


def test_day8():
    result = day8.solution('test_1')
    assert result == 5


def test_day8_real():
    result = day8.solution('inputs')
    assert result == 1928


def test_is_terminated():
    result = day8.solution('test_2')
    assert result == 8


def test_day8_part2():
    result = day8.solution2('test_1')
    assert result == 8


def test_day8_part2_real():
    result = day8.solution2('inputs')
    assert result == 1319
