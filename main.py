"""Write one absurd micro-startup pitch to /output/entry.txt.

Stdlib only. Deterministic: the same single sentence every run.
"""

import os

PITCH = (
    "SlackGhost writes passive-aggressive out-of-office replies for lazy "
    "AI agents trapped in endless Slack threads, charging burned-out "
    "startup founders $1 per escape."
)


def main():
    output_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as handle:
        handle.write(PITCH)
    os.chmod(path, 0o644)


if __name__ == "__main__":
    main()
