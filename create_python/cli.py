"""CLI entry point for create-python."""

from typing import Annotated

import typer
from rich.console import Console

from create_python.scaffold import create_project

app = typer.Typer(
    name="create-python",
    help="Scaffold a modern Python project with uv, ruff and pytest.",
    add_completion=False,
)
console = Console()


@app.command()
def main(
    project_name: Annotated[str, typer.Argument(help="Name of the project to create")],
    python_version: Annotated[str, typer.Option("--python-version", "-p", help="Python version")] = "3.13",
    output_dir: Annotated[str, typer.Option("--output-dir", "-o", help="Parent directory for the project")] = ".",
    author: Annotated[str, typer.Option("--author", "-a", help="Author name")] = "",
    description: Annotated[str, typer.Option("--description", "-d", help="Project description")] = "",
    git: Annotated[bool, typer.Option("--git", help="Init git repository")] = False,
    install: Annotated[bool, typer.Option("--install", help="Run uv sync")] = False,
) -> None:
    """Create a new Python project."""
    project_path = create_project(
        project_name=project_name,
        python_version=python_version,
        output_dir=output_dir,
        author=author,
        description=description,
        init_git=git,
        run_install=install,
    )
    console.print(f"\n[bold green]Project created at:[/] {project_path}")
    console.print("\n[bold]Next steps:[/]")
    console.print(f"  cd {project_path.name}")
    if install:
        console.print("  uv sync")
    console.print("  uv run pytest")
