from utils import file_utils

FLOOR = '.'
EMPTY = 'L'
OCCUPIED = '#'


def prepare_data(file_name):
    return file_utils.get_lines(file_name)


def solution(file_name):
    lines = prepare_data(file_name)
    seat_finder = SeatFinder(lines)
    return seat_finder.find_seats(seat_finder.find_direct_neighbours, 4)


def solution2(file_name):
    lines = prepare_data(file_name)
    seat_finder = SeatFinder(lines)
    return seat_finder.find_seats(seat_finder.find_visible_neighbours, 5)


def count_occupied(lines):
    return sum([line.count('#') for line in lines])


class SeatFinder:
    def __init__(self, lines):
        self.lines = lines
        self.nb_lines = len(lines)
        self.nb_columns = len(lines[0])

    def find_seats(self, find_function, tolerance):
        change = True
        while change:
            change = self.next_round(find_function, tolerance)
        return count_occupied(self.lines)

    def next_round(self, find_method, tolerance):
        change = False
        after_round = []
        for line_index in range(0, self.nb_lines):
            new_line = []
            for column_index in range(0, self.nb_columns):
                cell = self.lines[line_index][column_index]
                new_seat_state = cell
                if cell == EMPTY:
                    neighbours = find_method(line_index, column_index)
                    if neighbours.count(OCCUPIED) == 0:
                        new_seat_state = OCCUPIED
                        change = True
                elif cell == OCCUPIED:
                    neighbours = find_method(line_index, column_index)
                    if neighbours.count(OCCUPIED) >= tolerance:
                        new_seat_state = EMPTY
                        change = True
                new_line.append(new_seat_state)
            after_round.append(new_line)
        self.lines = after_round
        return change

    def find_direct_neighbours(self, line_index, column_index):
        neighbours = []
        for i in range(max(0, column_index - 1), min(column_index + 2, self.nb_columns)):
            for j in range(max(0, line_index - 1), min(line_index + 2, self.nb_lines)):
                if i != column_index or j != line_index:
                    neighbours.append(self.lines[j][i])
        return neighbours

    def find_visible_neighbours(self, line_index, column_index):
        neighbours = []
        self.find_north_neighbour(column_index, line_index, neighbours)
        self.find_south_neighbour(column_index, line_index, neighbours)
        self.find_west_neighbour(column_index, line_index, neighbours)
        self.find_east_neighbour(column_index, line_index, neighbours)
        self.find_north_west_neighbour(column_index, line_index, neighbours)
        self.find_north_east_neighbour(column_index, line_index, neighbours)
        self.find_south_west_neighbour(column_index, line_index, neighbours)
        self.find_south_east_neighbour(column_index, line_index, neighbours)
        return neighbours

    def find_south_east_neighbour(self, column_index, line_index, neighbours):
        for i in range(1,
                       min(self.nb_columns - column_index, len(self.lines) - line_index)):
            if self.lines[line_index + i][column_index + i] != FLOOR:
                neighbours.append(self.lines[line_index + i][column_index + i])
                break

    def find_south_west_neighbour(self, column_index, line_index, neighbours):
        for i in range(1, min(column_index + 1, len(self.lines) - line_index)):
            if self.lines[line_index + i][column_index - i] != FLOOR:
                neighbours.append(self.lines[line_index + i][column_index - i])
                break

    def find_north_east_neighbour(self, column_index, line_index, neighbours):
        for i in range(1, min(self.nb_columns - column_index, line_index + 1)):
            if self.lines[line_index - i][column_index + i] != FLOOR:
                neighbours.append(self.lines[line_index - i][column_index + i])
                break

    def find_north_west_neighbour(self, column_index, line_index, neighbours):
        for i in range(1, min(column_index + 1, line_index + 1)):
            if self.lines[line_index - i][column_index - i] != FLOOR:
                neighbours.append(self.lines[line_index - i][column_index - i])
                break

    def find_west_neighbour(self, column_index, line_index, neighbours):
        for i in range(column_index - 1, -1, -1):
            if self.lines[line_index][i] != FLOOR:
                neighbours.append(self.lines[line_index][i])
                break

    def find_east_neighbour(self, column_index, line_index, neighbours):
        for i in range(column_index + 1, self.nb_columns):
            if self.lines[line_index][i] != FLOOR:
                neighbours.append(self.lines[line_index][i])
                break

    def find_south_neighbour(self, column_index, line_index, neighbours):
        for i in range(line_index + 1, len(self.lines)):
            if self.lines[i][column_index] != FLOOR:
                neighbours.append(self.lines[i][column_index])
                break

    def find_north_neighbour(self, column_index, line_index, neighbours):
        for i in range(line_index - 1, -1, -1):
            if self.lines[i][column_index] != FLOOR:
                neighbours.append(self.lines[i][column_index])
                break
