"""Find files of a given type """
from pathlib import Path
from typing import Union


def find_files(file_path: Union[str, Path], file_type: str) -> list:
    """Recursively find files of the stated type along the given file path."""
    return list(Path(file_path).rglob(f"*{file_type}"))
