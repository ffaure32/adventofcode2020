from utils import file_utils


def navigate(direction, coords):
    if direction == 'e':
        return (coords[0] + 2, coords[1])
    elif direction == 'w':
        return (coords[0] - 2, coords[1])
    elif direction == 'se':
        return (coords[0] + 1, coords[1] - 1)
    elif direction == 'sw':
        return (coords[0] - 1, coords[1] - 1)
    elif direction == 'ne':
        return (coords[0] + 1, coords[1] + 1)
    elif direction == 'nw':
        return (coords[0] - 1, coords[1] + 1)


def parse_line(line):
    moves = list()
    keep =''
    for move in line:
        if move in ('s', 'n'):
            keep = move
        else:
            moves.append(keep + move)
            keep = ''
    return moves


def new_coords(moves):
    coords = (0, 0)
    for move in moves:
        coords = navigate(move, coords)
    return coords


def prepare_data(file_name):
    flipped = set()
    lines = file_utils.get_lines(file_name)
    for line in lines:
        moves = parse_line(line)
        coords = new_coords(moves)
        if coords not in flipped:
            flipped.add(coords)
        else:
            flipped.remove(coords)
    return flipped


def solution(file_name):
    flipped = prepare_data(file_name)
    return len(flipped)


def test_solution():
    count = solution('test_1')
    print(count)
    assert 10 == count


def test_solution_real():
    count = solution('input')
    print(count)
    assert 485 == count


def test_parse_line():
    line = 'nwwswee'
    moves = parse_line(line)
    assert ['nw', 'w', 'sw', 'e', 'e'] == moves


def test_navigate():
    coords = (0, 0)
    moves = ['nw', 'w', 'sw', 'e', 'e']
    for move in moves:
        coords = navigate(move, coords)
    assert (0, 0) == coords
