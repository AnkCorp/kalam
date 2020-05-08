"""Data Package class."""

from typing import Any, List
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

    def add_identifier(self: "DataPack", identifier: str) -> None:
        """Adds an identifier."""
        if identifier not in self.identifiers:
            self.identifiers.append(identifier)

    def add_descriptor(self: "DataPack", descriptor: str) -> None:
        """Adds a descriptor."""
        if descriptor not in self.descriptors:
            self.descriptors.append(descriptor)

    def add_unit(self: "DataPack", unit: Any) -> None:
        """Adds a Data Unit."""
        if unit not in self.units:
            self.units.append(unit)
