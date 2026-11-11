#!/usr/bin/env python3
"""Validate the standalone skill and its local installation package."""

import hashlib
import os
import re
import subprocess
import tarfile
import tempfile
import zipfile
from pathlib import Path

import yaml


# Define the release tree and the byte-for-byte source reference.
releaseDir = Path(__file__).resolve().parents[1]
skillDir = releaseDir / "data-storytelling"
archiveDir = releaseDir.parent
originalGuide = Path("/mnt/data/HOW_TO_STORYTELLING(1).md")
checks = []


# Record each deterministic assertion by name.
def expect(checkName, condition):
    if not condition:
        raise AssertionError(checkName)
    checks.append(checkName)


# Parse the exact YAML frontmatter from SKILL.md.
def readFrontmatter():
    content = (skillDir / "SKILL.md").read_text(encoding="utf-8")
    match = re.match(r"\A---\n(.*?)\n---\n", content, flags=re.S)
    expect("frontmatter-present", match is not None)
    return yaml.safe_load(match.group(1))


# Ensure local Markdown links point to bundled, existing files.
def validateLinks():
    fileCount = 0
    linkCount = 0
    for docPath in skillDir.rglob("*.md"):
        fileCount += 1
        document = docPath.read_text(encoding="utf-8")
        for link in re.findall(r"\[[^]]+\]\(([^)]+)\)", document):
            if link.startswith(("https://", "http://", "mailto:")):
                continue
            target = (docPath.parent / link.split("#")[0]).resolve()
            expect(f"link-{linkCount}", target.is_file() and target.is_relative_to(skillDir))
            linkCount += 1
    expect("markdown-files-present", fileCount >= 6)
    expect("internal-links-present", linkCount >= 10)


# Check source identity, source IDs, and skill metadata.
def validateSkill():
    metadata = readFrontmatter()
    expect("skill-name", metadata["name"] == "data-storytelling")
    expect("meaningful-description", "evidence" in metadata["description"])
    expect("no-unsupported-top-level-metadata", sorted(metadata) == ["description", "name"])
    agentInfo = yaml.safe_load((skillDir / "agents/openai.yaml").read_text())
    expect("agent-ui-match", agentInfo["interface"]["display_name"] == "Data Storytelling")
    if originalGuide.is_file():
        sourceBytes = originalGuide.read_bytes()
        packagedBytes = (skillDir / "references/HOW_TO_STORYTELLING.md").read_bytes()
        expect("original-preserved-byte-for-byte", sourceBytes == packagedBytes)
    crosswalk = (skillDir / "references/research-crosswalk.md").read_text()
    registered = set(re.findall(r"\*\*R(\d{2})\s+—", crosswalk))
    mentioned = set(re.findall(r"\[R(\d{2})\]", crosswalk))
    expect("research-sources-complete", registered == {f"{i:02d}" for i in range(1, 20)})
    expect("crosswalk-references-resolve", mentioned <= registered)
    validateLinks()


# Run the installer with isolated HOME/CODEX_HOME and capture its status.
def runInstall(sandboxHome, *arguments):
    environment = os.environ.copy()
    environment["HOME"] = str(sandboxHome)
    environment["CODEX_HOME"] = str(sandboxHome / "legacyCodex")
    return subprocess.run(
        [str(releaseDir / "install.sh"), *arguments],
        check=False,
        text=True,
        capture_output=True,
        env=environment,
    )


# Exercise create, refusal, explicit upgrade, and repository installation.
def validateInstaller():
    syntax = subprocess.run(["bash", "-n", str(releaseDir / "install.sh")], check=False)
    expect("bash-syntax", syntax.returncode == 0)
    with tempfile.TemporaryDirectory(prefix="story-skill-test-") as sandbox:
        home = Path(sandbox)
        target = home / ".agents/skills/data-storytelling"
        expect("install-user", runInstall(home, "--user").returncode == 0)
        expect("install-user-file", (target / "SKILL.md").is_file())
        expect("reject-implicit-overwrite", runInstall(home, "--user").returncode != 0)
        expect("upgrade-explicit", runInstall(home, "--user", "--replace").returncode == 0)
        other = target / "unrelated-file.txt"
        other.write_text("must disappear on requested upgrade")
        expect("upgrade-removes-old-custom-file", runInstall(home, "--user", "--replace").returncode == 0 and not other.exists())
        repo = home / "repo"
        expect("install-repo", runInstall(home, "--repo", str(repo)).returncode == 0)
        expect("repo-target", (repo / ".agents/skills/data-storytelling/SKILL.md").is_file())
        expect("install-legacy", runInstall(home, "--legacy-codex").returncode == 0)
        expect("legacy-target", (home / "legacyCodex/skills/data-storytelling/SKILL.md").is_file())
        expect("missing-repo-rejected", runInstall(home, "--repo").returncode != 0)
        expect("no-backups", not list(home.rglob("*.bak")) and not list(home.rglob("*~")))


# Ensure tarball and ZIP have the intended safe layouts and no forbidden symlinks.
def validateArchives():
    zipPath = archiveDir / "data-storytelling-v0.2.0.zip"
    tarPath = archiveDir / "data-storytelling-v0.2.0.tar.gz"
    with zipfile.ZipFile(zipPath) as archive:
        zipNames = archive.namelist()
        expect("zip-integrity", archive.testzip() is None)
        expect("zip-root", all(name.startswith("data-storytelling/") for name in zipNames))
        expect("zip-entrypoint", "data-storytelling/SKILL.md" in zipNames)
        expect("zip-source", "data-storytelling/references/HOW_TO_STORYTELLING.md" in zipNames)
    with tarfile.open(tarPath, "r:gz") as archive:
        tarNames = archive.getnames()
        expect("tar-root", "data-storytelling/SKILL.md" in tarNames)
        expect("tar-installer", "install.sh" in tarNames)
        expect("tar-no-symlinks", all(item.isfile() or item.isdir() for item in archive))
        expect("tar-source", "data-storytelling/references/HOW_TO_STORYTELLING.md" in tarNames)


# Execute the deterministic release validation suite.
def main():
    validateSkill()
    validateInstaller()
    validateArchives()
    digest = hashlib.sha256((skillDir / "references/HOW_TO_STORYTELLING.md").read_bytes()).hexdigest()
    print(f"PASS: {len(checks)} release assertions")
    print(f"Original guide SHA-256: {digest}")
    print("Behavioral agent evals: NOT RUN (see references/evaluation-cases.md)")


if __name__ == "__main__":
    main()
