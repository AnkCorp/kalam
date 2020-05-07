"""Build command in CLI."""

import click

from kalam.io.packer import Packer
from kalam.jobs import Job
from kalam.pipeline import Pipeline, Runner


@click.command()
def build() -> None:
    """Test command."""
    pipeline = Pipeline()
    job = Job()
    runner = Runner()
    pipeline.add_job(job)
    pipeline.runner = runner
    click.secho(f"Hahaha {pipeline}", fg="yellow")
    pipeline.run()
    click.secho(f"Did it!!!", fg="green")

    packer = Packer()
    packer.pack()
