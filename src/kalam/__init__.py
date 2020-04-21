"""The Kalam project."""
try:
    from importlib.metadata import version, PackageNotFoundError  # type: ignore
except ImportError:  # pragma: no cover
    from importlib_metadata import version, PackageNotFoundError  # type: ignore


try:
    __version__ = version(__name__)
except PackageNotFoundError:  # pragma: no cover
    __version__ = "unknown"

from kalam import io  # noqa
from kalam import jobs  # noqa
from kalam import pipeline  # noqa
from kalam import generators  # noqa
