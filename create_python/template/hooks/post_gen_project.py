"""Post-generation hook to remove unused CI files."""

import os
import shutil

ci = "{{ cookiecutter.ci }}"

if ci != "github":
    shutil.rmtree(os.path.join(os.getcwd(), ".github"), ignore_errors=True)

if ci != "gitlab":
    gitlab_ci = os.path.join(os.getcwd(), ".gitlab-ci.yml")
    if os.path.exists(gitlab_ci):
        os.remove(gitlab_ci)
