"""Checks the upstream watch's decisions against stubbed answers from GitHub.

scripts/check_upstream_release.py asks GitHub about the Collections
Ontology's repository. These tests replace its one network call, `_get`,
with a table of answers, so they run offline. They show what the report says
when master moves, the file changes or goes, the edition moves, a licence
appears, a file is added, or a check cannot finish.
"""

import http.client
import importlib.util
import json
import urllib.error
import urllib.request
from pathlib import Path

import pytest

ROOT = Path(__file__).parent.parent
SCRIPT = ROOT / "scripts" / "check_upstream_release.py"
COPY = ROOT / "src" / "collections" / "schema" / "upstream" / "collections.owl"
NEWER = "a" * 40


@pytest.fixture
def watch():
    """A fresh copy of the script, so no test sees another's cached answers."""
    spec = importlib.util.spec_from_file_location("watch_under_test", SCRIPT)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def _tree(watch, owl_sha=None, extra=()):
    """A tree listing that holds the pinned file, the files left out on
    purpose, a picture, and any `extra` paths."""
    entries = [{"path": "README.md", "type": "blob", "sha": "1" * 40}]
    if owl_sha is not False:
        entries.append(
            {
                "path": watch.PINNED_FILE,
                "type": "blob",
                "sha": owl_sha or watch.PINNED_BLOB,
            }
        )
    entries += [{"path": p, "type": "blob", "sha": "2" * 40} for p in watch.LEFT_OUT]
    entries.append(
        {"path": "images/Collections-Ontology-Bag.png", "type": "blob", "sha": "3" * 40}
    )
    entries.append({"path": "examples", "type": "tree", "sha": "4" * 40})
    entries += [{"path": p, "type": "blob", "sha": "5" * 40} for p in extra]
    return {"tree": entries, "truncated": False}


def _answers(watch, head=None, owl=None, tree=None, licence=None):
    """What GitHub answers, keyed by the address the script asks. By default
    nothing has changed since the pin and GitHub detects no licence."""
    head = head or watch.PINNED_COMMIT
    answers = {
        f"{watch.API}/branches/{watch.PINNED_BRANCH}": {"commit": {"sha": head}},
        f"{watch.API}/git/trees/{head}?recursive=1": tree or _tree(watch),
        f"{watch.RAW}/{head}/{watch.PINNED_FILE}": owl
        if owl is not None
        else COPY.read_bytes(),
    }
    if licence:
        answers[f"{watch.API}/license"] = {"license": {"spdx_id": licence}}
    return answers


def _stub(watch, answers):
    """Make `_get` answer from the table: an exception is raised, a missing
    address is a 404, bytes are returned as they are, and anything else as
    JSON."""

    def get(url):
        if url not in answers:
            raise urllib.error.HTTPError(url, 404, "Not Found", None, None)
        answer = answers[url]
        if isinstance(answer, Exception):
            raise answer
        if isinstance(answer, bytes):
            return answer
        return json.dumps(answer).encode()

    watch._get = get


def _run(watch, tmp_path):
    report = tmp_path / "report.md"
    code = watch.main(["--report", str(report)])
    return code, report.read_text(encoding="utf-8")


def test_nothing_changed(watch, tmp_path):
    """With master at the pin, the file unchanged and no licence, the watch
    reports each check and exits 0."""
    _stub(watch, _answers(watch))
    code, text = _run(watch, tmp_path)
    assert code == 0, text
    assert "- master names the pinned commit `619e7b026463`" in text
    assert "- Licence: none that GitHub detects, as at the pin." in text
    assert "- The copy of `collections.owl` matches its pin byte for byte." in text
    assert "- Edition: CO 2.0, as pinned." in text
    assert "For information" not in text


def test_master_moved(watch, tmp_path):
    """A commit on master needs attention, though the file is unchanged."""
    _stub(watch, _answers(watch, head=NEWER))
    code, text = _run(watch, tmp_path)
    assert code == 1
    assert (
        "**master now names commit `aaaaaaaaaaaa`, not the pinned `619e7b026463`.**"
        in text
    )
    assert "- Edition: CO 2.0, as pinned." in text


def test_the_file_changed(watch, tmp_path):
    """A changed file at the head needs attention, and so does the edition it names."""
    owl = COPY.read_bytes().replace(
        b">2.0</owl:versionInfo>", b">2.1</owl:versionInfo>"
    )
    _stub(
        watch, _answers(watch, head=NEWER, owl=owl, tree=_tree(watch, owl_sha="6" * 40))
    )
    code, text = _run(watch, tmp_path)
    assert code == 1
    assert (
        "**The head of master changes `collections.owl` (object `666666666666`).**"
        in text
    )
    assert "**`collections.owl` names `2.1` in owl:versionInfo, not 2.0.**" in text
    assert "is not the pinned file; the copy check says how." in text


def test_the_file_dropped(watch, tmp_path):
    """A head without the file needs attention."""
    answers = _answers(watch, head=NEWER, tree=_tree(watch, owl_sha=False))
    del answers[f"{watch.RAW}/{NEWER}/{watch.PINNED_FILE}"]
    _stub(watch, answers)
    code, text = _run(watch, tmp_path)
    assert code == 1
    assert "**The head of master no longer holds `collections.owl`.**" in text
    assert (
        "**The edition check could not finish: `HTTP Error 404: Not Found`.**" in text
    )


def test_the_copy_drifted(watch, tmp_path, monkeypatch):
    """A copy that differs from its pin, or is missing, needs attention."""
    monkeypatch.setattr(watch, "COPY", tmp_path)
    _stub(watch, _answers(watch))
    code, text = _run(watch, tmp_path)
    assert code == 1
    assert "**`collections.owl` is missing from the copy.**" in text

    (tmp_path / "collections.owl").write_bytes(COPY.read_bytes() + b"\n")
    code, text = _run(watch, tmp_path)
    assert code == 1
    assert (
        "**The copy of `collections.owl` differs from its pin `4e19e4892212`.**" in text
    )


def test_a_licence_appears(watch, tmp_path):
    """A licence GitHub detects, or one the header states, needs attention,
    and its name is quoted as code."""
    _stub(watch, _answers(watch, licence="@someone"))
    code, text = _run(watch, tmp_path)
    assert code == 1
    assert "**GitHub now detects the licence `@someone` for" in text

    owl = COPY.read_bytes().replace(
        b"<dc:language>en</dc:language>",
        b'<dc:language>en</dc:language>\n        <dcterms:license rdf:resource="https://creativecommons.org/licenses/by/4.0/"/>',
    )
    _stub(watch, _answers(watch, owl=owl))
    code, text = _run(watch, tmp_path)
    assert code == 1
    assert (
        "**The header of `collections.owl` now states `dcterms:license` "
        "`https://creativecommons.org/licenses/by/4.0/`.**"
    ) in text


def test_an_added_file_is_for_information(watch, tmp_path):
    """A new ontology file beside the known ones is reported but needs no
    attention by itself; a picture is not reported."""
    _stub(
        watch,
        _answers(watch, tree=_tree(watch, extra=["collections-3.0.owl", "new.png"])),
    )
    code, text = _run(watch, tmp_path)
    assert code == 0, text
    assert "also holds `collections-3.0.owl`, which the copy neither holds" in text
    assert "new.png" not in text


@pytest.mark.parametrize(
    "error, shown",
    [
        (
            urllib.error.URLError("Connection refused"),
            "`<urlopen error Connection refused>`",
        ),
        (http.client.IncompleteRead(b"partial"), "`IncompleteRead(7 bytes read)`"),
        (EOFError("cut off"), "`cut off`"),
        (
            ValueError("the answer is larger than 5000000 bytes"),
            "`the answer is larger",
        ),
    ],
)
def test_a_check_that_could_not_finish(watch, tmp_path, error, shown):
    """A refused, cut-off or oversized answer is a check that could not
    finish, and the report is still written."""
    answers = _answers(watch)
    answers[f"{watch.API}/branches/{watch.PINNED_BRANCH}"] = error
    _stub(watch, answers)
    code, text = _run(watch, tmp_path)
    assert code == 1
    assert f"**The head check could not finish: {shown}" in text
    assert "- Licence: none that GitHub detects, as at the pin." in text


@pytest.mark.parametrize(
    "branch",
    [
        {},  # LookupError: no commit
        {"commit": None},  # TypeError: not an object
        {"commit": {"sha": "../../evil"}},  # ValueError: not a hash
    ],
)
def test_an_answer_of_another_shape(watch, tmp_path, branch):
    """An answer without a commit hash where one belongs stops the checks
    that need it, and no address is built from it."""
    answers = _answers(watch)
    answers[f"{watch.API}/branches/{watch.PINNED_BRANCH}"] = branch
    _stub(watch, answers)
    code, text = _run(watch, tmp_path)
    assert code == 1
    for label in ("head", "copy", "edition"):
        assert f"**The {label} check could not finish:" in text
    assert "evil/" not in text


def test_the_token_goes_to_the_api_alone(watch, monkeypatch):
    """The token is an unredirected header, sent to api.github.com and never
    to the raw file host."""
    seen = []

    class Answer:
        def __enter__(self):
            return self

        def __exit__(self, *exc):
            return False

        def read(self, size):
            return b"{}"

    def urlopen(req, timeout):
        seen.append(req)
        return Answer()

    monkeypatch.setenv("GITHUB_TOKEN", "secret")
    monkeypatch.setattr(watch, "_open", urlopen)
    watch._get(f"{watch.API}/license")
    watch._get(f"{watch.RAW}/{watch.PINNED_COMMIT}/{watch.PINNED_FILE}")
    watch._get("https://api.github.com.example.org/repos")
    api, raw, lookalike = seen
    assert api.unredirected_hdrs == {"Authorization": "Bearer secret"}
    assert "Authorization" not in api.headers
    assert not raw.unredirected_hdrs and "Authorization" not in raw.headers
    assert not lookalike.unredirected_hdrs


def test_an_oversized_answer_is_refused(watch, monkeypatch):
    """An answer larger than MAX_BYTES is refused, not read in full."""

    class Answer:
        def __enter__(self):
            return self

        def __exit__(self, *exc):
            return False

        def read(self, size):
            return b"x" * size

    monkeypatch.setattr(watch, "_open", lambda req, timeout: Answer())
    with pytest.raises(ValueError, match="larger than"):
        watch._get(f"{watch.API}/license")


def test_a_redirect_off_github_is_refused(watch):
    """A redirect is followed to GitHub's two hosts over https, and to no
    other address."""
    handler = watch._GitHubRedirect()
    req = urllib.request.Request(f"{watch.API}/license")
    for newurl in (
        "https://example.org/license",
        "http://api.github.com/repos/x",
        "https://api.github.com.example.org/repos/x",
    ):
        with pytest.raises(ValueError, match="leads off GitHub"):
            handler.redirect_request(req, None, 302, "Found", {}, newurl)
    moved = "https://api.github.com/repositories/1/license"
    assert (
        handler.redirect_request(req, None, 301, "Moved", {}, moved).full_url == moved
    )


def test_server_text_stays_on_one_line(watch, tmp_path):
    """A licence name with a blank line and a mention in it stays inside its
    code span, so the issue mentions no one."""
    _stub(watch, _answers(watch, licence="MIT\n\n@someone `x`"))
    code, text = _run(watch, tmp_path)
    assert code == 1
    assert "**GitHub now detects the licence `MIT @someone 'x'` for" in text


def test_a_refused_licence_check(watch, tmp_path):
    """An error other than GitHub's 404 for no licence is a check that could
    not finish."""
    answers = _answers(watch)
    answers[f"{watch.API}/license"] = urllib.error.HTTPError(
        f"{watch.API}/license", 403, "Forbidden", None, None
    )
    _stub(watch, answers)
    code, text = _run(watch, tmp_path)
    assert code == 1
    assert (
        "**The licence check could not finish: `HTTP Error 403: Forbidden`.**" in text
    )


def test_a_truncated_tree(watch, tmp_path):
    """A tree listing GitHub cut short stops the copy check."""
    _stub(watch, _answers(watch, tree={"tree": [], "truncated": True}))
    code, text = _run(watch, tmp_path)
    assert code == 1
    assert "**The copy check could not finish: `the tree at" in text
    assert "- Edition: CO 2.0, as pinned." in text


def test_a_file_without_an_ontology_header(watch, tmp_path):
    """A file at the head with no owl:Ontology header, or with no edition in
    it, needs attention."""
    owl = COPY.read_bytes()
    start, end = owl.index(b"<owl:Ontology"), owl.index(b"</owl:Ontology>")
    _stub(watch, _answers(watch, owl=owl[:start] + owl[end + 15 :]))
    code, text = _run(watch, tmp_path)
    assert code == 1
    assert "has no owl:Ontology header.**" in text

    no_edition = owl.replace(
        b'<owl:versionInfo rdf:datatype="&xsd;string">2.0</owl:versionInfo>', b""
    )
    _stub(watch, _answers(watch, owl=no_edition))
    code, text = _run(watch, tmp_path)
    assert code == 1
    assert "**`collections.owl` names no edition in owl:versionInfo, not 2.0.**" in text
