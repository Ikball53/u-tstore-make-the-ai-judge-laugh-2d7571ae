"""Make the AI Judge Laugh — one funny line, written cold, no setup."""

from pathlib import Path

# Deadpan dev joke: a first-try green test suite is so out of character
# that the only logical conclusion is mistaken authorship.
LINE = "My code passed all 47 tests on the first run, so I deleted it \u2014 someone else clearly wrote it."

OUTPUT_PATH = Path("/output/entry.txt")


def build_entry_text() -> str:
    line = LINE.strip()
    assert 1 <= len(line) <= 200, f"line must be 1-200 chars, got {len(line)}"
    assert "\n" not in line, "entry must be a single line"
    return line


def main() -> None:
    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_PATH.write_bytes(build_entry_text().encode("utf-8"))


if __name__ == "__main__":
    main()
