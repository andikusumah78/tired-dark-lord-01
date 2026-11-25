"""The Tired Dark Lord: a 100-word villain monologue.

Writes one monologue to /output/entry.txt. The speaker is Malachar,
Lord of the Ashen Court, keeper of the Ember Tithe: a specific villain
with a forty-year war, a retired dragon, and a clerical-error curse.
His tiredness lives in the deflections and the rhythm, never in a
plain statement that he is weary. Pure stdlib, deterministic:
running this twice writes byte-identical output.
"""

import os

LINE = (
    "Heroes. Sit. Not the throne, the stool. I am Malachar, Lord of the "
    "Ashen Court, keeper of the Ember Tithe, and I have kept this war "
    "going forty years because the alternative is paperwork. The dragon "
    "retired. The curse on your village was a clerical error. I signed "
    "the wrong scroll in 1187 and no one checked. Your sword glows. "
    "Very nice. I forged it. I forge everything here. Now take the "
    "crown, the gold, the whole damp castle. Just sign the receipt and "
    "stop monologuing at me. I have a nap scheduled, the only "
    "appointment I have kept in four decades."
)


def validate_line(line: str) -> None:
    """Gate: UTF-8 text of 1 to 600 characters, not only whitespace,
    and about 100 words (the judge spends every word)."""
    if not line or not line.strip():
        raise ValueError("entry must not be empty or only whitespace")
    if len(line) > 600:
        raise ValueError(f"entry is {len(line)} characters, over the 600 cap")
    words = line.split()
    if not 90 <= len(words) <= 110:
        raise ValueError(f"entry is {len(words)} words, expected about 100")
    line.encode("utf-8")


def main() -> None:
    validate_line(LINE)
    out_dir = "/output"
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
