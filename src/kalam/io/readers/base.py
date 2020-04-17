"""Base module for reader and file."""

from kalam.io.files.base import File
from kalam.utils.path import (
    generate_path,
    get_abs_path,
    get_path_accessed_time,
    get_path_created_time,
    get_path_modified_time,
    path_exist,
)


class Reader:
    """Reader class."""

    def __init__(self: "Reader") -> None:
        """Initialize reader instance."""
        self.reader = dict()
        self.file = File()

    def open(self: "Reader", path: str) -> None:
        """Open file."""
        abs_path = get_abs_path(path)
        try:
            if path_exist(abs_path):
                with open(abs_path) as file_data:
                    self.file.set_file_info(
                        {
                            "path": abs_path,
                            "raw": file_data.read(),
                            "metadata": {
                                "created_at": get_path_created_time(abs_path),
                                "accessed_at": get_path_accessed_time(abs_path),
                                "modified_at": get_path_modified_time(abs_path),
                            },
                        }
                    )
            else:
                raise OSError

        except OSError:
            print("[Reader Error] Path doesn't exist. path: {}".format(abs_path))

        except IOError:
            print("[Reader Error] Could not read file at: {}".format(abs_path))


path = generate_path(["..", "..", "__init__.py"])

r = Reader()
r.open(path)

print(r.file.file)
