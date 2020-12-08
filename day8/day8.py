from utils import file_utils


def parse_line(line):
    split = line.split(' ')
    return Instruction(split[0], int(split[1]))


def prepare_data(file_name):
    lines = prepare_lines(file_name)
    return BootCode(lines)


def prepare_lines(file_name):
    lines = file_utils.get_lines("inputs", file_name)
    lines = [parse_line(line) for line in lines]
    return lines


def solution(input_file):
    boot_code = prepare_data(input_file)
    boot_code.execute_all_instructions()
    return boot_code.accumulator


def solution2(input_file):
    lines = prepare_lines(input_file)
    for index, line in enumerate(lines):
        new_instruction = switch_instructions(line)
        if new_instruction:
            new_lines = lines.copy()
            new_lines[index] = new_instruction
            boot_code = BootCode(new_lines)
            boot_code.execute_all_instructions()
            if boot_code.has_terminated():
                return boot_code.accumulator


def switch_instructions(instruction):
    if instruction.operation == 'nop':
        return Instruction('jmp', instruction.argument)
    elif instruction.operation == 'jmp':
        return Instruction('nop', instruction.argument)


class Instruction:
    def __init__(self, operation, argument):
        self.operation = operation
        self.argument = argument


class BootCode:
    def __init__(self, instructions):
        self.instructions = instructions
        self.accumulator = 0
        self.current_position = 0
        self.visited_positions = []

    def execute_next_instruction(self):
        self.visited_positions.append(self.current_position)
        instruction = self.instructions[self.current_position]
        if instruction.operation == 'nop':
            self.current_position += 1
        elif instruction.operation == 'acc':
            self.accumulator += instruction.argument
            self.current_position += 1
        elif instruction.operation == 'jmp':
            self.current_position += instruction.argument

    def execute_all_instructions(self):
        while self.no_loop() and self.is_not_terminated():
            self.execute_next_instruction()

    def no_loop(self):
        return self.current_position not in self.visited_positions

    def is_not_terminated(self):
        return 0 <= self.current_position < len(self.instructions)

    def has_terminated(self):
        return not self.is_not_terminated()