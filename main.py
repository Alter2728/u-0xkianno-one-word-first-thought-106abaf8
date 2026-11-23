"""Entry for make.fun's "One Word, First Thought" bounty.

Writes exactly one word to entry.txt in the output directory
(1-24 UTF-8 characters, not only white space, no newline).
The same bytes are written on every run.
"""

import os

# Draft: "petrichor" - the smell of earth after rain. Vivid and
# specific, but it is the first "interesting word" most word
# lovers reach for, so the field likely holds copies of it;
# byte-identical entries share one rate and the earlier receipt
# places first.
# Revised: "psithurism" - the sound of wind whispering through
# trees. Just as vivid, but rarer in the field, and the word
# itself sounds like what it names: a soft hush of consonants
# that rewards a second look. Chosen over apricity (winter-sun
# warmth, lovely but static) for that sound-meaning match.
WORD = "psithurism"


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(WORD)


if __name__ == "__main__":
    main()
