"""Tests for util/path.

Tests must be written in order in which they are defined in kalam.utils.path
"""

import os
from typing import List

import kalam.utils.path as path_util


def test_generate_abs_path() -> None:
    """Test generate_abs_path function."""
    relative_path = path_util.generate_path(["..", "..", "test"])
    abs_path = path_util.generate_abs_path(__file__, relative_path)
    assert abs_path.__contains__("test") is True


def test_generate_path() -> None:
    """Test generate_path."""
    test_path = path_util.generate_path([path_util.pwd(), "..", "..", "test"])
    actual_path = os.path.join(path_util.pwd(), "..", "..", "test")
    assert test_path == actual_path


def test_get_path_basename() -> None:
    """Test get_path_basename."""
    path = "../test/folder/space contained folder/testfile.pdf"
    filename = path_util.get_path_basename(path)
    assert filename == "testfile.pdf"


def test_get_file_extension_from_path() -> None:
    """Test get_file_extension_from_path."""
    path = "../test/folder/space contained folder/testfile.pdf"
    test_ext = path_util.get_file_extension_from_path(path)
    actual_ext = ".pdf"
    assert test_ext == actual_ext


def test_path_exist() -> None:
    """Test path_exist.

    Assuming "./didn't exist" actually not exist.
    """
    path = path_util.generate_abs_path(__file__, "didn't exist")
    assert path_util.path_exist(path) is False

    path = path_util.generate_abs_path(__file__, "test_file.py")
    assert path_util.path_exist(path) is True


def test_get_path_accessed_time() -> None:
    """Test get_path_accessed_time."""
    path = "test_file.py"
    path = path_util.generate_abs_path(__file__, path)
    accessed_at = path_util.get_path_accessed_time(path)
    assert isinstance(accessed_at, float)


def test_get_path_modified_time() -> None:
    """Test get_path_modified_time."""
    path = "test_file.py"
    path = path_util.generate_abs_path(__file__, path)
    modified_time = path_util.get_path_modified_time(path)
    assert isinstance(modified_time, float)


def test_get_path_created_time() -> None:
    """Test get_path_created_time."""
    path = "test_file.py"
    path = path_util.generate_abs_path(__file__, path)
    created_time = path_util.get_path_created_time(path)
    assert isinstance(created_time, float)


def test_mkdir() -> None:
    """Test mkdir.

    Assuming test_folder didn't exist
    """
    path = path_util.generate_abs_path(__file__, "test_folder")
    assert path_util.mkdir(path) is True
    assert path_util.mkdir(path) is False
    path_util.rmdir(path)


def test_mkdir_current() -> None:
    """Test mkdir_current."""
    path = "test_folder_2"
    path_util.mkdir_current(path)
    assert path_util.path_exist(path) is True

    actual_path = path_util.generate_path([path_util.pwd(), path])
    path_util.rmdir(actual_path)
    assert path_util.path_exist(actual_path) is False


def test_rmdir() -> None:
    """Test rmdir."""
    path = path_util.generate_abs_path(__file__, "test_folder_3")
    path_util.mkdir(path)
    assert path_util.path_exist(path) is True

    path_util.rmdir(path)
    assert path_util.path_exist(path) is False


def test_create_file_current() -> None:
    """Test create_file_current."""
    filename = "test_file_2.txt"
    write = "This is test input"
    path_util.create_file_current(filename, write)
    actual_path = path_util.generate_path([path_util.pwd(), filename])

    assert path_util.path_exist(actual_path) is True

    with open(actual_path) as f:
        assert write == f.read()

    os.remove(actual_path)


def test_pwd() -> None:
    """Test pwd."""
    test_pwd = path_util.pwd()
    actual_pwd = os.getcwd()
    assert test_pwd == actual_pwd


def test_tree() -> None:
    """Test tree."""
    path = "."
    function_tree = path_util.tree(path)
    files: List[str] = []

    for _, _, f in function_tree:
        for file in f:
            files.append(file)

    assert "test_file.py" in files
    assert "test_path.py" in files


def test_split_path_directories() -> None:
    """Test split_path_directories."""
    path = "/this/is/the/path"
    path_list = path_util.split_path_directories(path)
    assert len(path_list) == 4
    assert "this" in path_list
    assert "is" in path_list
    assert "the" in path_list
    assert "path" in path_list


def test_path_diff() -> None:
    """Test path_diff."""
    path1 = "/this/is/path/"
    path2 = "/this/is/path/2/with/extra/dir"

    path_diff = path_util.path_diff(path1, path2)
    assert path_diff == "2/with/extra/dir"

    path_diff = path_util.path_diff(path2, path1)
    assert path_diff == "2/with/extra/dir"


def test_dir_in_ignore_list() -> None:
    """Test check_dir_in_ignore_list."""

    path_list = [
        "/user/ank/test/test1",
        "/user/ank/website/dist",
        "/user/ank/website/website2",
    ]
    path = "/user/ank/folder1"
    path2 = "/user/ank/website/dist/static"
    path3 = "/user/ank/website/dist/static/image"
    path4 = "/user/ank/website/website3/"
    path5 = "/user/ank/website/website3/cool-stuffs"

    assert path_util.dir_in_ignore_list(path, path_list) is False
    assert path_util.dir_in_ignore_list(path2, path_list) is True
    assert path_util.dir_in_ignore_list(path3, path_list) is True
    assert path_util.dir_in_ignore_list(path4, path_list) is False
    assert path_util.dir_in_ignore_list(path5, path_list) is False
