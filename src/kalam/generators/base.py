"""This module contain generator class."""

import toml

from kalam.utils.path import (
    create_file_current,
    generate_path,
    get_path_basename,
    mkdir_current,
)


class Generator:
    """Base generator class."""

    def __init__(self: "Generator", filename_with_path: str = "") -> None:
        """Initialize generator instance."""

        # File to create
        self.file_to_create = []

        # Directory to create
        self.dir_to_create = [
            "contents",
            "contents_templates",
            "data",
            "generators/web",
        ]

        # Default configuration
        self.config = {
            "title": "",
            "languageCode": "en-US",
            "baseURL": "http://localhost:8080",
        }

        # If filename_with_path is not empty then call setup
        if filename_with_path != "":
            self.setup(filename_with_path)

    def setup(self: "Generator", filename_with_path: str) -> None:
        """Setup the project."""
        self.filename_with_path = filename_with_path
        self.input_config_details()
        self.init_file_to_create()
        self.create_directory()
        self.create_files()

    def init_file_to_create(self: "Generator") -> None:
        """initialize file to create."""
        config = toml.dumps(self.config)
        self.file_to_create.append({"filename": "kalam.toml", "write": config})

    def create_directory(self: "Generator") -> None:
        """Create direcotry."""
        filename_with_path = self.filename_with_path
        try:
            mkdir_current(filename_with_path)
            for path in self.dir_to_create:
                mkdir_current(generate_path([filename_with_path, path]))

        except OSError as e:
            print(
                "[Generator Error] Unable to create directory. Given path: {}".format(
                    filename_with_path
                )
            )

            print("[Reason] {}".format(e.strerror))

    def create_files(self: "Generator") -> None:
        """Create files."""
        filename_with_path = self.filename_with_path
        try:
            for item in self.file_to_create:
                create_file_current(
                    generate_path([filename_with_path, item["filename"]]),
                    write=item["write"],
                )

        except OSError as e:
            print("[Generator Error] Unable to create files. {}")
            print("[Reason] {}".format(e.strerror))

    def input_config_details(self: "Generator") -> None:
        """Take config details from user."""
        filename = get_path_basename(self.filename_with_path)
        print("Press enter to choose default")

        res = input("Title (Default: {}): ".format(filename))
        if res == "":
            self.config["title"] = filename
        else:
            self.config["title"] = res

        res = input("Base URL (Default: {}): ".format(self.config["baseURL"]))
        if res != "":
            self.config["baseURL"] = res

        res = input("Language Code (Default: {}): ".format(self.config["languageCode"]))
        if res != "":
            self.config["languageCode"] = res

        print(self.config)
