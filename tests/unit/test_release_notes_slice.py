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
The GitHub release body is a SLICE of ``RELEASE.md``, and an empty slice ships silently.

``make build_gh_release`` runs ``gh release create ... -n "$(CURRENT_RELEASE_NOTES)"``, where
``CURRENT_RELEASE_NOTES`` is a perl range over ``RELEASE.md``: from the heading naming the version
in the ``Makefile`` to the next ``*****`` entry separator. Nothing downstream checks that the range
matched anything -- ``gh release create -n ""`` succeeds -- so a heading the pattern cannot see
produces a published release with an EMPTY body and no error anywhere in the log.

That is not hypothetical here. The opening pattern read ``Release ONDEWO VTSI Client Python`` while
the ondewo-vtsi-api generator writes, and ``RELEASE.md`` uses, ``Release ONDEWO VTSI Python Client``
-- the same three words the other way round. Measured 2026-09-15 over all 31 published releases of
this client, body length against the wording of the matching heading: the 9 releases whose heading
uses the old ``Client Python`` wording (2.2.0, 2.3.0, 3.0.0-3.5.0 and 8.3.0) all have a NON-EMPTY
body of 44-668 bytes, and the 20 whose heading uses the generator's wording all have a body of
length 0, as do 4.0.0 and 6.3.1, which carry no entry at all. So the pattern was right for 3.5.0 and
older and went stale when the wording flipped at 5.0.0; 8.3.0 is the one entry written with the old
wording AFTER that flip, not -- as this file claimed until 2026-09-15 -- the only one in the file.
15 of the 37 headings still use it, and they are deliberately left alone.

These tests re-derive BOTH halves of the range from the ``Makefile`` rather than restating them, so
they cannot drift from the command that actually runs, and they fail when the current version's
slice is missing, unterminated, or nothing but its own heading. A parse that finds nothing raises
instead of silently inspecting an empty file -- an inspection of nothing must never read as a pass.
"""

import re
import shutil
import subprocess
from pathlib import Path
from typing import (
    List,
    Tuple,
)

import pytest

REPO_ROOT: Path = Path(__file__).resolve().parents[2]
MAKEFILE: Path = REPO_ROOT / "Makefile"
RELEASE_NOTES: Path = REPO_ROOT / "RELEASE.md"

# The version the release targets, as the Makefile spells it.
VERSION_RE: re.Pattern = re.compile(r"^ONDEWO_VTSI_VERSION=(?P<version>\S+)\s*$", re.MULTILINE)

# The perl range itself: `perl -ne 'print if /<start>/../<end>/'`. Neither half contains a slash,
# so a slash-delimited capture is unambiguous.
RANGE_RE: re.Pattern = re.compile(r"perl -ne 'print if /(?P<start>[^/]*)/\.\./(?P<end>[^/]*)/'")

# What the ondewo-vtsi-api release generator writes into this client's RELEASE.md, and greps for
# before deciding whether to insert its own boilerplate entry: `release_client` derives `Python`
# from the clone URL and emits `## Release ONDEWO VTSI Python Client <version>`.
GENERATOR_HEADING = "## Release ONDEWO VTSI Python Client {version}"

# The generator's OWN guard, transcribed from ondewo-vtsi-api's Makefile:
#     grep -qE "^#+ Release ONDEWO VTSI ${UPPER_REPO_NAME} Client ${ONDEWO_VTSI_API_VERSION}$$"
# It is ANCHORED at both ends, so a heading carrying trailing whitespace is invisible to it and the
# generator inserts a SECOND heading for the same version. This guard must therefore be at least as
# strict: comparing `line.strip()` would accept exactly the heading the generator cannot see, making
# the guard weaker than the thing it guards.
GENERATOR_GREP = r"^#+ Release ONDEWO VTSI Python Client {version}$"

# This guard's OWN notion of the entry separator, deliberately independent of the Makefile's
# terminator -- it is what the terminator is checked AGAINST, so deriving it from the Makefile would
# make the check circular.
SEPARATOR_RE: re.Pattern = re.compile(r"^\*{5,}$")

# The shape the terminator must NOT match: a markdown **bold** span inside an entry. Terminating on
# `/\*\*/` -- the bug ondewo-vtsi-api fixed in ab9158e -- truncates the notes at the first one of
# these, mid-sentence, with no error. Kept as a literal probe so this half of the property stays
# falsifiable even for a release entry that happens to contain no bold text at all.
BOLD_SPAN_PROBE = "and type `string` do not change and no `json_name` override is added**, so the change is"

# A generated boilerplate entry (heading, blank, `### Improvements`, blank, one bullet, blank,
# separator) is 7 lines, so the floor is deliberately below that: a bar of 10 would fail a release
# whose notes the generator wrote, which is legitimate and ships a ~250 byte body, not an empty one.
MINIMUM_SLICE_LINES = 5


def _read(path: Path) -> str:
    """
    Read a repository file, failing loudly when it is absent.

    Args:
        path (Path):
            Absolute path to the file to read.

    Returns:
        str:
            The file's text.

    Raises:
        AssertionError:
            When the file does not exist, so that a moved or renamed file fails the guard instead
            of making it vacuous.
    """
    assert path.is_file(), f"{path} does not exist -- this guard cannot inspect anything"
    return path.read_text(encoding="utf-8")


def _release_version() -> str:
    """
    Extract the version the Makefile releases.

    Returns:
        str:
            The value of the Makefile's version variable, e.g. ``8.7.0``.

    Raises:
        AssertionError:
            When the assignment is absent or spelled differently, which would otherwise leave every
            downstream assertion testing a made-up version.
    """
    match = VERSION_RE.search(_read(MAKEFILE))
    assert match is not None, "Makefile carries no `ONDEWO_VTSI_VERSION=<version>` assignment"
    return match.group("version")


def _release_notes_range() -> Tuple[str, str]:
    """
    Extract the two halves of the perl range the Makefile slices RELEASE.md with.

    Returns:
        Tuple[str, str]:
            The opening pattern (with the version variable already substituted) and the terminator.

    Raises:
        AssertionError:
            When no `perl -ne 'print if /.../../.../'` command is found in the Makefile.
    """
    match = RANGE_RE.search(_read(MAKEFILE))
    assert match is not None, "Makefile carries no release-notes `perl -ne 'print if /a/../b/'` range"
    start = match.group("start").replace("${ONDEWO_VTSI_VERSION}", _release_version())
    return start, match.group("end")


def _slice_release_notes(start: str, end: str) -> List[str]:
    """
    Reproduce perl's scalar range operator over RELEASE.md, line by line.

    ``..`` turns on when the left pattern matches and tests the right pattern on the SAME line, so
    the terminating line is included in the output -- which is why a released body ends with the
    ``*****`` separator.

    Args:
        start (str):
            The opening pattern, as a regular expression.
        end (str):
            The terminating pattern, as a regular expression.

    Returns:
        List[str]:
            The matched lines, newlines stripped.
    """
    start_re = re.compile(start)
    end_re = re.compile(end)
    collected: List[str] = []
    in_range = False
    for line in _read(RELEASE_NOTES).splitlines():
        if not in_range:
            if start_re.search(line):
                in_range = True
                collected.append(line)
                if end_re.search(line):
                    break
            continue
        collected.append(line)
        if end_re.search(line):
            break
    return collected


def _entry_separator_lines() -> List[str]:
    """
    Every ``*****`` entry separator in RELEASE.md, found WITHOUT the Makefile's terminator.

    Returns:
        List[str]:
            The separator lines, verbatim.

    Raises:
        AssertionError:
            When fewer than two are found, which would leave the terminator checks inspecting
            nothing -- an inspection of nothing must never read as a pass.
    """
    lines = [line for line in _read(RELEASE_NOTES).splitlines() if SEPARATOR_RE.match(line)]
    assert len(lines) >= 2, (
        f"RELEASE.md carries {len(lines)} `*****` entry separators; this guard cannot tell a working "
        "release-notes terminator from a broken one without them"
    )
    return lines


def _current_entry_body() -> List[str]:
    """
    The current version's entry, from its heading to the next separator, found WITHOUT the terminator.

    The Makefile's terminator is the thing under test here, so the entry is delimited by this
    module's own ``SEPARATOR_RE`` instead -- using the terminator to find the lines the terminator
    must not match would make the check circular.

    Returns:
        List[str]:
            The lines strictly between the version's heading and the next separator.

    Raises:
        AssertionError:
            When the heading is absent, when no separator follows it, or when the entry has no body.
    """
    version = _release_version()
    heading_re = re.compile(GENERATOR_GREP.format(version=re.escape(version)))
    lines = _read(RELEASE_NOTES).splitlines()

    opened = [index for index, line in enumerate(lines) if heading_re.match(line)]
    assert opened, f"RELEASE.md carries no anchored {GENERATOR_HEADING.format(version=version)!r} heading"

    rest = lines[opened[0] + 1 :]
    terminators = [index for index, line in enumerate(rest) if SEPARATOR_RE.match(line)]
    assert terminators, f"the {version} entry in RELEASE.md is not followed by a `*****` separator"

    body = rest[: terminators[0]]
    assert [line for line in body if line.strip()], f"the {version} entry in RELEASE.md has no body"
    return body


def test_the_release_notes_terminator_matches_every_entry_separator() -> None:
    """The terminator must END a slice: it has to match the separator lines RELEASE.md really carries."""
    _, end = _release_notes_range()
    end_re = re.compile(end)
    unmatched = [line for line in _entry_separator_lines() if not end_re.search(line)]
    assert not unmatched, (
        f"the release-notes terminator /{end}/ does not match {len(unmatched)} of the `*****` entry "
        f"separators in RELEASE.md, e.g. {unmatched[0]!r} -- the slice would run to the end of the "
        "file and the release body would carry every older entry too"
    )


def test_the_release_notes_terminator_matches_nothing_inside_an_entry() -> None:
    r"""The terminator must not fire EARLY: `/\*\*/` truncates at the first **bold** span in the entry."""
    _, end = _release_notes_range()
    end_re = re.compile(end)

    assert not end_re.search(BOLD_SPAN_PROBE), (
        f"the release-notes terminator /{end}/ matches a markdown **bold** span ({BOLD_SPAN_PROBE!r}), "
        "so it truncates the notes mid-entry -- the bug ondewo-vtsi-api fixed in ab9158e"
    )

    premature = [line for line in _current_entry_body() if end_re.search(line)]
    assert not premature, (
        f"the release-notes terminator /{end}/ matches {len(premature)} line(s) INSIDE the entry being "
        f"released, e.g. {premature[0]!r}, so the published body would stop there, mid-entry, with no error"
    )


def test_the_opening_pattern_matches_the_heading_the_api_generator_writes() -> None:
    """The slice must look for the heading ondewo-vtsi-api writes, not a locally invented one."""
    version = _release_version()
    start, _ = _release_notes_range()
    heading = GENERATOR_HEADING.format(version=version)
    assert re.search(start, heading), (
        f"the release-notes slice looks for /{start}/, which does not match the heading the "
        f"ondewo-vtsi-api generator writes and RELEASE.md uses: {heading!r}. An unmatched heading "
        "publishes a release with an EMPTY body and no error anywhere."
    )


def test_release_md_documents_the_version_being_released_exactly_once() -> None:
    """The curated entry must exist, and exist once -- the slice takes the FIRST match."""
    version = _release_version()
    heading = GENERATOR_HEADING.format(version=version)
    lines = _read(RELEASE_NOTES).splitlines()

    # Matched the way the generator matches it: the RAW line against an ANCHORED pattern. Comparing
    # `line.strip()` would pass a heading carrying trailing whitespace, which the generator's own
    # `grep -qE "...${VERSION}$"` cannot see -- so the guard would be weaker than the thing it guards.
    heading_re = re.compile(GENERATOR_GREP.format(version=re.escape(version)))
    headings = [line for line in lines if heading_re.match(line)]

    if not headings:
        untrimmed = [line for line in lines if heading_re.match(line.strip()) and line != line.strip()]
        assert not untrimmed, (
            f"RELEASE.md carries the {version} heading with trailing whitespace ({untrimmed[0]!r}). The "
            "perl slice would still match it, but the generator greps for an ANCHORED "
            f'"^#+ ... Client {version}$" and would not -- so it inserts a SECOND heading for the same '
            "version, burying this entry and tripping markdownlint MD024."
        )

    assert len(headings) == 1, (
        f"RELEASE.md carries {len(headings)} {heading!r} headings, expected exactly 1. None means "
        "an empty release body; two means the generator inserted its boilerplate on top of a "
        "curated entry, which buries it and trips markdownlint MD024."
    )


def test_the_current_versions_release_notes_slice_is_not_empty() -> None:
    """The exact slice the release publishes must carry real content and be terminated."""
    version = _release_version()
    start, end = _release_notes_range()
    lines = _slice_release_notes(start, end)

    assert lines, (
        f'the release-notes slice for {version} is EMPTY. `gh release create -n ""` would succeed '
        "and publish a release with no body at all."
    )
    assert re.search(start, lines[0]), f"the slice does not open on the {version} heading: {lines[0]!r}"
    assert re.search(end, lines[-1]), (
        f"the release-notes slice for {version} is UNTERMINATED -- it runs to the end of RELEASE.md, "
        "so the release body would carry every older entry too"
    )
    assert len(lines) >= MINIMUM_SLICE_LINES, (
        f"the release-notes slice for {version} is {len(lines)} lines, below the {MINIMUM_SLICE_LINES}-line "
        "floor: even the generated boilerplate entry is 7 lines"
    )

    body = [line for line in lines[1:-1] if line.strip()]
    assert body, f"the release-notes slice for {version} is a heading and a separator with nothing in between"


@pytest.mark.skipif(shutil.which("perl") is None, reason="perl is not installed")
def test_the_python_reimplementation_agrees_with_the_perl_the_makefile_runs() -> None:
    """Run the Makefile's own perl command, so this guard cannot drift from the real slice."""
    start, end = _release_notes_range()
    completed = subprocess.run(
        ["perl", "-ne", f"print if /{start}/../{end}/", str(RELEASE_NOTES)],
        capture_output=True,
        text=True,
        check=True,
    )
    assert completed.stdout.splitlines() == _slice_release_notes(start, end)
