"""
test.test_template
"""

import os
import subprocess
from typing import Sequence

import pytest


def test_project_path(cookies):
    """
    Test project path
    """

    project = cookies.bake()
    assert project.exit_code == 0
    assert project.exception is None
    assert os.path.basename(project.project_path) == "my-python-package"
    assert os.path.isdir(project.project_path)


def run(args: Sequence[str], dirpath: os.PathLike) -> subprocess.CompletedProcess:
    """
    Helper for running commands
    """

    completed_process = subprocess.run(
        args=args,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        cwd=dirpath,
        encoding="utf-8",
        check=False,
    )
    print(completed_process.stdout)
    print(completed_process.stderr)
    return completed_process


@pytest.fixture
def project_env_bin_dir(tmp_path):
    """
    Helper which returns Python directory
    """

    env_output = run(["python3", "-m", "venv", "env"], tmp_path)
    assert env_output.returncode == 0
    return os.path.join(tmp_path, "env", "bin")


@pytest.fixture
def baked_with_development_dependencies(cookies, project_env_bin_dir):
    """
    Helper which bakes a cookie, including its optional development dependencies
    """
    # pylint: disable=redefined-outer-name

    result = cookies.bake()
    assert result.exit_code == 0
    pip = os.path.join(project_env_bin_dir, "pip3")
    latest_pip_output = run(
        [pip, "install", "--upgrade", "pip", "setuptools", "tox"], result.project_path
    )
    assert latest_pip_output.returncode == 0
    pip_output = run([pip, "install", "--editable", ".[dev]"], result.project_path)
    assert pip_output.returncode == 0
    return result.project_path


def test_black(baked_with_development_dependencies, project_env_bin_dir):
    """
    Run black on baked cookie
    """
    # pylint: disable=redefined-outer-name

    project_dir = baked_with_development_dependencies
    black = os.path.join(project_env_bin_dir, "black")
    result = run([black, "--check", "--diff", "."], project_dir)
    assert result.returncode == 0


def test_pylint(baked_with_development_dependencies, project_env_bin_dir):
    """
    Run pylint on baked cookie
    """
    # pylint: disable=redefined-outer-name

    project_dir = baked_with_development_dependencies
    pylint = os.path.join(project_env_bin_dir, "pylint")
    result = run(
        [pylint, os.path.join(project_dir, "src"), os.path.join(project_dir, "tests")],
        project_dir,
    )
    assert result.returncode == 0


def test_pytest(baked_with_development_dependencies, project_env_bin_dir):
    """
    Run pytest on baked cookie
    """
    # pylint: disable=redefined-outer-name

    project_dir = baked_with_development_dependencies
    pytest = os.path.join(project_env_bin_dir, "pytest")
    result = run([pytest], project_dir)
    assert result.returncode == 0


def test_tox(baked_with_development_dependencies, project_env_bin_dir):
    """
    Run tox on baked cookie
    """
    # pylint: disable=redefined-outer-name

    project_dir = baked_with_development_dependencies
    tox = os.path.join(project_env_bin_dir, "tox")
    result = run([tox], project_dir)
    assert result.returncode == 0
