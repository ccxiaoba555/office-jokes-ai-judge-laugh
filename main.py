#!/usr/bin/env python3
"""Office Jokes entry for make.fun's "Make the AI Judge Laugh: Office Jokes".

Writes one original one-line joke about office life to /output/entry.txt.
The joke is a single line, 113 characters, well under the 200-character cap.

Deterministic: the same bytes on every run. No network, no randomness,
no input files, no environment secrets.
"""

import os
from pathlib import Path

JOKE = (
    "I hit reply-all to ask to be removed from the thread, "
    "and now forty colleagues are replying-all to agree with me."
)


def main() -> None:
    out_dir = Path(os.environ.get("OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "entry.txt").write_text(JOKE + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
