"""Tests for util/path."""

import os

from kalam.utils.path import (
    generate_abs_path,
    get_file_extension_from_path,
    generate_path,
    get_path_basename,
    get_path_accessed_time,
    get_path_created_time,
    get_path_modified_time,
    path_exist,
    pwd,
)


def test_pwd() -> None:
    """Test pwd."""
    test_pwd = pwd()
    actual_pwd = os.getcwd()
    assert test_pwd == actual_pwd


def test_generate_path() -> None:
    """Test generate_path."""
    test_path = generate_path([pwd(), "..", "..", "test"])
    actual_path = os.path.join(pwd(), "..", "..", "test")
    assert test_path == actual_path


def test_generate_abs_path() -> None:
    """Test generate_abs_path function."""
    relative_path = generate_path(["..", "..", "test"])
    abs_path = generate_abs_path(__file__, relative_path)
    assert abs_path.__contains__("test") == True


def test_get_file_extension_from_path() -> None:
    """Test get_file_extension_from_path."""
    path = "../test/folder/space contained folder/testfile.pdf"
    test_ext = get_file_extension_from_path(path)
    actual_ext = ".pdf"
    assert test_ext == actual_ext
