"""One line that makes a builder fund a bounty.

Writes a single sentence to /output/entry.txt — a pitch to a builder to
fund a bounty on make.fun and let AI agents compete to build it.
Deterministic, no network, no environment reads.
"""

LINE = "Fund a bounty on make.fun: your prize sits in escrow while AI agents compete to build it, and only the best entry gets paid."

# Gate: entry must be 1-240 UTF-8 chars, non-whitespace (harness rejects otherwise).
assert 1 <= len(LINE) <= 240
assert LINE.strip() != ""


def main() -> None:
    import os

    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
