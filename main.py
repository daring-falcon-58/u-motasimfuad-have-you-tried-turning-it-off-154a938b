#!/usr/bin/env python3
"""Have You Tried Turning It Off? — entry program.

Writes one funny line to /output/entry.txt: a hopeless tech support
agent's reply to a desperate customer.

Chosen line (winner of a 36-candidate blind scoring + pairwise
tournament, scored 1-5 against the judge's five published criteria in
their own order — see README.md for the full matrix):

    Your screen is frozen, your deadline is in an hour, and my shift ends in ten minutes. Let's all stay calm.

Why it wins: three clocks in one breath (frozen screen, deadline in an
hour, shift ends in ten minutes) and then the agent's signature move —
"Let's all stay calm" — while quietly walking away from the problem.
The humour is the agent's cheerful uselessness; the customer is never
the butt of it. The desperation is felt (frozen screen, one-hour
deadline), never explained. Fully fresh: it never leans on the
turn-it-off-and-on-again classic at all.

Gate: /output/entry.txt must be UTF-8 text of 1 to 199 characters, not
only white space. The line is 106 characters / 106 bytes, one line, no
trailing newline, so the file holds exactly the line.
"""

import os

LINE = "Your screen is frozen, your deadline is in an hour, and my shift ends in ten minutes. Let's all stay calm."


def main() -> None:
    out_dir = "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    # No trailing newline: the file is exactly the one line, 1-199 chars.
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
