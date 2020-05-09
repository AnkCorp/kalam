"""Data Package class."""

from typing import List
import uuid

from kalam.io.files import File


class DataPack:
    """Creates a data package."""

    def __init__(self: "DataPack") -> None:
        """Initialize a data package."""
        self.identifiers: List[str] = []
        self.descriptors: List[str] = []
        self.units: List[File] = []
        self.id: uuid.UUID = uuid.uuid4()
        self.assets: List[File] = []
        self.url: str = ""

    def add_identifiers(self: "DataPack", identifiers: List[str]) -> None:
        """Adds a list identifiers."""
        self.identifiers = self.identifiers + identifiers

    def add_descriptors(self: "DataPack", descriptors: List[str]) -> None:
        """Adds a list descriptors."""
        self.descriptors = self.descriptors + descriptors

    def add_units(self: "DataPack", units: List[File]) -> None:
        """Adds a list Data Units."""
        self.units = self.units + units

    def add_assets(self: "DataPack", assets: List[File]) -> None:
        """Adds a list of assets."""
        self.assets = self.assets + assets

    def set_url(self: "DataPack", url: str) -> None:
        """Set the url."""
        self.url = url
