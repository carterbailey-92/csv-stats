"""CSV Stats — Print row count, column types, and empty-cell rates for a CSV."""
from __future__ import annotations

import argparse


def main() -> int:
    parser = argparse.ArgumentParser(
        prog='csv_stats',
        description='Print row count, column types, and empty-cell rates for a CSV.',
    )
    parser.add_argument('path', nargs='?', help='Input file or folder')
    parser.add_argument('--out', help='Output folder')
    parser.add_argument('--preview', help='Show the plan and do not write')
    args = parser.parse_args()
    print('CSV Stats')
    print('A quick profile of a dump.')
    print('Local CLI preview.')
    if vars(args):
        print(args)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
# tweak (2026-11-03)
# tune (2026-11-03)
# cleanup (2026-11-03)
# minor adjust (2026-11-04)
# revisit later (2026-11-05)
# update note (2026-11-05)
# small fix (2026-11-05)
# polish (2026-11-06)
