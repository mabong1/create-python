"""Project scaffolding logic using cookiecutter."""

import subprocess
from pathlib import Path

from cookiecutter.main import cookiecutter as run_cookiecutter
from rich.console import Console

console = Console()

TEMPLATE_DIR = Path(__file__).parent / "template"


def slugify(name: str) -> str:
    """Convert project name to kebab-case slug."""
    return name.lower().replace(" ", "-").replace("_", "-")


def to_snake_case(name: str) -> str:
    """Convert project name to snake_case package name."""
    return name.lower().replace("-", "_").replace(" ", "_")


def create_project(
    *,
    project_name: str,
    python_version: str,
    output_dir: str,
    author: str,
    description: str,
    ci: str,
    init_git: bool,
    run_install: bool,
) -> Path:
    """Scaffold a new Python project."""
    project_slug = slugify(project_name)
    package_name = to_snake_case(project_name)

    context = {
        "project_name": project_name,
        "project_slug": project_slug,
        "package_name": package_name,
        "python_version": python_version,
        "author": author,
        "description": description or f"A Python project: {project_name}",
        "ci": ci,
    }

    console.print(f"[bold]Creating project:[/] {project_slug}")

    project_dir = run_cookiecutter(
        str(TEMPLATE_DIR),
        output_dir=output_dir,
        no_input=True,
        extra_context=context,
    )
    project_path = Path(project_dir)

    if init_git:
        console.print("[dim]Initializing git repository...[/]")
        subprocess.run(["git", "init", "-b", "main"], cwd=project_path, capture_output=True, check=True)
        subprocess.run(
            ["uv", "run", "pre-commit", "install"],
            cwd=project_path,
            capture_output=True,
            check=True,
        )
        subprocess.run(["git", "add", "."], cwd=project_path, capture_output=True, check=True)
        subprocess.run(
            ["git", "commit", "-m", "Initial commit"],
            cwd=project_path,
            capture_output=True,
            check=True,
        )

    if run_install:
        console.print("[dim]Installing dependencies with uv...[/]")
        subprocess.run(["uv", "sync"], cwd=project_path, capture_output=True, check=True)

    return project_path
