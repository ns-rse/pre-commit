from .sample import find_files


def test_find_files():
    """Test the find_files() function"""
    py_files = find_files(file_path="./", file_ext=".py")
    assert isinstance(py_files, list)
    assert "sample.py" in py_files
