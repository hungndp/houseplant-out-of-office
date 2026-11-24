"""houseplant-out-of-office — The Houseplant Out-of-Office.

The line is an out-of-office auto-reply written by a houseplant, in
the plant's own voice. A monstera with 3 opinions about the window
and 0 about the sender's email: water it, then they will talk.
Concrete numbers (3 opinions, 0 opinions), plant voice, surprise,
punch and brevity. The line is 116 characters, inside the
120-character cap, with no dollar amount.
"""

import os

SETUP = (
    "Out of office. I am a monstera with 3 opinions about the window "
    "and 0 about your email. "
)

PUNCH = "Water me, then we will talk."

LINE = SETUP + PUNCH

TERMINATOR = "\n"


def resolve_output_dir():
    """Return the output directory, defaulting to /output."""
    return os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")


def write_entry(out_dir, text):
    """Write the entry line to entry.txt inside out_dir."""
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(text + TERMINATOR)
    return path


def main() -> None:
    if not LINE.strip():
        raise ValueError("entry line is empty")
    out_dir = resolve_output_dir()
    write_entry(out_dir, LINE)


if __name__ == "__main__":
    main()
