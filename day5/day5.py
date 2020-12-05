from utils import file_utils


class SeatRange:
    def __init__(self, seat_code = None):
        self.right_left_interval = [0, 7]
        self.front_back_interval = [0, 127]

        if seat_code:
            self.initiate_position(seat_code)

    def initiate_position(self, seat_code):
        fb_commands = seat_code[: - 3]
        for command in fb_commands:
            self.split_front_back(command)
        lr_commands = seat_code[- 3:]
        for command in lr_commands:
            self.split_right_left(command)

    def split_front_back(self, part):
        split(self.front_back_interval, part == 'F')

    def split_right_left(self, part):
        split(self.right_left_interval, part == 'L')

    def coords(self):
        return ((self.front_back_interval[0], self.right_left_interval[0]))

    def seat_id(self):
        coords = self.coords()
        return coords[0]*8 + coords[1]


def split(coords, up):
    middle = (coords[1] - coords[0]) // 2 + 1
    if up:
        coords[1] -= middle
    else:
        coords[0] += middle


def prepare_data(file_name):
    lines = file_utils.get_lines("inputs", file_name)
    return [SeatRange(line).seat_id() for line in lines]


def solution(file_name):
    lines = prepare_data(file_name)
    return max(lines)


def solution2(file_name):
    lines = prepare_data(file_name)
    lines.sort()
    for i in range(len(lines)):
        if lines[i] != lines[i+1]-1:
            return lines[i]+1
    pass
