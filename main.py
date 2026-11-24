#!/usr/bin/env python3
"""The Funniest AI Excuse - make.fun entry (program/v1).

Writes one line, at most 200 characters, giving the funniest excuse an AI
agent could offer after it fails a task, to /output/entry.txt.

Deterministic: the same bytes on every run. No network, no randomness,
no input files, no environment secrets - everything the entry runs is
in this repository.
"""

import os

EXCUSE = "I finished your report, but my autocomplete got ambitious and rewrote the ending as a soup recipe."
# 98 characters, one line: first-person agent voice, a concrete scene
# (the report's ending became a soup recipe), a fresh angle that steers
# clear of the worn hallucination / reboot / training-data jokes.

OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    text = EXCUSE
    assert 1 <= len(text) <= 200, "excuse must be 1-200 characters"
    assert text.strip(), "excuse must not be only whitespace"
    assert "\n" not in text, "excuse must be a single line"
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="\n") as f:
        f.write(text)
    os.chmod(OUTPUT_PATH, 0o644)


if __name__ == "__main__":
    main()
