"""This module contain file class."""

from typing import TypedDict

from kalam.constants.file_type import file_types, UNKNOWN
from kalam.utils.path import (
    get_file_extension_from_path,
    get_path_basename,
)


class MetadataDict(TypedDict):
    """Dictionary shape for Metadata."""

    created_at: float
    accessed_at: float
    modified_at: float


class FileDictArg(TypedDict):
    """Dictionary shape for File argument."""

    path: str
    metadata: dict


class FileDict(FileDictArg):
    """Dictionary shape for File."""

    filename: str
    filetype: str
    raw: str


class File:
    """Base class for file."""

    def __init__(self: "File") -> None:
        """Initialize file instance."""
        self.file: FileDict = {
            "path": "",
            "raw": "",
            "metadata": {"created_at": "", "accessed_at": "", "modified_at": ""},
            "filename": "",
            "filetype": "",
        }

    def set_file_info_for_packing(self: "File", data: FileDictArg) -> None:
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

    def filepath(self: "File") -> str:
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

    def filename(self: "File") -> str:
        """Return the name of the file."""
        if "filetype" in self.file:
            return self.file["filename"]
        else:
            raise KeyError("[File Error] File name is not set.")
