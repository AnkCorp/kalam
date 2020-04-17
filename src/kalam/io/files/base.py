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
            self.set_file_abs_path(data["path"])
            self.set_file_name(data["path"])
            self.set_file_type(data["path"])
            self.set_file_metadata(data["metadata"])
            self.set_file_raw_data(data["raw"])

    def set_file_abs_path(self: "File", path: str = "") -> None:
        """Set file absolute path."""
        self.file["abs_path"] = path

    def set_file_name(self: "File", path: str = "") -> None:
        """Set file name."""
        self.file["file_name"] = get_path_basename(path)

    def set_file_type(self: "File", path: str = "") -> None:
        """Set the file type."""
        ext = get_file_extension_from_path(path)
        self.file["type"] = file_types.get(ext, UNKNOWN)

    def set_file_metadata(self: "File", data: dict) -> None:
        """Set file metadata."""
        self.file["metadata"] = data

    def set_file_raw_data(self: "File", data: str) -> None:
        """Set file raw data."""
        self.file["raw"] = data
