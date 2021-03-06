"""Command-line interface."""

import click

from .. import __version__


@click.command()
@click.version_option(version=__version__)
def main() -> None:
    """Kalam console."""
    click.secho("Hello World!", fg="green")
