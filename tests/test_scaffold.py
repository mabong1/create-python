"""Tests for the scaffolding logic."""

from create_python.scaffold import slugify, to_snake_case


def test_slugify():
    assert slugify("My Project") == "my-project"
    assert slugify("my_project") == "my-project"
    assert slugify("Already-Slug") == "already-slug"


def test_to_snake_case():
    assert to_snake_case("my-project") == "my_project"
    assert to_snake_case("My Project") == "my_project"
    assert to_snake_case("already_snake") == "already_snake"
