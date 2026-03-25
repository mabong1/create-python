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
    use_ci: Annotated[str, typer.Option("--use-ci", help="Add CI workflow (github or gitlab)")] = "",
    git: Annotated[bool, typer.Option("--git", help="Init git repository")] = False,
    install: Annotated[bool, typer.Option("--install", help="Run uv sync")] = False,
) -> None:
    """Create a new Python project."""
    if use_ci and use_ci not in ("github", "gitlab"):
        console.print("[bold red]Error:[/] --use-ci must be 'github' or 'gitlab'")
        raise typer.Exit(code=1)

    project_path = create_project(
        project_name=project_name,
        python_version=python_version,
        output_dir=output_dir,
        author=author,
        description=description,
        ci=use_ci or "none",
        init_git=git,
        run_install=install,
    )
    console.print(f"\n[bold green]Project created at:[/] {project_path}")
    console.print("\n[bold]Next steps:[/]")
    console.print(f"  cd {project_path.name}")
    if install:
        console.print("  uv sync")
    console.print("  uv run pytest")
