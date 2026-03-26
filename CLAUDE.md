# CLAUDE.md

## What is this project?

`create-python` (v0.2.0) is a CLI tool that scaffolds modern Python projects with an opinionated setup: uv, ruff, pytest, and optional CI/CD. Built with Typer + Cookiecutter.

## Project structure

```
create_python/
  cli.py              # Typer CLI entry point (main command + flags)
  scaffold.py         # Core logic: slugify, to_snake_case, create_project()
  __init__.py          # Version string
  template/
    cookiecutter.json  # Template variables and defaults
    hooks/
      post_gen_project.py  # Removes unused CI files after generation
    {{cookiecutter.project_slug}}/  # The actual template
tests/
  test_cli.py          # 12 tests — CLI behavior via CliRunner
  test_scaffold.py     # 2 tests — slugify/snake_case unit tests
```

## Entry point

`create_python.cli:app` (registered as `create-python` in pyproject.toml scripts)

## CLI flags

| Flag | Short | Default | Description |
|------|-------|---------|-------------|
| `--python-version` | `-p` | `3.13` | Python version |
| `--output-dir` | `-o` | `.` | Where to create the project |
| `--author` | `-a` | `""` | Author name |
| `--description` | `-d` | `""` | Project description |
| `--use-ci` | | `""` | `github` or `gitlab` |
| `--git` | | `false` | Init git repo + initial commit |
| `--install` | | `false` | Run `uv sync` |

## Dev commands

```bash
make install        # uv sync
make test           # uv run pytest
make cov            # pytest --cov --cov-report=term-missing
make check          # ruff check .
make format         # ruff check --fix + ruff format
make format-check   # check only, no writes
```

## Tools and config

- **Linter/formatter:** ruff (line-length=120, rules: E,F,I,N,W,UP,B,SIM,RUF)
- **ruff excludes** `create_python/template` (template code has Jinja syntax)
- **Testing:** pytest + pytest-cov, test path: `tests/`
- **Pre-commit:** ruff hooks (lint with --fix + format)
- **Build:** hatchling
- **Python:** >=3.11

## Key design decisions

- Cookiecutter template lives inside the package (`create_python/template/`)
- `post_gen_project.py` hook deletes CI files that don't match the chosen provider
- Tests mock subprocess calls (git init, uv sync) — no real subprocesses in tests
- Generated projects use MIT license, uv, ruff, pytest, and hatchling
