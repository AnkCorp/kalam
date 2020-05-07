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

    def set_file_info_for_packing(self: "File", data: dict) -> None:
        """Set file info for packing."""
        self.file["path"] = data["path"]
        self.file["filename"] = get_path_basename(data["path"])
        self.file["filetype"] = file_types.get(
            get_file_extension_from_path(data["path"]), UNKNOWN
        )
        self.file["metadata"] = data["metadata"]

    def set_file_raw_data(self: "File", data: str) -> None:
        """Set raw data to the file."""
        self.file["raw"] = data

    def file_path(self: "File") -> str:
        """Return the path of the file."""
        if "path" in self.file:
            return self.file["path"]
        else:
            raise KeyError("[File Error] Path is not set.")

    def filetype(self: "File") -> str:
        """Return the path of the file."""
        if "filetype" in self.file:
            return self.file["filetype"]
        else:
            raise KeyError("[File Error] File type is not set.")
