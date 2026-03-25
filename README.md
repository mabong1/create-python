# create-python

CLI tool to scaffold modern Python projects with batteries included.

## Features

Generated projects come pre-configured with:

- **[uv](https://docs.astral.sh/uv/)** -- fast Python package manager
- **[ruff](https://docs.astral.sh/ruff/)** -- linter
- **[pytest](https://docs.pytest.org/)** -- testing framework
- **[hatchling](https://hatch.pypa.io/)** -- modern build backend
- **[pre-commit](https://pre-commit.com/)** -- git hooks for automated checks
- Flat package layout
- `pyproject.toml` with all tooling configured
- `Makefile` with common development commands

## Installation

```bash
# With uv (recommended)
uv tool install git+https://github.com/mabong1/create-python.git

# With pipx
pipx install git+https://github.com/mabong1/create-python.git
```

To upgrade to the latest version:

```bash
uv tool upgrade create-python
```

To uninstall:

```bash
uv tool uninstall create-python
```

## Usage

```bash
# Create a new project
create-python my-project

# Specify Python version
create-python my-project --python-version 3.12

# With author and description
create-python my-project --author "Jane Doe" --description "My awesome project"

# Skip git init and dependency install
create-python my-project --no-git --no-install
```

## Options

| Option | Short | Default | Description |
|---|---|---|---|
| `--python-version` | `-p` | `3.13` | Python version for the project |
| `--output-dir` | `-o` | `.` | Parent directory for the project |
| `--author` | `-a` | | Author name |
| `--description` | `-d` | | Project description |
| `--git` | | `false` | Init a git repository |
| `--install` | | `false` | Automagically run `uv sync` |

## Generated project structure

```
my-project/
├── pyproject.toml          # Project config with all tooling
├── Makefile                # Development commands
├── README.md
├── .gitignore
├── .python-version
├── .pre-commit-config.yaml
├── my_project/
│   ├── __init__.py
│   └── main.py
└── tests/
    ├── __init__.py
    └── test_main.py
```

## Development

```bash
# Clone and install
git clone https://github.com/mabong1/create-python.git
cd create-python
make install

# Install git hooks
uv run pre-commit install

# Run tests
make test

# Run tests with coverage
make cov

# Lint
make check

# Format code
make format

# Check formatting without modifying
make format-check
```
