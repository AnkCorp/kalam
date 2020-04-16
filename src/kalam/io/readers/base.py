"""Base module for reader and file."""

from kalam.utils.file_tool import (
    # generate_path,
    get_abs_path,
    get_file_metadata,
    get_file_type,
    get_path_basename,
)


class File:
    """File class."""

    def __init__(self: "File") -> None:
        """Initialize the file object."""
        self.file = dict()

    def set_file_info(self: "File", info: dict) -> None:
        """Set file info."""
        self.file = info

    def get_file_info(self: "File") -> "File":
        """Return the file info."""
        return self.file


class Reader(File):
    """Reader class."""

    def open(self: "Reader", path: str) -> None:
        """Open file."""
        abs_path_of_file = get_abs_path(__file__, path)
        try:
            with open(abs_path_of_file) as f:
                file_info = {
                    "path": abs_path_of_file,
                    "file_name": get_path_basename(abs_path_of_file),
                    "type": get_file_type(abs_path_of_file),
                    "metadata": get_file_metadata(abs_path_of_file),
                    "raw": f.read(),
                }
                self.set_file_info(file_info)
                f.close()

        except IOError:
            print("Could not read file at: {}".format(abs_path_of_file))


# path = generate_path(["..", "..", "__init__.py"])

# r = Reader()
# r.open(path)
# print(r.get_file_info())
