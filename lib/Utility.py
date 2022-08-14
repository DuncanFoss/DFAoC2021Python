import os
from typing import Union


def data_reader(
    name: str, ext: str = ".txt", source: str = "./docs/data/", filetype: str = None
) -> 'list[str]':
    """
    Reads a file and returns the content as a list of strings without extra new lines
    """
    return open(f"{source}{name[:-1]}{ext}", "r", newline="").read().splitlines()


def derive_basename(full_path: str) -> str:
    """
    Given the full path up to and including a filename, returns the file name without
    an extension
    """
    path, ext = os.path.splitext(full_path)
    return path.split("/")[-1]


def add_list(data: list) -> Union[int, float]:
    total = 0
    for d in data:
        total += d
    return total
