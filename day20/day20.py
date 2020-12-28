import math
import re

from utils import file_utils, math_utils


class Tile:

    def __init__(self, id) -> None:
        super().__init__()
        self.id = id
        self.lines = []
        self.sides = []
        self.sides_for_bottom = []
        self.neighbours = dict()

    def add_line(self, line):
        self.lines.append(line)

    def compute_sides(self):
        self.sides.append(self.flip_side(self.left()))
        self.sides.append(self.bottom())
        self.sides.append(self.flip_side(self.right()))
        self.sides.append(self.flip_side(self.top()))
        for i in range(4):
            self.sides.append(self.flip_side(self.sides[i]))

    def compute_sides_for_bottom(self):
        self.sides_for_bottom.append(self.top())
        self.sides_for_bottom.append(self.flip_side(self.left()))
        self.sides_for_bottom.append(self.flip_side(self.bottom()))
        self.sides_for_bottom.append(self.right())
        for i in range(4):
            self.sides_for_bottom.append(self.flip_side(self.sides_for_bottom[i]))

    def flip_side(self, side):
        return side[::-1]

    def bottom(self):
        return self.lines[-1]

    def top(self):
        return self.lines[0]

    def left(self):
        return ''.join([line[0] for line in self.lines])

    def right(self):
        return ''.join([line[-1] for line in self.lines])

    def has_common_side(self, other_tile):
        common_side = set(self.sides).intersection(other_tile.sides)
        if common_side:
            common_side = next(iter(common_side))
            self.neighbours[other_tile] = self.sides.index(common_side)
            other_tile.neighbours[self] = other_tile.sides.index(common_side)

    def rotate(self):
        self.lines = list(zip(*self.lines[::-1]))

    def flip_horizontally(self):
        self.lines = self.lines[::-1]

    def flip_vertically(self):
        new_lines = list()
        for line in self.lines:
            line = line[::-1]
            new_lines.append(line)
        self.lines = new_lines

    def print(self):
        [print(line) for line in self.lines]

    def __str__(self) -> str:
        result = ''
        for line in self.lines:
            result += ''.join(line) + '\n'
        return result

    def count_hashtags(self):
        return sum([line.count('#') for line in self.lines])


tile_regex = re.compile(r'Tile (\d*):')


def prepare_data(file_name):
    tiles = list()
    lines = file_utils.get_lines(file_name)
    for line in lines:
        if line.startswith('Tile'):
            match = tile_regex.match(line)
            current_tile = Tile(int(match.group(1)))
        elif not line:
            current_tile.compute_sides()
            current_tile.compute_sides_for_bottom()
            tiles.append(current_tile)
        else:
            current_tile.add_line(line)
    init_neighbours(tiles)
    return tiles


def init_neighbours(tiles):
    for i in range(len(tiles)):
        for j in range(i + 1, len(tiles)):
            tiles[i].has_common_side(tiles[j])


def solution(file_name):
    tiles = prepare_data(file_name)
    corner_tiles = list(filter(lambda tile: len(tile.neighbours) == 2, tiles))
    result = [tile.id for tile in corner_tiles]
    print(math_utils.prod(result))
    return result


def solution2(file_name):
    tiles_matrix = sort_tiles_in_matrix(file_name)
    giant_tile = crop_tiles(tiles_matrix)
    giant_tile_obj = build_tile_object(giant_tile)
    dragons_count = verify_different_angles(giant_tile_obj)
    total_hashtags = giant_tile_obj.count_hashtags()
    return total_hashtags - 15 * dragons_count


def verify_different_angles(giant_tile):
    found_dragons = 0
    found_dragons += verify_dragon(giant_tile.lines)
    giant_tile.rotate()
    found_dragons += verify_dragon(giant_tile.lines)
    giant_tile.rotate()
    found_dragons += verify_dragon(giant_tile.lines)
    giant_tile.rotate()
    found_dragons += verify_dragon(giant_tile.lines)
    giant_tile.flip_vertically()
    found_dragons += verify_dragon(giant_tile.lines)
    giant_tile.rotate()
    found_dragons += verify_dragon(giant_tile.lines)
    giant_tile.rotate()
    found_dragons += verify_dragon(giant_tile.lines)
    giant_tile.rotate()
    found_dragons += verify_dragon(giant_tile.lines)
    return found_dragons


def build_tile_object(giant_tile):
    giant_tile_obj = Tile(12)
    for line in giant_tile:
        giant_tile_obj.add_line(line)
    return giant_tile_obj


def crop_tiles(tiles_matrix):
    matrix_size = len(tiles_matrix)
    giant_tile = list()
    for i in range(matrix_size * 8):
        giant_tile.append(list())
    for i in range(0, matrix_size):
        for j in range(0, matrix_size):
            tile = tiles_matrix[i][j]
            for k in range(0, 8):
                giant_tile[i * 8 + k - 1].extend(tile.lines[k + 1][1:9])
    return giant_tile


def sort_tiles_in_matrix(file_name):
    tiles = prepare_data(file_name)
    matrix_size = round(math.sqrt(len(tiles)))
    tiles_matrix = list()
    for i in range(matrix_size):
        tiles_matrix.append(list())
    corner_tiles = list(filter(lambda tile: len(tile.neighbours) == 2, tiles))
    edge_tiles = list(filter(lambda tile: len(tile.neighbours) <= 3, tiles))
    next_tile = corner_tiles[0]
    next_tile.rotate()
    next_tile.rotate()
    edge_tiles.remove(next_tile)
    tiles.remove(next_tile)
    tiles_matrix[0].append(next_tile)
    # first line
    for i in range(1, matrix_size):
        previous_tile = next_tile
        next_tile = list(filter(lambda tile: tile in next_tile.neighbours.keys(), edge_tiles))[0]
        rotate_for_right(previous_tile, next_tile)
        tiles_matrix[0].append(next_tile)
        edge_tiles.remove(next_tile)
        tiles.remove(next_tile)
    # first column
    for i in range(1, matrix_size):
        previous_tile = tiles_matrix[i - 1][0]
        next_tile = list(filter(lambda tile: tile in previous_tile.neighbours.keys(), edge_tiles))[0]
        rotate_for_bottom(previous_tile, next_tile)
        tiles_matrix[i].append(next_tile)
        edge_tiles.remove(next_tile)
        tiles.remove(next_tile)
    # inside tiles
    for i in range(1, matrix_size):
        for j in range(1, matrix_size):
            previous_tile = tiles_matrix[i - 1][j]
            next_tile = list(filter(
                lambda tile: tile in previous_tile.neighbours.keys() and tile in tiles_matrix[i][
                    j - 1].neighbours.keys(), tiles))[0]
            rotate_for_bottom(previous_tile, next_tile)
            tiles_matrix[i].append(next_tile)
            tiles.remove(next_tile)
    return tiles_matrix


def rotate_for_right(previous_tile, next_tile):
    face_to_find = ''.join(previous_tile.right())
    to_rotate = next_tile.sides.index(face_to_find)
    number_of_rotations = to_rotate % 4
    for k in range(number_of_rotations):
        next_tile.rotate()
    if to_rotate >= 4:
        next_tile.flip_horizontally()


def rotate_for_bottom(previous_tile, next_tile):
    face_to_find = ''.join(previous_tile.bottom())
    to_rotate = next_tile.sides_for_bottom.index(face_to_find)
    number_of_rotations = to_rotate % 4
    for j in range(number_of_rotations):
        next_tile.rotate()
    if to_rotate >= 4:
        next_tile.flip_vertically()


dragon = list()
dragon.append(list('                  # '))
dragon.append(list('#    ##    ##    ###'))
dragon.append(list(' #  #  #  #  #  #   '))


def is_dragon(sub_tile):
    for i in range(len(dragon)):
        for j in range(len(dragon[0])):
            if dragon[i][j] == '#':
                if sub_tile[i][j] != '#':
                    return False
    return True


def test_dragon():
    assert is_dragon(dragon)


def verify_dragon(giant_tile):
    count_dragons = 0
    for i in range(len(giant_tile)-len(dragon)):
        for j in range(len(giant_tile[0])-len(dragon[0])):
            sub_tile = list()
            for k in range(len(dragon)):
                sub_tile.append(giant_tile[i+k][j:j+len(dragon[0])])
            if is_dragon(sub_tile):
                count_dragons = count_dragons + 1
    return count_dragons


def test_solution():
    result = solution('input')
    assert 51214443014783 == math_utils.prod(result)


def test_solution2():
    result = solution2('input')
    print(result)
    assert 51214443014783 == result
