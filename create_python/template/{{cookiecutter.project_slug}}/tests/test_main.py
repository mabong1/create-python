from {{ cookiecutter.package_name }}.main import hello


def test_hello():
    assert hello() == "Hello from {{ cookiecutter.project_slug }}!"
