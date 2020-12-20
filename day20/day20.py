import re

from utils import file_utils, math_utils


class Tile:

    def __init__(self, id) -> None:
        super().__init__()
        self.id = id
        self.lines = []
        self.sides = []
        self.neighbours = set()

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
        if any(side in other_tile.sides for side in self.sides):
            self.neighbours.add(other_tile)
            other_tile.neighbours.add(self)


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
    return tiles


def solution(file_name):
    tiles = prepare_data(file_name)
    for i in range(len(tiles)):
        for j in range(i + 1, len(tiles)):
            tiles[i].has_common_side(tiles[j])
    corner_tiles = list(filter(lambda tile: len(tile.neighbours) == 2, tiles))
    result = [tile.id for tile in corner_tiles]
    print(math_utils.prod(result))
    return result


def test_solution():
    result = solution('input')
    assert 51214443014783 == math_utils.prod(result)
