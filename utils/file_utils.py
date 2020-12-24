import os
from pathlib import Path


def get_lines(file_name):
    data_folder = Path("inputs")
    file_path = data_folder / file_name
    file = open(file_path)
    lines = file.readlines()
    return [line.rstrip('\r\n') for line in lines]


def get_file(file_name):
    data_folder = Path("inputs")
    file_path = data_folder / file_name
    file = open(file_path)
    return file.read()
