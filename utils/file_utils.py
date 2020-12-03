from pathlib import Path


def get_lines(path, file_name):
    data_folder = Path(path)
    file_path = data_folder / file_name
    file = open(file_path)
    lines = file.readlines()
    return [line.rstrip('\r\n') for line in lines]

