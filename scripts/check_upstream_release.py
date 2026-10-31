#!/usr/bin/env python3
# /// script
# requires-python = ">=3.10"
# dependencies = []
# ///
"""Check the copy of the Collections Ontology against its GitHub repository.

The schema renders the Collections Ontology (CO) 2.0, and
``src/collections/schema/upstream/collections.owl`` is a copy of CO's OWL
file. CO publishes no releases. The file lives on the master branch of
collections-ontology/collections-ontology, which last changed in 2019.
Four things can go wrong without any change in this repository:

- a commit lands on master, so the copy may fall behind;
- the copied file changes or goes, or the copy drifts from its pin;
- the file names another edition in its ``owl:versionInfo``;
- a licence appears, which may change what this repository may copy.

The commit, the copied file's git object hash and the edition are pinned
below. The script asks the GitHub API for the head of master, the licence
GitHub detects and the file tree at the head, and reads the file itself
from raw.githubusercontent.com at the head commit.

It prints a Markdown report, and exits 1 when:

- master no longer names the pinned commit;
- the copied file at the head differs from its pin, or is gone;
- the copy in this repository differs from its pin;
- the file names an edition other than the pinned one, or its header
  states a licence;
- GitHub detects a licence for the repository;
- a check could not finish, such as a refused, failed or cut-off request,
  or an answer larger than the script reads.

An ontology file the authors add beside the known ones is reported for
information only.

Text a server chose, such as a commit hash, a licence name or an error
message, is quoted as code in the report, so the issue the workflow opens
from it cannot mention anyone. Set ``GITHUB_TOKEN`` to raise the API rate
limit. The token goes to api.github.com alone, never on to a redirect.
Usage::

    python scripts/check_upstream_release.py [--report FILE]
"""

from __future__ import annotations

import argparse
import hashlib
import http.client
import json
import os
import re
import sys
import urllib.error
import urllib.request
from functools import cache
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
COPY = ROOT / "src" / "collections" / "schema" / "upstream"
REPOSITORY = "collections-ontology/collections-ontology"
API = f"https://api.github.com/repos/{REPOSITORY}"
RAW = f"https://raw.githubusercontent.com/{REPOSITORY}"
USER_AGENT = "lmodel-collections-watch"

# The most the script reads of one answer. The largest, the file tree, is
# about 30 kB, and the OWL file about 40 kB.
MAX_BYTES = 5_000_000

# The branch CO lives on, the commit the copy was taken from, and the
# edition its owl:versionInfo names, which is the schema header's
# `version`. Move them together, with PINNED_BLOB, the copy and the schema,
# when the copy is replaced.
PINNED_BRANCH = "master"
PINNED_COMMIT = "619e7b02646321174635fd04be658e338bf7d1d7"
PINNED_EDITION = "2.0"

# The repository's address, which is the schema header's `source`;
# tests/test_upstream.py holds the two equal.
PINNED_SOURCE = f"https://github.com/{REPOSITORY}"

# The copied file, by its path in the repository and in the copy, and its
# git object hash at PINNED_COMMIT. tests/test_upstream.py checks the copy
# against it offline.
PINNED_FILE = "collections.owl"
PINNED_BLOB = "4e19e4892212de2b1805923a7a69fa4ba8c1b424"

# The other ontology files at PINNED_COMMIT, which the copy leaves out on
# purpose: CO's alignments with other vocabularies and its Turtle examples.
# Only an ontology file the authors add beyond these is reported.
LEFT_OUT = frozenset(
    {
        "alignment.owl",
        "examples/fabio-and-lists-snip1.ttl",
        "examples/fabio-and-lists-snip2.ttl",
        "examples/fabio-and-lists-snip3.ttl",
        "examples/fabio-and-lists-snip4.ttl",
        "examples/ore-and-co-snip1.ttl",
        "examples/ore-and-co-snip2.ttl",
        "examples/ore-and-co-snip3.ttl",
        "examples/ore-and-co-snip4.ttl",
        "examples/ore-and-co-snip5.ttl",
        "examples/ore-and-co-snip6.ttl",
        "examples/persons-list-1.ttl",
    }
)
ONTOLOGY_FILE = re.compile(r"\.(owl|owx|rdf|ttl|n3|nt|jsonld)$")

COMMIT_HASH = re.compile(r"^[0-9a-f]{40}$")
ONTOLOGY_HEADER = re.compile(r"<owl:Ontology\b.*?</owl:Ontology>", re.S)
VERSION_INFO = re.compile(r"<owl:versionInfo\b[^>]*>\s*([^<]*?)\s*</owl:versionInfo>")
# A licence or rights statement in the ontology's header, in the forms
# ontologies commonly use.
LICENCE_STATEMENT = re.compile(
    r"<((?:dc|dcterms|dct|cc|schema|xhv):(?:rights|license|licence))\b[^>]*?"
    r"(?:rdf:resource=\"([^\"]*)\"[^>]*/>|>([^<]*)<)"
)


def _get(url: str) -> bytes:
    req = urllib.request.Request(
        url,
        headers={"Accept": "application/vnd.github+json", "User-Agent": USER_AGENT},
    )
    token = os.environ.get("GITHUB_TOKEN")
    if token and url.startswith(API + "/"):
        # urllib copies ordinary headers onto a redirect, so the token goes in
        # an unredirected one and reaches api.github.com alone.
        req.add_unredirected_header("Authorization", f"Bearer {token}")
    with urllib.request.urlopen(req, timeout=60) as resp:
        body = resp.read(MAX_BYTES + 1)
    if len(body) > MAX_BYTES:
        raise ValueError(f"the answer from {url} is larger than {MAX_BYTES} bytes")
    return body


def _code(text: object) -> str:
    """Text a server chose, such as a commit hash, as a code span, so it
    cannot mention a person or add a link in the issue."""
    return "`" + str(text).replace("`", "'") + "`"


def _blob_sha(data: bytes) -> str:
    """The git object hash of a file's bytes, as the trees API reports it."""
    return hashlib.sha1(b"blob %d\0" % len(data) + data).hexdigest()


@cache
def _head() -> str:
    """The commit the branch names, asked once. Anything but a commit hash
    is refused, since the hash goes into the addresses asked next."""
    sha = json.loads(_get(f"{API}/branches/{PINNED_BRANCH}"))["commit"]["sha"]
    if not isinstance(sha, str) or not COMMIT_HASH.match(sha):
        raise ValueError(f"the branch {PINNED_BRANCH} names {sha!r}, not a commit hash")
    return sha


def _tree(ref: str) -> dict[str, str]:
    """Every file of the repository at a commit, by path, with its object hash."""
    body = json.loads(_get(f"{API}/git/trees/{ref}?recursive=1"))
    if body.get("truncated"):
        raise OSError(f"the tree at {ref} is too large for one listing")
    return {e["path"]: e["sha"] for e in body["tree"] if e["type"] == "blob"}


def check_head() -> tuple[list[str], bool]:
    """Report whether master still names the pinned commit."""
    head = _head()
    if head != PINNED_COMMIT:
        return [
            f"- **{PINNED_BRANCH} now names commit {_code(head[:12])}, not the pinned "
            f"`{PINNED_COMMIT[:12]}`.** Read what the commits after it change, and "
            "move the pins once the copy and the schema follow them."
        ], True
    return [
        f"- {PINNED_BRANCH} names the pinned commit `{PINNED_COMMIT[:12]}`, "
        "from which the copy was taken."
    ], False


def check_licence() -> tuple[list[str], bool]:
    """Report whether GitHub detects a licence for the repository. It
    detected none at the pin, and answers 404 when it detects none."""
    try:
        found = (json.loads(_get(f"{API}/license")).get("license") or {}).get("spdx_id")
    except urllib.error.HTTPError as err:
        if err.code != 404:
            raise
        found = None
    if found:
        return [
            f"- **GitHub now detects the licence {_code(found)} for {REPOSITORY}.** "
            "Read what it allows, and update NOTICE, which records the licences "
            "of the project's Google Code archive."
        ], True
    return ["- Licence: none that GitHub detects, as at the pin."], False


def check_copy() -> tuple[list[str], bool]:
    """Report whether the copy is the pinned file, whether the head still
    holds that file unchanged, and any ontology file added beside it."""
    report, attention = [], False
    path = COPY / PINNED_FILE
    if not path.is_file():
        attention = True
        report.append(f"- **`{PINNED_FILE}` is missing from the copy.**")
    elif _blob_sha(path.read_bytes()) != PINNED_BLOB:
        attention = True
        report.append(
            f"- **The copy of `{PINNED_FILE}` differs from its pin `{PINNED_BLOB[:12]}`.** "
            "Restore it from the pinned commit, or move the pins with it."
        )
    else:
        report.append(f"- The copy of `{PINNED_FILE}` matches its pin byte for byte.")

    head = _head()
    tree = _tree(head)
    if PINNED_FILE not in tree:
        attention = True
        report.append(
            f"- **The head of {PINNED_BRANCH} no longer holds `{PINNED_FILE}`.** Find "
            "where CO's authors now publish it, and move the pins."
        )
    elif tree[PINNED_FILE] != PINNED_BLOB:
        attention = True
        report.append(
            f"- **The head of {PINNED_BRANCH} changes `{PINNED_FILE}` (object "
            f"{_code(tree[PINNED_FILE][:12])}).** Replace the copy with the file at "
            "that commit, move the pins here, and update the schema."
        )
    added = sorted(
        p
        for p in tree
        if ONTOLOGY_FILE.search(p) and p != PINNED_FILE and p not in LEFT_OUT
    )
    if added:
        report.append(
            f"- For information, {REPOSITORY} at {_code(head[:12])} also holds "
            + ", ".join(_code(p) for p in added)
            + ", which the copy neither holds nor leaves out on purpose."
        )
    return report, attention


def check_edition() -> tuple[list[str], bool]:
    """Report the edition the file at the head names, and any licence its
    header states."""
    head = _head()
    data = _get(f"{RAW}/{head}/{PINNED_FILE}")
    text = data.decode("utf-8", "replace")
    header = ONTOLOGY_HEADER.search(text)
    if not header:
        return [
            f"- **The check of the edition could not finish: `{PINNED_FILE}` at "
            f"{_code(head[:12])} has no owl:Ontology header.**"
        ], True
    report, attention = [], False
    if _blob_sha(data) != PINNED_BLOB:
        report.append(
            f"- `{PINNED_FILE}` at {_code(head[:12])} is not the pinned file; "
            "the copy check says how."
        )
    editions = VERSION_INFO.findall(header.group(0))
    if editions != [PINNED_EDITION]:
        attention = True
        shown = ", ".join(_code(e) for e in editions) or "no edition"
        report.append(
            f"- **`{PINNED_FILE}` names {shown} in owl:versionInfo, not "
            f"{PINNED_EDITION}.** Read what changed, and move the schema header's "
            "`version` with the pins."
        )
    else:
        report.append(f"- Edition: CO {PINNED_EDITION}, as pinned.")
    for prop, resource, literal in LICENCE_STATEMENT.findall(header.group(0)):
        attention = True
        report.append(
            f"- **The header of `{PINNED_FILE}` now states {_code(prop)} "
            f"{_code(resource or literal.strip())}.** Read what it allows, and update NOTICE."
        )
    return report, attention


# Each check, by the name the report gives it when it cannot finish.
CHECKS = (
    ("head", check_head),
    ("licence", check_licence),
    ("copy", check_copy),
    ("edition", check_edition),
)


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument(
        "--report", type=Path, help="Also write the Markdown report to this file"
    )
    args = parser.parse_args(argv)
    lines = [
        f"- Pinned: Collections Ontology {PINNED_EDITION}, `{PINNED_FILE}` at commit "
        f"`{PINNED_COMMIT[:12]}` of {PINNED_SOURCE}, copied to "
        "`src/collections/schema/upstream/`."
    ]
    attention = False
    for label, check in CHECKS:
        try:
            found, needs = check()
        # OSError covers a refused or failed request and a timeout,
        # HTTPException and EOFError a connection cut off mid-answer,
        # ValueError an answer that is not JSON, is too large or names no
        # commit, and LookupError, TypeError and AttributeError JSON of
        # another shape.
        except (
            OSError,
            http.client.HTTPException,
            EOFError,
            ValueError,
            LookupError,
            TypeError,
            AttributeError,
        ) as err:
            found = [f"- **The {label} check could not finish: {_code(err)}.**"]
            needs = True
        lines += found
        attention = attention or needs
    text = "\n".join(lines) + "\n"
    print(text, end="")
    if args.report:
        args.report.write_text(text, encoding="utf-8")
    return 1 if attention else 0


if __name__ == "__main__":
    sys.exit(main())
