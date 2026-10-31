# Playbooks

* [Regenerate and test](regenerate-and-test.md) - How to change the schema: install with `uv sync --group dev`, edit `src/collections/schema/collections.yaml`, run `just lint`, `just gen-project`, `just gen-doc`, `just lokf-adapt` and `just test`, and commit the regenerated files.
* [Validate data](validate-data.md) - How to check a collection, set, bag or list file against the schema with `linkml-validate`, and which of CO's rules only `tests/test_data.py` checks.
* [Update the upstream pins](update-upstream-pins.md) - What to do when the upstream watch reports a new commit on CO's master branch, a changed or dropped `collections.owl`, another edition in `owl:versionInfo`, or a licence: replace the copy, move the pins in `scripts/check_upstream_release.py` and the schema header together, and run the tests.
* [Release](release.md) - How a release is made: write `## [Unreleased]` in CHANGELOG.md, merge a `feat:`, `fix:` or `security:` change, and semantic-release tags it from the `v0.0.0` baseline, the first release being 0.1.0, after which Knowledge Release attaches the schema copy and the bundle.
* [Knowledge sources map](knowledge-sources.md) - The librarian's scrape map: every repository location and external page this bundle derives concepts from, the concepts each yields, how to re-check each on a refresh run, and the paths left out on purpose.
