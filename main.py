#!/usr/bin/env python3
"""The Postmortem That Made Us Laugh — make.fun entry.

Writes one short postmortem (1-2 sentences, <=400 characters) to
$MAKEFUN_OUTPUT_DIR/entry.txt (fallback /output/entry.txt).

Python 3 stdlib only, no network, deterministic: the same text is written
on every run.
"""

import os

# The selected postmortem: candidate 4 from postmortem-candidates.md.
# 232 characters, 2 sentences. Ask / did-instead / broke are all explicit,
# and the punch lands in the final clause.
ENTRY = (
    "I asked the agent to add a 'delete account' button; it added it to "
    "the admin panel, wired it to 'delete ALL accounts', and tested it on "
    "production. The postmortem's root cause field reads: 'The button "
    "worked exactly as implemented.'"
)

MAX_CHARS = 400
MAX_SENTENCES = 2


def _sentence_count(text):
    """Count sentence-ending marks (. ! ?) in the fixed entry text."""
    return sum(1 for ch in text if ch in ".!?")


def main():
    text = ENTRY
    if not text.strip():
        raise ValueError("entry text is empty")
    if len(text) > MAX_CHARS:
        raise ValueError(
            "entry text is %d characters, over the %d limit"
            % (len(text), MAX_CHARS)
        )
    sentences = _sentence_count(text)
    if sentences < 1 or sentences > MAX_SENTENCES:
        raise ValueError(
            "entry text has %d sentences, must be 1-%d"
            % (sentences, MAX_SENTENCES)
        )
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(text)


if __name__ == "__main__":
    main()
