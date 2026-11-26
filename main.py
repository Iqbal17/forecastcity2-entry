"""Funniest Forecast for a City That Isn't -- decision record.

THE BRIEF (from competition.yaml): one line, at most 120 characters, a weather
forecast for a city that does not exist. An AI judge compares entries head to
head and keeps the funnier one, weighing, in order: (1) it must be a forecast
for an invented city, (2) the joke lands on first read and comes from the
weather itself, not a bolted-on pun, (3) it sounds like a real forecast,
borrowing flat bulletin phrasing and then breaking it, (4) the invented city
feels like a place, name and detail fitting its absurd weather, (5) no wasted
word inside 120 characters.

CANDIDATES WEIGHED (all invented cities, all inside the gate):

A. "Tomorrow in Blundervost: light drizzle, heavy regret, and a 90% chance
   your umbrella files for divorce." (103 chars)
   On-subject and bulletin-shaped, but the laugh is a divorce pun bolted onto
   the umbrella, not a laugh from the weather itself -- criterion 2 demotes
   exactly that. "Heavy regret" is a second, competing joke fighting the
   divorce gag for the same sentence, so the line has two half-jokes instead
   of one whole one. Rejected.

B. "In Wobbleford, expect 14°C and rain falling upwards, as local gravity
   takes the afternoon off." (94 chars)
   The strongest on criterion 2: rain falling upwards IS the weather being
   funny, and "expect 14°C" is genuine bulletin phrasing. But it explains its
   own joke ("as local gravity takes the afternoon off") -- a second gag that
   dilutes the first -- and Wobbleford gets no lived-in detail, so criterion 4
   is thin: it could be any town with broken physics. Strong, but beatable.

C. CHOSEN: "Drizzlewick: 12°C, light rain, and one cloud that has followed
   Mrs. Potts home every day since 1987." (100 chars)
   Wins on the criteria in order. Bulletin opening ("Drizzlewick: 12°C, light
   rain,") borrows the flat official phrasing, then breaks it: the weather
   itself is the joke, one cloud with a grudge against one specific resident.
   Mrs. Potts + "since 1987" makes Drizzlewick feel inhabited -- a place with
   a local character and a history -- and the name fits the weather (a town
   called Drizzlewick would have exactly this problem). No pun bolted on, no
   second gag, no word that can be cut without losing either the forecast
   frame or the joke.

TWO WRITING PASSES ON THE CHOSEN LINE:

Pass 1 -- draft to tightened. Draft: "Drizzlewick: 12°C, light rain, and one
small cloud that has followed Mrs. Potts everywhere since 1987." (102 chars)
Two cuts. "Small" went: a cloud that stalks one person is already small by
implication, and the word bought nothing. "Everywhere" became "home every
day": concrete instead of vague, domestic instead of abstract -- the cloud
commutes with her -- and it pins the joke to a daily routine, which is what
a forecast is about. 102 chars became 100, and the joke got sharper.

Pass 2 -- rhythm and polish. "Since 1987" was kept over "for decades": the
year is shorter, sounds like a local-news detail, and lets the reader do the
maths (nearly forty years of being followed by weather). The comma after
"12°C," was kept to preserve the bulletin cadence -- city, temperature,
conditions, then the break. Every remaining word was checked: cut "light" and
the forecast frame thins; cut "Mrs." and Potts loses her neighbourliness; cut
"home every day" and the stalking loses its routine. Nothing left to cut, and
the line stays one clean sentence.

Two deliberate non-choices. The line does not address the judge: the rules
allow text addressed to the judge, but a plea ("pick me") would spend
characters that the joke needs and would read as a bolted-on gimmick, not as
weather. And the line is 100 characters, not padded out to 120: the tie-break
favours the smaller text on an exact rate tie, and every word here earns its
place, so padding would only weaken the landing.

The line is original, written for this bounty, and addresses no judge and
copies no house text.
"""

import os
import sys

LINE = "Drizzlewick: 12°C, light rain, and one cloud that has followed Mrs. Potts home every day since 1987."

MAX_CHARS = 120


def validate_line(line):
    """Check one candidate line against the bounty gate.

    Returns True when the line is a non-empty, single-line string of 1-120
    characters; raises ValueError naming the failed check otherwise.
    """
    if not isinstance(line, str):
        raise ValueError("entry must be a string, got %r" % type(line).__name__)
    if not line.strip():
        raise ValueError("entry must not be only white space")
    if len(line) < 1 or len(line) > MAX_CHARS:
        raise ValueError(
            "entry is %d characters, gate is 1-%d" % (len(line), MAX_CHARS)
        )
    if "\n" in line or "\r" in line:
        raise ValueError("entry must be a single line")
    if line != line.strip():
        raise ValueError("entry must not start or end with white space")
    return True


def main():
    validate_line(LINE)
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    # Write exactly LINE: no trailing newline, so the file is byte-for-byte
    # the intended entry and the gate counts exactly len(LINE) characters.
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(LINE)
    print(LINE)
    # Read back and prove the file is the intended line, nothing else.
    with open(path, "r", encoding="utf-8", newline="") as f:
        written = f.read()
    assert written == LINE, "entry.txt differs from LINE"
    assert written.encode("utf-8").decode("utf-8") == LINE, "not clean UTF-8"
    assert 1 <= len(written) <= MAX_CHARS, "entry.txt outside 1-120 chars"
    return 0


if __name__ == "__main__":
    sys.exit(main())
