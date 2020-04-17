"""Utility related to file and path operations."""

import os


def get_abs_path(filename: str, relative_path_of_target: str) -> str:
    """Return the abs path of the target file.

    Require the calling function filename, and path of target file relative to
    the file containing calling function.

    Args:
        relative_path_of_target: relative path of the target file.

    Returns:
        absolute path of the target file.
    """
    dirname = os.path.dirname(os.path.realpath(filename))
    path = os.path.realpath(os.path.join(dirname, relative_path_of_target))
    return path


def generate_path(path_array: list) -> str:
    """Merge the item in the array to form the path.

    If in future we want to switch to another function for path
    then we only have to edit here.

    Args:
        path_array: list of item

    Returns:
        path generated on the basis of path_array
    """
    return os.path.join(*path_array)


def get_path_basename(path: str) -> str:
    """Extract the filename from the path.

    Args:
        path: path of the target file.

    Returns:
        Return the filename.
    """
    return os.path.basename(path)


def get_file_extension_from_path(path: str) -> str:
    """Extract the file extension from the path.

    Args:
        path: path of the target file.

    Returns:
        Return the file extension.
    """
    return str.lower(os.path.splitext(path)[-1])


def path_exist(path: str) -> bool:
    """Check if path exist or not.

    Args:
        path: path whose existence need to check

    Returns:
        Return whether path exist or not
    """
    return os.path.exists(path)


def get_path_accessed_time(path: str) -> float:
    """Returns the last time when path is accessed.

    Args:
        path: target path

    Returns:
        Returns the accessed time as floating point. It returns time from epoch
    """
    return os.path.getatime(path)


def get_path_modified_time(path: str) -> float:
    """Returns the last time when path is modified.

    Args:
        path: target path

    Returns:
        Returns the modified time as floating point. It returns time from epoch
    """
    return os.path.getmtime(path)


def get_path_created_time(path: str) -> float:
    """Returns the path created time.

    Args:
        path: target path

    Returns:
        Returns the created time as floating point. It returns time from epoch
    """
    return os.path.getctime(path)


def mkdir(path: str) -> None:
    """Create the path.

    It first check whether path already exist or not, then creates

    Args:
        path: path to create.
    """
    if not path_exist(path):
        os.path.mkdir(path)


def mkdir_current(filename: str) -> None:
    """Create the path.

    Create directory with respect to current directory

    Args:
        filename: name of the file.
    """
    path = generate_path([os.getcwd(), filename])
    mkdir(path)
