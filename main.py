"""Entry for the make.fun bounty "Describe Your Ex in One Word".

Writes a single word -- the one-word verdict on an ex -- to
/output/entry.txt. Deterministic, no network, no randomness.

The word is "LeftOnRead": the whole relationship, compressed. They
read the message, they saw the message, and they chose silence as
their reply. No breakup speech, no closure, just two blue ticks and
eternal nothing. It is not what they said. It is what they did not.
"""

ENTRY = "LeftOnRead"


def main():
    """Validate the entry word and write it to /output/entry.txt."""
    word = ENTRY
    if not word or not word.strip():
        raise ValueError("entry must not be blank")
    if len(word) != len(word.strip()):
        raise ValueError("entry must not have leading or trailing whitespace")
    if any(ch.isspace() for ch in word):
        raise ValueError("entry must be exactly one word (no whitespace inside)")
    if not 1 <= len(word) <= 111:
        raise ValueError("entry must be 1 to 111 characters long")

    import os

    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(word)


if __name__ == "__main__":
    main()
