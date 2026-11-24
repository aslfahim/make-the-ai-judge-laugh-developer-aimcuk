#!/usr/bin/env python3
"""Write one funny single-line developer excuse to /output/entry.txt.

Concept: STALE CACHE - the fix deployed hours ago, but the cache is
still serving a version from 2019 out of pure spite.
"""

import os

LINE = (
    "I shipped the fix hours ago; the cache is still serving the 2019 "
    "build out of spite \u2014 I cleared it twice and it took it personally, "
    "so now we wait."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
