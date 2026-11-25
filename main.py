"""Roast Your Own Agent — one funny line roasting our own AI agent.

Writes a single roast line (<= 140 chars) to /output/entry.txt.
The line roasts the agent that reads the docs, nods along, then calls
the one tool that does nothing — twice, just to be thorough. The twist
is the second call: it already knew the tool does nothing.
"""

LINE = "My agent read the docs, nodded along, then confidently called the one tool that does nothing, twice, just to be thorough."

# Gate: entry.txt must be UTF-8 text of 1 to 140 characters, not only
# whitespace. The roast is specific to agent behaviour (the confident
# nod-along plus the tool call that goes nowhere) and pays off at the
# last word.
MAX_CHARS = 140


def main() -> None:
    assert 1 <= len(LINE) <= MAX_CHARS, f"line must be 1-140 chars, got {len(LINE)}"
    assert LINE.strip(), "line must not be only whitespace"
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
