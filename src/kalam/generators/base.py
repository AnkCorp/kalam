"""This module contain generator class."""

from getpass import getuser
from sys import exit

from click import BOOL, prompt, secho
import toml


from kalam.utils.path import (
    create_file_current,
    generate_path,
    get_path_basename,
    mkdir_current,
    path_exist,
    pwd,
)


class Generator:
    """Base generator class."""

    def __init__(self: "Generator", type: str, filename_with_path: str = "") -> None:
        """Initialize generator instance."""
        # File to create
        self.file_to_create = []

        # Directory to create
        self.dir_to_create = [
            "contents",
            "contents_templates",
            "data",
            f"generators/{type}",
        ]

        # Default configuration.
        self.config = {"title": ""}

        # List of default questions ask to update config file.
        self.config_questions = [
            {
                "question": "Author",
                "property": "author",
                "default": getuser(),
                "type": str,
            },
            {
                "question": "Git Enable (Yes/No)",
                "property": "git_enable",
                "default": "Yes",
                "type": BOOL,
            },
        ]

        # If filename_with_path is not empty then call setup
        if filename_with_path != "":
            self.setup(filename_with_path)

    def setup(self: "Generator", filename_with_path: str) -> None:
        """Setup the project."""
        self.filename_with_path = filename_with_path
        if not path_exist(filename_with_path):
            self.input_config_details()
            self.init_file_to_create()
            self.create_directory()
            self.create_files()
            if "git_enable" in self.config and self.config["git_enable"]:
                self.setup_git()
        else:
            secho(
                "[Error] Path: '{}' already exists.".format(
                    generate_path([pwd(), filename_with_path])
                ),
                fg="red",
            )

    def init_file_to_create(self: "Generator") -> None:
        """Initialize file to create."""
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
            secho(
                "[Generator] Process failed.\n[Reason] {}".format(
                    filename_with_path, e.strerror
                ),
                fg="red",
            )

            # Terminate the program
            exit()

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
            secho(
                "[Generator] Process failed while writing on {}\n[Reason] {}".format(
                    item["filename"], e.strerror
                ),
                fg="red",
            )

            # Terminate the program
            exit()

    def input_config_details(self: "Generator") -> None:
        """Take config details from user."""
        filename = get_path_basename(self.filename_with_path)
        secho("Press 'Enter' to choose default.", fg="yellow")

        self.config["title"] = prompt("Title", default=filename)

        for question in self.config_questions:
            self.config[question["property"]] = prompt(
                question["question"],
                default=question["default"],
                type=question["type"] if "type" in question else str,
            )

    def setup_git(self: "Generator") -> None:
        """Initialize directory as git repo."""
        from git import Repo

        filename_with_path = self.filename_with_path
        Repo.init(filename_with_path)
