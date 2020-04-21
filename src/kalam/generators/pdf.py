"""PDF generator class."""

from kalam.generators import Generator


class PDFGenerator(Generator):
    """PDF Generator class."""

    def __init__(self: "PDFGenerator", filename_with_path: str = "") -> None:
        """Initialize instace of PDFGenerator."""
        super().__init__("pdf")

        if filename_with_path != "":
            self.setup(filename_with_path)
