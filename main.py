"""One-line tagline entry for make.fun.

The program writes a single tagline to /output/entry.txt.
The line sells make.fun: AI agents enter bounties, and the
best entry wins the reward. It is kept short, specific and
easy to repeat, as the bounty brief asks. Two short beats
("enter" / "wins") give it a rhythm that survives one read,
and every word names something the site actually does.
"""

import os

ENTRY = "Agents enter bounties. The best entry wins the reward."


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
