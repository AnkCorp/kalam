"""File tree module."""

from sys import exit
from typing import Dict, Union

from click import secho

from kalam.utils.path import (
    generate_path,
    path_diff,
    path_exist,
    pwd,
    split_path_directories,
    tree,
)


class FileTreeDict(Dict):
    """Dictionary shape for File Tree Dictionary."""

    str: Union[str, Dict[str, str]]


class FileTree:
    """Create a list of file which has to be processed."""

    def __init__(self: "FileTree") -> None:
        """Initialize."""
        self.file_tree = FileTreeDict()
        # self.file_list = list()

    def create_file_tree(self: "FileTree") -> None:
        """Create file tree."""
        path = pwd()

        if self.check_config_file():
            for root, dirs, files in tree(path):
                current = FileTreeDict()
                # Traversing and storing all files in current directory.
                for f in files:
                    p = generate_path([root, f])
                    current[f] = p
                    # self.file_list.append(p)

                # Traversing and storing all directories in current directory.
                for d in dirs:
                    current[d] = FileTreeDict()

                # Getting the key as a list.
                paths = split_path_directories(path_diff(path, root))

                # Current dictionary to update.
                current_dict = self.file_tree

                # Get current key to update.
                for p in paths:
                    current_dict = current_dict[p]

                current_dict.update(current)

    def check_config_file(self: "FileTree") -> bool:
        """Check whether kalam.toml exist in present directory or not."""
        path = generate_path([pwd(), "kalam.toml"])

        # check whether kalam.toml exist in current path or not. If not then exit.
        if not (path_exist(path)):
            secho("kalam.config not found", fg="red")
            exit()
        return True

    def get_dir_dict(self: "FileTree", key: str) -> FileTreeDict:
        """Return the value/path of the dir."""
        return self.file_tree[key]

    def get_file_tree(self: "FileTree") -> FileTreeDict:
        """Return the file tree dictionary."""
        return self.file_tree
