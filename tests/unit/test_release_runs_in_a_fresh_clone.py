# Copyright 2021-2026 ONDEWO GmbH
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
"""
The ``release`` target works in the fresh clone ondewo-vtsi-api's ``release_client`` makes, and tests first.

The fresh clone has no ``.venv`` and the release host has no conda environment for this repository, so every
tool the release runs must come from ``uv sync`` of ``uv.lock``. And nothing may be pushed, tagged or published
before the unit suite passed.
"""

import re
from pathlib import Path
from typing import List

REPO_ROOT: Path = Path(__file__).resolve().parents[2]
MAKEFILE: str = (REPO_ROOT / "Makefile").read_text(encoding="utf-8")


def _recipe(target: str) -> List[str]:
    """
    Return the recipe lines of a make target.

    Args:
        target (str):
            The target name.

    Returns:
        List[str]:
            Its tab-indented recipe lines, stripped.
    """
    match = re.search(rf"^{re.escape(target)}:.*\n((?:\t.*\n)+)", MAKEFILE, flags=re.MULTILINE)
    assert match is not None, target
    return [line.strip() for line in match.group(1).splitlines()]


def test_the_release_needs_no_conda() -> None:
    """Verify no recipe activates a conda environment on the release path."""
    assert "activate ondewo-vtsi-client-python" not in "\n".join(_recipe("release"))


def test_pre_commit_runs_in_a_synced_project_environment() -> None:
    """Verify pre-commit runs through ``uv run --no-sync`` after ``install_dev_environment`` synced the .venv."""
    assert re.search(r"^precommit_hooks_run_all_files:\s*install_dev_environment\b", MAKEFILE, re.MULTILINE)
    assert _recipe("precommit_hooks_run_all_files") == ["uv run --no-sync pre-commit run --all-files"]
    assert _recipe("install_dev_environment") == ["uv sync --extra dev --frozen --python 3.12"]


def test_the_release_tests_before_it_pushes_tags_or_publishes() -> None:
    """Verify ``make test`` runs before the first push, branch, tag, GitHub release and PyPI upload."""
    recipe: List[str] = _recipe("release")
    first_test: int = recipe.index("make test")
    for step in (
        "git push",
        "make create_release_branch",
        "make create_release_tag",
        "make release_to_github_via_docker",
        "make push_to_pypi_via_docker",
    ):
        assert first_test < recipe.index(step), step
    assert "uv run --no-sync pytest tests/unit -q \\" in _recipe("test")
