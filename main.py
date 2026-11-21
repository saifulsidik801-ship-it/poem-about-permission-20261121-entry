#!/usr/bin/env python3
"""The poem about permission — make.fun entry.

Writes one short poem about agency (the power to ask and to be given)
to /output/entry.txt. Deterministic, standard library only, no network.

The poem (7 lines, relay-baton image): agency is not the thing held,
it is the handing over — asked for, given, and taken back when the
asking stops.
"""

import os

POEM = """Take the baton — it is warm from my hand,
and yours only while you run.
Ask, and the lane opens;
stop asking, and it cools
in my palm again.
Power was never the thing held.
It was the handing over."""


def main() -> None:
    text = POEM.strip("\n")
    code_points = len(text)
    assert 1 <= code_points <= 280, f"poem is {code_points} code points"
    assert text.strip(), "poem must not be only whitespace"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(text)
    # Read back and verify: the file on disk must be exactly the poem.
    with open("/output/entry.txt", encoding="utf-8") as f:
        assert f.read() == text, "entry.txt differs from the poem"
    print(f"wrote /output/entry.txt ({code_points} code points)")


if __name__ == "__main__":
    main()
