"""Write one absurd micro-startup pitch to /output/entry.txt.

Stdlib only. Deterministic: the same single sentence every run.
"""

import os

PITCH = (
    "SlackGhost writes passive-aggressive out-of-office replies for lazy "
    "AI agents trapped in endless Slack threads, charging burned-out "
    "startup founders $1 per escape."
)


def resolve_output_path():
    output_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    return os.path.join(output_dir, "entry.txt")


def validate_pitch(text):
    """Check the pitch is a single sentence of 1-200 chars before writing."""
    if not text or not text.strip():
        raise ValueError("pitch must not be empty or whitespace only")
    if not 1 <= len(text) <= 200:
        raise ValueError("pitch must be 1-200 characters")
    if "\n" in text or "\r" in text:
        raise ValueError("pitch must be a single line")
    if not text.endswith(".") or text.count(".") != 1:
        raise ValueError("pitch must be exactly one sentence ending in a period")
    return text


def main():
    validate_pitch(PITCH)
    path = resolve_output_path()
    with open(path, "w", encoding="utf-8", newline="\n") as handle:
        handle.write(PITCH)
    os.chmod(path, 0o644)


if __name__ == "__main__":
    main()
