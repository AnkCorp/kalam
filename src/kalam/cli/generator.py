"""Generator command in CLI."""

import click

from kalam.generators import PDFGenerator, TexGenerator, WebGenerator


@click.command(
    name="new", help="Create new project [project name is required]",
)
@click.argument("project_name", required=True)
@click.option("--pdf", "-p", is_flag=True, help="Create PDF document")
@click.option("--tex", "-t", is_flag=True, help="Create TEX document")
def create_new_project(project_name: str, pdf: bool, tex: bool) -> None:
    """Create new project. Project name is required."""
    click.secho("Creating new project", fg="green")

    if pdf:
        click.secho("Type: PDF")
        PDFGenerator(project_name)

    elif tex:
        click.secho("Type: Tex")
        TexGenerator(project_name)

    # Default
    else:
        click.secho("Type: Web [Default]")
        WebGenerator(project_name)
