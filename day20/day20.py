import math
import re

from utils import file_utils, math_utils


class Tile:

    def __init__(self, id) -> None:
        super().__init__()
        self.id = id
        self.lines = []
        self.sides = []
        self.neighbours = dict()

    def add_line(self, line):
        self.lines.append(line)

    def upper_side(self):
        return self.lines[0]

    def lower_side(self):
        return self.lines[-1]

    def compute_sides(self):
        self.sides.append(self.lines[0])
        self.sides.append(''.join([line[0] for line in self.lines]))
        self.sides.append(''.join([line[-1] for line in self.lines]))
        self.sides.append(self.lines[-1])
        for i in range(4):
            self.sides.append(self.sides[i][::-1])

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
    print()
    # first line
    for i in range(1, matrix_size):
        previous_tile = next_tile
        next_tile = list(filter(lambda tile: tile in next_tile.neighbours.keys(), edge_tiles))[0]
        previous_tile.print()
        print(previous_tile.neighbours[next_tile])
        print(next_tile.neighbours[previous_tile])
        to_rotate = next_tile.neighbours[previous_tile]
        if to_rotate == 3:
            next_tile.rotate()
            next_tile.rotate()
        tiles_matrix[0].append(next_tile)
        edge_tiles.remove(next_tile)
        tiles.remove(next_tile)
    # first column
    for i in range(1, matrix_size):
        next_tile = list(filter(lambda tile: tile in tiles_matrix[i - 1][0].neighbours.keys(), edge_tiles))[0]
        tiles_matrix[i].append(next_tile)
        edge_tiles.remove(next_tile)
        tiles.remove(next_tile)
    # inside tiles
    for i in range(1, matrix_size):
        for j in range(1, matrix_size):
            next_tile = list(filter(
                lambda tile: tile in tiles_matrix[i - 1][j].neighbours.keys() and tile in tiles_matrix[i][
                    j - 1].neighbours.keys(), tiles))[0]
            tiles_matrix[i].append(next_tile)
            tiles.remove(next_tile)

    for i in range(0, matrix_size):
        for j in range(0, matrix_size):
            tiles_matrix[j][i].print()
            print()
    return tiles_matrix


def test_solution():
    result = solution('input')
    assert 51214443014783 == math_utils.prod(result)


def test_solution2():
    result = solution2('input')
    assert 51214443014783 == math_utils.prod(result)
