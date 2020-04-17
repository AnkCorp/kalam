"""This module contain file class."""

from kalam.constants.file_type import file_types, UNKNOWN
from kalam.utils.path import (
    get_file_extension_from_path,
    get_path_basename,
)


class File:
    """Base class for file."""

    def __init__(self: "File") -> None:
        """Initialize file instance."""
        self.file = dict()

    def set_file_info(self: "File", data: dict) -> None:
        """Set file info."""
        if bool(data):
            path = data["path"]
            self.file["abs_path"] = path
            self.file["file_name"] = get_path_basename(path)
            self.file["type"] = file_types.get(
                get_file_extension_from_path(path), UNKNOWN
            )
            self.file["metadata"] = data["metadata"]
            self.file["raw"] = data["raw"]
