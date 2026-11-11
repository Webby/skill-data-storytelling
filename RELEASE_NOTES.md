# Data Storytelling — release 0.2.0

## What changed from v0.1

1. Refined the original BLOT/SCR concept with Minto's explicit SCQ reader-question stage, keeping the author's original framework intact.
2. Added an evidence-to-claim protocol for numbers, forecasts, uncertainty, causal language, source provenance, counterevidence, and privacy.
3. Made narrative structure conditional. Introduced an evidence-first path when no Hero's Journey, transformation arc, or literary plot is warranted.
4. Added Duarte's present-versus-possible contrast as an optional method for persuasive talks, not a substitute for substantiated forecasts.
5. Added visualization integrity, chart selection, and W3C/WCAG-aware accessibility guidance; kept the original 3–4 information blocks as a heuristic.
6. Clarified that scientific studies do not establish universal memory benefits from storytelling.
7. Added `research-crosswalk.md` with direct links, source types, limits, and mapping from each original guide section to v0.2 decisions.
8. Added a review rubric, four evidence hard gates, and 12 behavioral eval prompts (including negative controls).
9. Reduced unconditional skill context via topic-specific references and disabled no invocation mode (automatic discovery remains the default).
10. Improved installation: current user skill path (`~/.agents/skills`), explicit `--replace` upgrade, no backup or deletion of unrelated files, and a legacy option for older Codex setups.

## Distribution

- `data-storytelling-v0.2.0.zip`: only one root skill folder, for agents / API environments that accept a ZIP skill bundle.
- `data-storytelling-v0.2.0.tar.gz`: `install.sh` + root skill folder, for local Codex deployment.
- `data-storytelling/SKILL.md`: skill entrypoint.

The user-authored `HOW_TO_STORYTELLING.md` was copied byte-for-byte into `references/`; the v0.1 archive and directory are unchanged.

## Usage

Extract the tarball and run:

```bash
./install.sh --user
./install.sh --user --replace
./install.sh --repo /path/to/project
./install.sh --repo /path/to/project --replace
./install.sh --legacy-codex --replace
```

`--replace` intentionally removes an existing `data-storytelling` folder **only after** verifying its manifest name. It never creates a backup. Omit `--replace` to refuse accidental overwrite. Old v0.1 installations under `~/.codex/skills` are not automatically deleted or migrated when installing into `~/.agents/skills`.

**ChatGPT web:** a standalone local skill ZIP is not guaranteed to install directly in a web chat. Current OpenAI documentation differentiates filesystem/desktop skills from web-accessible skills bundled in plugins, and workspace/plugin creation depends on availability and permission. A valid ZIP skill is not itself a published ChatGPT plugin. Consult https://learn.chatgpt.com/docs/build-skills and https://learn.chatgpt.com/docs/build-plugins for the supported route.

## Validation scope

Package syntax, internal Markdown links, source-file identity, archive safety and installer behavior can be tested locally. End-to-end behavior, automatic invocation, and measured improvement over v0.1 require live agent runs; the bundled evaluation cases are **proposed**, not executed performance evidence.
