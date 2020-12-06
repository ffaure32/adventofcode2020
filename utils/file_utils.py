import os
from pathlib import Path


def get_lines(path, file_name):
    data_folder = Path(path)
    print (os.getcwd())
    file_path = data_folder / file_name
    print (file_path)
    file = open(file_path)
    lines = file.readlines()
    return [line.rstrip('\r\n') for line in lines]

