"""Packer class which pack the files."""

from typing import List

from kalam.io.data_pack import DataPack
from kalam.io.file_tree import FileTree
from kalam.io.files import File
from kalam.io.readers import Reader
from kalam.utils.dict import dict_all_value_in_list


class Packer:
    """Packer class."""

    def __init__(self: "Packer") -> None:
        """Initialize packer instance."""
        self.packer: List[DataPack] = []
        self.file_tree = FileTree()
        self.dir_to_read = ["contents", "contents_templates", "data", "generators"]

    def create_tree(self: "Packer") -> None:
        """Run file tree."""
        self.file_tree.create_file_tree()

    def read_files_from_dirs(self: "Packer") -> None:
        """Read files from the dirs."""
        for dir in self.dir_to_read:
            if dir in self.file_tree.file_tree:
                files = dict_all_value_in_list(self.file_tree.get_dir_dict(dir))
                file_instances: List[File] = []
                for file in files:
                    reader = Reader()
                    reader.init_file_for_packing(file)
                    file_instances.append(reader.get_file_instance())

                for instance in file_instances:
                    for data_pack in self.packer:
                        if [dir, instance.filetype()] == data_pack.identifiers:
                            data_pack.add_unit(instance)
                            break
                    else:
                        new_data_pack = DataPack()
                        new_data_pack.add_identifier(dir)
                        new_data_pack.add_identifier(instance.filetype())
                        new_data_pack.add_unit(instance)
                        self.packer.append(new_data_pack)

    def pack(self: "Packer") -> None:
        """Pack all files."""
        self.create_tree()
        self.read_files_from_dirs()
