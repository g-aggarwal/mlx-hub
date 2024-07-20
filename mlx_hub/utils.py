# Copyright (c) 2024 Gaurav Aggarwal

from importlib.resources import files
from typing import List

PACKAGE_PATH = 'mlx_hub'


def read_packaged_file(file_name: str) -> List[str]:
    """Reads and returns suggested models from a file."""
    try:
        with files(PACKAGE_PATH).joinpath(file_name).open() as file_name:
            lines = file_name.readlines()
            return [line.strip() for line in lines]
    except (FileNotFoundError, IOError):
        print(f"An error occurred while reading the file at path {file_name}.")
        return []


def print_packaged_file(file_name: str):
    """Prints suggested models from a file."""
    for line in read_packaged_file(file_name):
        print(line)
