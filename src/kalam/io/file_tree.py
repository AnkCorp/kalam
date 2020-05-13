"""File tree module."""

from sys import exit
from typing import List, TypedDict

from click import secho

import kalam.constants.default_dirs as default_dirs
from kalam.utils.path import (
    dir_in_ignore_list,
    generate_path,
    path_diff,
    path_exist,
    pwd,
    split_path_directories,
    tree,
)


class FileTreeDict(TypedDict):
    """Dictionary shape for File Tree Dictionary."""

    identifiers: List[str]
    url: str
    files: List[str]
    assets: List[str]


class FileTree:
    """Create a list of file which has to be processed."""

    def __init__(self: "FileTree") -> None:
        """Initialize."""
        # For data pack
        self.file_tree: List[FileTreeDict] = []

        # For watcher
        self.file_list: List[str] = []

    def get_all_files_in_dir(self: "FileTree", dir: str) -> List[str]:
        """Returns all the files in the directory."""
        file_list: List[str] = []
        for root, _, files in tree(dir):
            for file in files:
                file_list.append(generate_path([root, file]))
        return file_list

    def process_dir(self: "FileTree", dir: str, process_assets: bool = False) -> None:
        """Process files in dir."""
        dir_to_ignore: List[str] = []

        for root, dirs, files in tree(dir):
            assets: List[str] = []

            if not dir_in_ignore_list(root, dir_to_ignore):
                if len(files) != 0:
                    file_list = [generate_path([root, f]) for f in files]
                    self.file_list = self.file_list + file_list

                    if bool(dirs) and process_assets:
                        dir_to_ignore = dir_to_ignore + [
                            generate_path([root, d]) for d in dirs
                        ]
                        if "assets" in dirs:
                            assets = self.get_all_files_in_dir(
                                generate_path([root, "assets"])
                            )

                    identifiers = split_path_directories(path_diff(pwd(), root))
                    self.file_tree.append(
                        {
                            "identifiers": identifiers,
                            "url": generate_path(identifiers),
                            "assets": assets,
                            "files": file_list,
                        }
                    )

    def create_file_tree(self: "FileTree", extra_dirs: List[str]) -> None:
        """Create file tree."""
        root = pwd()
        if self.check_config_file():
            self.process_dir(generate_path([root, default_dirs.CONTENTS]), True)
            self.process_dir(generate_path([root, default_dirs.CONTENTS_TEMPLATES]))
            self.process_dir(generate_path([root, default_dirs.DATA]))
            self.process_dir(generate_path([root, default_dirs.GENERATORS]))

            for dir in extra_dirs:
                self.process_dir(generate_path([root, dir]))

    def check_config_file(self: "FileTree") -> bool:
        """Check whether kalam.toml exist in present directory or not."""
        path = generate_path([pwd(), "kalam.toml"])

        # check whether kalam.toml exist in current path or not. If not then exit.
        if not (path_exist(path)):
            secho("kalam.config not found", fg="red")
            exit()
        return True

    def get_tree(self: "FileTree") -> List[FileTreeDict]:
        """Send the file tree."""
        return self.file_tree

    def get_list(self: "FileTree") -> List[str]:
        """Send the file list."""
        return self.file_list
