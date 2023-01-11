"""Find files of a given type """
from pathlib import Path
from typing import Union


def find_files(file_path: Union[str, Path], file_type: str):
    """Recursively find and load files of the stated type along the given file path."""
    return Path(file_path).rglob(f"*{file_type}")
