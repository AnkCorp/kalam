"""Packer class which pack the files."""

from typing import List

from kalam.io.data_pack import DataPack
from kalam.io.file_tree import FileTree
from kalam.io.files import File
from kalam.io.readers import Reader
from kalam.utils.path import generate_path


class Packer:
    """Packer class."""

    def __init__(self: "Packer") -> None:
        """Initialize packer instance."""
        self.file_packs: List[DataPack] = []
        self.file_tree = FileTree()
        self.extra_dirs: List[str] = []

    def create_tree(self: "Packer") -> None:
        """Run file tree."""
        self.file_tree.create_file_tree(self.extra_dirs)

    def get_file_object(self: "Packer", file_list: List[str]) -> List[File]:
        """Return the file object after reading the files."""
        file_objects: List[File] = []
        for file in file_list:
            r = Reader()
            r.init_file_for_packing(file)
            file_objects.append(r.get_file_instance())
        return file_objects

    def pack_files_from_tree(self: "Packer") -> None:
        """Pack the file in data pack using file tree."""
        for file_tree in self.file_tree.get_tree():
            # Get file objects
            file_objects = self.get_file_object(file_tree["files"])

            # Get assets object
            assets_objects = self.get_file_object(file_tree["assets"])

            # Set data into data pack format
            data_pack = DataPack()
            data_pack.add_assets(assets_objects)
            data_pack.add_units(file_objects)
            data_pack.add_identifiers(file_tree["identifiers"])
            data_pack.set_url(generate_path(file_tree["identifiers"]))

            # append data to file packs
            self.file_packs.append(data_pack)

    def pack(self: "Packer") -> None:
        """Pack all files."""
        self.create_tree()
        self.pack_files_from_tree()
