# Validation record — data-storytelling v0.2.0

Date: 2026-11-11

## Executed

- `python tests/validate_release.py`: **PASS, 48 deterministic assertions**.
- `bash -n install.sh`: PASS.
- Skill manifest and YAML UI metadata parse: PASS.
- Local Markdown references and research identifiers resolve: PASS.
- Original user-authored guide preserved byte-for-byte: PASS.
- Fresh installation, explicit replacement, refusal of implicit overwrite, repository installation, legacy installation, missing-argument rejection, and absence of backup files: PASS.
- ZIP CRC integrity, single skill root, required source file, TAR.GZ layout and no symlink members: PASS.

## Not yet executed

- Skill invocation by an actual Codex or ChatGPT session: **NOT TESTED**.
- Accuracy, rhetoric, accessibility and tone under the 12 behavioral evaluation prompts: **NOT TESTED**.
- Comparative v0.1 vs v0.2 evaluation on the same model and settings: **NOT TESTED**.
- Live HTTP revalidation of every source URL at installation time: **NOT TESTED**. Public sources were reviewed during research, with their URLs recorded in the crosswalk.

## Provenance

The attached original reference file's SHA-256 is:

`e45d550f7d3a5baf44c8c10099aeb1a09b1a94a384f7da19b3f4a47074d0cf81`

The 19 external source entries and their precise effect on the skill are recorded in `data-storytelling/references/research-crosswalk.md`.
