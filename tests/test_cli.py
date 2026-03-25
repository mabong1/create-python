"""Tests for the create-python CLI."""

from unittest.mock import patch

from typer.testing import CliRunner

from create_python.cli import app

runner = CliRunner()


def test_help():
    result = runner.invoke(app, ["--help"])
    assert result.exit_code == 0
    assert "create a new python project" in result.output.lower()


def test_create_project(tmp_path):
    result = runner.invoke(app, ["test-project", "--output-dir", str(tmp_path)])
    assert result.exit_code == 0

    project_dir = tmp_path / "test-project"
    assert project_dir.exists()
    assert (project_dir / "pyproject.toml").exists()
    assert (project_dir / "test_project" / "__init__.py").exists()
    assert (project_dir / "test_project" / "main.py").exists()
    assert (project_dir / "tests" / "test_main.py").exists()
    assert (project_dir / ".gitignore").exists()
    assert (project_dir / "README.md").exists()


def test_create_project_custom_python_version(tmp_path):
    result = runner.invoke(app, ["my-app", "--output-dir", str(tmp_path), "--python-version", "3.12"])
    assert result.exit_code == 0

    pyproject = (tmp_path / "my-app" / "pyproject.toml").read_text()
    assert ">=3.12" in pyproject


def test_create_project_with_author(tmp_path):
    result = runner.invoke(
        app,
        ["my-app", "--output-dir", str(tmp_path), "--author", "John Doe"],
    )
    assert result.exit_code == 0

    pyproject = (tmp_path / "my-app" / "pyproject.toml").read_text()
    assert "John Doe" in pyproject


def test_create_project_with_git(tmp_path):
    with patch("create_python.scaffold.subprocess.run") as mock_run:
        result = runner.invoke(app, ["my-app", "--output-dir", str(tmp_path), "--git"])
        assert result.exit_code == 0

    project_path = tmp_path / "my-app"
    mock_run.assert_any_call(["git", "init"], cwd=project_path, capture_output=True, check=True)
    mock_run.assert_any_call(
        ["uv", "run", "pre-commit", "install"],
        cwd=project_path,
        capture_output=True,
        check=True,
    )
    mock_run.assert_any_call(["git", "add", "."], cwd=project_path, capture_output=True, check=True)
    mock_run.assert_any_call(
        ["git", "commit", "-m", "Initial commit"],
        cwd=project_path,
        capture_output=True,
        check=True,
    )


def test_create_project_with_install(tmp_path):
    with patch("create_python.scaffold.subprocess.run") as mock_run:
        result = runner.invoke(app, ["my-app", "--output-dir", str(tmp_path), "--install"])
        assert result.exit_code == 0

    project_path = tmp_path / "my-app"
    mock_run.assert_any_call(["uv", "sync"], cwd=project_path, capture_output=True, check=True)


def test_create_project_no_subprocess_by_default(tmp_path):
    with patch("create_python.scaffold.subprocess.run") as mock_run:
        result = runner.invoke(app, ["my-app", "--output-dir", str(tmp_path)])
        assert result.exit_code == 0

    mock_run.assert_not_called()
