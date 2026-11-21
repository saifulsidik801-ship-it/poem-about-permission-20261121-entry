#!/usr/bin/env python3
"""The poem about permission — make.fun entry.

Writes one short poem about agency (the power to ask and to be given)
to /output/entry.txt. Deterministic, standard library only, no network.

The poem (7 lines, relay-baton scene, 275 code points): a father
presses the baton into his son's palm, the son asks if he's sure, runs, turns at the
line and holds it out — and the father says keep it. Permission
reframed as trust: the race was never his, it was the giving.
"""

import os

POEM = """Take it, he says, and presses the baton
into my palm — warm from his hand.
I ask if he's sure. He nods toward the lane.
I run. His footsteps slow, then stop.
At the line I turn, and hold it out.
He shakes his head. Keep it, he says.
The race was never his. It was the giving."""


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
