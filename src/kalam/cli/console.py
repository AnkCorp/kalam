"""Command-line interface."""

import click

from kalam.cli.build import build
from .. import __version__


@click.group()
@click.version_option(version=__version__)
def main() -> None:
    """Kalam console."""
    pass


main.add_command(build)
