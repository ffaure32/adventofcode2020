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


def all_moves(coords):
    all_moves = set()
    all_moves.add((coords[0] + 2, coords[1]))
    all_moves.add((coords[0] - 2, coords[1]))
    all_moves.add((coords[0] + 1, coords[1] - 1))
    all_moves.add((coords[0] - 1, coords[1] - 1))
    all_moves.add((coords[0] + 1, coords[1] + 1))
    all_moves.add((coords[0] - 1, coords[1] + 1))
    return all_moves


def parse_line(line):
    moves = list()
    keep = ''
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


def one_cell(tiles, tile, was_black):
    blacks = 0
    whites = 0
    for other_tile in all_moves(tile):
        if other_tile in tiles:
            blacks += 1
        else:
            whites += 1
    if was_black:
        if blacks == 0 or blacks > 2:
            return True
    else:
        if blacks == 2:
            return True
    return False


def maxes(flipped):
    minx, miny, maxx, maxy = 0, 0, 0, 0
    for flip in flipped:
        minx = min(minx, flip[0])
        maxx = max(maxx, flip[0])
        miny = min(miny, flip[1])
        maxy = max(maxy, flip[1])
        minxy = min(minx, miny) - 1
        maxxy = max(maxx, maxy) + 1
    return minxy, maxxy


def solution2(file_name):
    flipped = prepare_data(file_name)
    for i in range(100):
        flipped = one_turn(flipped)
    return flipped


def one_turn(flipped):
    new_flipped = set()
    minxy, maxxy = maxes(flipped)
    for y in range(minxy, maxxy + 1):
        if y % 2 != minxy % 2:
            minx = minxy - 1
            maxx = maxxy + 1
        else:
            minx = minxy
            maxx = maxxy
        for x in range(minx, maxx + 1, 2):
            in_flipped = (x, y) in flipped
            changed = one_cell(flipped, (x, y), in_flipped)
            if changed and not in_flipped:
                new_flipped.add((x, y))
            if not changed and in_flipped:
                new_flipped.add((x, y))
    return new_flipped


def test_solution2():
    new_matrix = solution2('input')
    assert 3933 == len(new_matrix)


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
