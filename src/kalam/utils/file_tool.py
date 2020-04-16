"""Utility related to file and path operations."""

import os

from kalam.constants import file_type


def get_abs_path(filename: str, relative_path_of_target: str) -> str:
    """Return the abs path of the target file.

    Require the calling function filename, and path of target file relative to
    the file containing calling function.

    Args:
        filename: file name of the calling function. usually __file__.
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
    return os.path.realpath(os.path.join(*path_array))


def get_path_basename(path: str) -> str:
    """Extract the filename from the path.

    Args:
        path: path of the target file.

    Returns:
        Return the filename.
    """
    return os.path.basename(path)


def get_file_type(path: str) -> str:
    """Extract the file type from file path.

    Args:
        path: path of the target file.

    Returns:
        Return the file type.
    """
    ext = str.lower(os.path.splitext(path)[-1])
    return {
        ".html": file_type.HTML,
        ".htm": file_type.HTML,
        ".pdf": file_type.PDF,
        ".md": file_type.MD,
        ".rst": file_type.RST,
        ".tex": file_type.TEX,
        ".js": file_type.JS,
        ".py": file_type.PY,
        ".jsx": file_type.JSX,
        ".toml": file_type.TOML,
    }.get(ext, file_type.UNKNOWN)


def get_file_metadata(path: str) -> dict:
    """Generate file metadata using file path.

    Args:
        path: path of the target file.

    Returns:
        Return the file metadata.
    """
    func = os.path
    metadata = {
        "created_at": func.getctime(path),
        "accessed_at": func.getatime(path),
        "modified_at": func.getmtime(path),
    }
    return metadata
