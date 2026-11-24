"""houseplant-out-of-office — The Houseplant Out-of-Office.

The line is an out-of-office auto-reply written by a houseplant, in
the plant's own voice. A monstera with 3 opinions about the window
and 0 about the sender's email: water it, then they will talk.
Concrete numbers (3 opinions, 0 opinions), plant voice, surprise,
punch and brevity. The line is 116 characters, inside the
120-character cap, with no dollar amount.
"""

import os

LINE = (
    "Out of office. I am a monstera with 3 opinions about the window "
    "and 0 about your email. Water me, then we will talk."
)


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(LINE + "\n")


if __name__ == "__main__":
    main()
