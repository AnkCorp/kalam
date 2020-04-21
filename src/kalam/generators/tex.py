"""Tex generator class."""

from kalam.generators import Generator


class TexGenerator(Generator):
    """Tex Generator class."""

    def __init__(self: "TexGenerator", filename_with_path: str = "") -> None:
        """Initialize instace of TexGenerator."""
        super().__init__("tex")

        if filename_with_path != "":
            self.setup(filename_with_path)
