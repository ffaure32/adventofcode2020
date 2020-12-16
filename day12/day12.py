from utils import file_utils
import math


def prepare_data(file_name):
    return file_utils.get_lines(file_name)


def solution(file_name):
    lines = prepare_data(file_name)
    ship = Ship()
    [ship.move(line) for line in lines]
    return manhattan_distance(ship.position)


def solution2(file_name):
    lines = prepare_data(file_name)
    ship = ShipWithWayPoint()
    [ship.move(line) for line in lines]
    return manhattan_distance(ship.position)


DIRECTIONS = ['E', 'S', 'W', 'N']


class Ship:
    def __init__(self):
        self.direction = 'E'
        self.position = (0, 0)

    def move(self, instruction):
        command = instruction[:1]
        value = int(instruction[1:])
        if command == "R":
            self.real_turn(value)
        elif command == "L":
            self.real_turn(-value)
        elif command == 'F':
            self.position = real_move(self.position, self.direction, value)
        else:
            self.position = real_move(self.position, command, value)

    def real_turn(self, value):
        rotation = value // 90
        turn = DIRECTIONS.index(self.direction)
        self.direction = DIRECTIONS[(turn + rotation) % len(DIRECTIONS)]


class ShipWithWayPoint:
    def __init__(self):
        self.direction = 'E'
        self.position = (0, 0)
        self.way_point = (10, -1)

    def move(self, instruction):
        command = instruction[:1]
        value = int(instruction[1:])
        if command == "R":
            self.real_turn(value)
        elif command == "L":
            self.real_turn(-value)
        elif command == 'F':
            self.position = (self.position[0] + self.way_point[0] * value,
                            self.position[1] + self.way_point[1] * value)
        else:
            self.way_point = real_move(self.way_point, command, value)

    def real_turn(self, value):
        value = math.radians(value)
        cos = math.cos(value)
        sin = math.sin(value)
        self.way_point = (cos * self.way_point[0] - sin * self.way_point[1],
                          sin * self.way_point[0] + cos * self.way_point[1])


def real_move(position, command, value):
    if command == 'E':
        position = (position[0] + value, position[1])
    elif command == 'N':
        position = (position[0], position[1] - value)
    elif command == 'W':
        position = (position[0] - value, position[1])
    elif command == 'S':
        position = (position[0], position[1] + value)
    return position


def manhattan_distance(position):
    return round(abs(position[0])) + round(abs(position[1]))
