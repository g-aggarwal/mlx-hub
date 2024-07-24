# Copyright (c) 2024 Gaurav Aggarwal

from importlib.resources import files
from typing import List

PACKAGE_DATA_PATH = 'mlx_hub.data'


def read_packaged_file(file_name: str) -> List[str]:
    """Reads and returns text from packaged file."""
    try:
        with files(PACKAGE_DATA_PATH).joinpath(file_name).open() as file_name:
            lines = file_name.readlines()
            return [line.strip() for line in lines]
    except (FileNotFoundError, IOError):
        print(f"An error occurred while reading the file at path {file_name}.")
        return []


def print_packaged_file(file_name: str):
    """Prints text from packaged file."""
    for line in read_packaged_file(file_name):
        print(line)
