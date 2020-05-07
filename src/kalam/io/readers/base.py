"""Base module for reader and file."""

from kalam.io.files.base import File
from kalam.utils.path import (
    get_path_accessed_time,
    get_path_created_time,
    get_path_modified_time,
)


class Reader:
    """Reader class.
    
    Here we are not checking whether path exist or not because this class
    assumes that the path given to it exists.

    Also path is absolute path not relative.
    """

    def __init__(self: "Reader") -> None:
        """Initialize reader instance."""
        self.reader = dict()
        self.file = File()

    def init_file_for_packing(self: "Reader", path: str) -> None:
        """Initialize file so that it becomes ready for packing."""
        self.file.set_file_info_for_packing(
            {
                "path": path,
                "metadata": {
                    "created_at": get_path_created_time(path),
                    "accessed_at": get_path_accessed_time(path),
                    "modified_at": get_path_modified_time(path),
                },
            }
        )

    def set_raw_data(self: "Reader") -> None:
        """Read the file and return file object."""
        with open(self.file.file_path()) as file_data:
            self.file.set_file_raw_data(file_data.read())

    def get_file_instance(self: "Reader") -> File:
        """Return the file instance."""
        return self.file

    def get_file(self: "Reader") -> dict:
        """Return the file dict"""
        return self.file.file
