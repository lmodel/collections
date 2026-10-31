---
type: Playbook
id: https://w3id.org/lmodel/collections/knowledge/playbooks/knowledge-sources
genre: reference
title: Knowledge sources map
description: "The librarian's scrape map: every repository location and external page this bundle derives concepts from, the concepts each yields, how to re-check each on a refresh run, and the paths left out on purpose."
resource: .
sources:
  - resource: README.md
  - resource: docs/about.md
  - resource: docs/index.md
  - resource: src/collections/schema
  - resource: src/collections_linkml/datamodel
  - resource: project.justfile
  - resource: .lokf/collections.yaml
  - resource: .lokf/justfile
  - resource: .lokf/pyproject.toml
  - resource: NOTICE
  - resource: LICENSE
  - resource: scripts/check_upstream_release.py
  - resource: .github/scripts
  - resource: .github/workflows
  - resource: .github/dependabot.yml
  - resource: .github/release
  - resource: justfile
  - resource: config.public.mk
  - resource: .linkml/generators.yaml
  - resource: .linkmllint.yaml
  - resource: project
  - resource: docs/schema
  - resource: docs/elements
  - resource: tests
  - resource: CONTRIBUTING.md
  - resource: .releaserc.json
  - resource: CHANGELOG.md
  - resource: website
  - resource: SECURITY.md
  - resource: AI_COVENANT.md
  - resource: .github/PULL_REQUEST_TEMPLATE
exclusions:
  - resource: .github/ISSUE_TEMPLATE
    reason: Issue forms, which are governance text and state nothing about the schema.
  - resource: .github/pull_request_template.md
    reason: The pull request checklist, which repeats CONTRIBUTING.md.
  - resource: CODE_OF_CONDUCT.md
    reason: The Contributor Covenant, governance text with nothing about the schema.
  - resource: uv.lock
    reason: The package's lock file, tooling that pins versions.
  - resource: pyproject.toml
    reason: Package metadata and spell checkers' settings; config.public.mk and the changelog state the package's name.
  - resource: .gitignore
    reason: "Tooling: the files git ignores."
  - resource: .editorconfig
    reason: "Tooling: editor settings."
  - resource: .yamllint.yaml
    reason: "Tooling: the YAML linter's settings."
  - resource: .markdownlint-cli2.jsonc
    reason: "Tooling: the Markdown linter's settings."
  - resource: lychee.toml
    reason: "Tooling: the link checker's settings."
  - resource: .pre-commit-config.yaml
    reason: "Tooling: the pre-commit hooks and the generated and copied files they leave alone."
  - resource: .copier-answers.yml
    reason: The copier template's answers, which `just update` reads.
  - resource: src/README.md
    reason: Text from the project template.
  - resource: docs/templates-linkml
    reason: The template's placeholders for gen-doc, not pages.
  - resource: examples
    reason: Text from the project template about generated example output.
  - resource: src/collections_linkml/__init__.py
    reason: Package plumbing.
  - resource: src/collections_linkml/_version.py
    reason: Package plumbing.
  - resource: tests/__init__.py
    reason: Test plumbing.
  - resource: llms.txt
    reason: The pointer that sends agents to this bundle.
  - resource: knowledge_bundle
    reason: The sidecar's link to the bundle.
  - resource: .lokf/lokf.yaml
    reason: LOKF's schema, pinned by the sidecar.
  - resource: .lokf/scripts
    reason: The sidecar's scripts, which the weekly sync replaces.
  - resource: .lokf/m365
    reason: The sidecar's Copilot skill builder and its instructions.
  - resource: .lokf/README.md
    reason: The sidecar's own README.
  - resource: .lokf/queries.http
    reason: The sidecar's sample queries.
  - resource: .lokf/ingest.yaml.sample
    reason: The sidecar's example ingest manifest, which this host does not use.
  - resource: .lokf/uv.lock
    reason: The sidecar's lock file.
  - resource: .lokf/.gitignore
    reason: The sidecar's git settings.
  - resource: .lokf/.gitattributes
    reason: The sidecar's git settings.
generated:
  by: process:ktl-librarian
  at: "2026-10-31T12:56:19Z"
status: draft
---

# Knowledge sources

A refresh run checks these sources again instead of finding them anew. Update this table whenever a source of the repository's knowledge moves, appears or goes.

Each concept derived from a file or folder of this repository names it by its path from the repository root, in `resource` and in `sources`. `knowledge-report.sh worklist` lists the concepts whose source moved since their stamp. It never fetches a page, so re-read the external pages this table names when the upstream watch reports a change.

| Source | Yields | Re-check by |
| --- | --- | --- |
| `src/collections/schema/collections.yaml`, `.linkmllint.yaml` | `datasets/collections-linkml-schema`, the four `glossary/` terms | re-read the header, each class's slots and the slots' ranges, IRIs and comments |
| `project.justfile`, `.lokf/collections.yaml`, `.lokf/justfile`, `.lokf/pyproject.toml` | the domain-schema section of `datasets/collections-linkml-schema` | re-read the `--root` list, the copy's notes, the `schema :=` line and the `[tool.lokf]` table |
| `src/collections/schema/upstream/collections.owl`, NOTICE | `datasets/collections-ontology-copy` | re-read the header and the pins NOTICE names |
| `scripts/check_upstream_release.py`, `.github/scripts/` | `playbooks/update-upstream-pins`, `workflows/upstream-watch` | re-read the pins, the docstring and the issue title |
| `README.md`, `docs/about.md`, `docs/index.md` | `explanations/names-and-iris`, `explanations/scope-and-rules`, `playbooks/validate-data` | re-read each section |
| `justfile`, `config.public.mk`, `.linkml/generators.yaml`, `project/`, `src/collections_linkml/datamodel/`, `docs/schema/`, `docs/elements/` | `datasets/generated-artefacts` | re-read the recipes, the variables and the settings; re-list `project/*/` |
| `tests/` | `datasets/test-data` | re-count `valid/`, `invalid/` and `problem/invalid/`; re-read the tests and the neighbours' checksums |
| `CONTRIBUTING.md`, the `lint`, `gen-project`, `gen-doc` and `test` recipes | `playbooks/regenerate-and-test` | confirm the setup, the checklist and the recipes |
| `.releaserc.json`, `.github/scripts/changelog-release.mjs`, `CHANGELOG.md`, `.github/release/` | `playbooks/release`, `workflows/semantic-release` | re-read the release rules, the baseline paragraph and the pinned tools |
| the nine files in `.github/workflows/`, `.github/PULL_REQUEST_TEMPLATE/` | the nine `workflows/` concepts | re-read each file's `on` keys, its jobs' permissions and Environments, and the variables it reads |
| `website/` | `services/documentation-site` | re-read `site.config.mjs` and `website/README.md` |
| `NOTICE`, `LICENSE`, `website/NOTICE`, the License section of `README.md` | `policies/license-and-attribution` | re-read each third-party entry |
| `SECURITY.md`, `.github/dependabot.yml` | `policies/security-policy` | re-read the table of surfaces and the settings not yet in force |
| `AI_COVENANT.md` | `policies/ai-covenant` | re-read the project note and the section on agent automation |
| <https://github.com/collections-ontology/collections-ontology>, <https://doi.org/10.3233/SW-130121>, the Google Code archive's project record | `references/collections-ontology` | re-read them when the upstream watch reports a change |

The paths under `exclusions` are left out, each for the reason it gives: governance text, tooling settings, template text, package plumbing, the pointer for agents, and the sidecar's own files.
