import os
from pathlib import Path


def get_lines(file_name):
    data_folder = Path("inputs")
    print (os.getcwd())
    file_path = data_folder / file_name
    print (file_path)
    file = open(file_path)
    lines = file.readlines()
    return [line.rstrip('\r\n') for line in lines]

