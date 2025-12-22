#!/usr/bin/env python3
"""
aggregate_scores.py

Reads a scoring CSV (same schema as reporting/scoring_sheet.csv) and prints:
- overall win counts/rates
- win counts by task_id
- primary_tag distribution
- average rubric ratings (if filled)

This is intentionally simple and transparent.
"""

from __future__ import annotations

import argparse
import csv
from collections import Counter, defaultdict
from pathlib import Path
from typing import Dict


def safe_float(x: str):
    try:
        return float(x)
    except Exception:
        return None


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument(
        "--scores",
        default="reporting/scoring_sheet_example.csv",
        help="Path to scoring CSV (default: reporting/scoring_sheet_example.csv)",
    )
    args = ap.parse_args()

    scores_path = Path(args.scores)
    if not scores_path.exists():
        raise FileNotFoundError(f"Scoring file not found: {scores_path}")

    overall_winner = Counter()
    by_task_winner: Dict[str, Counter] = defaultdict(Counter)
    primary_tags = Counter()

    dim_sums = Counter()
    dim_counts = Counter()
    dims = [
        "adherence_1to5",
        "temporal_1to5",
        "identity_1to5",
        "realism_1to5",
        "edit_precision_1to5",
    ]

    with scores_path.open("r", encoding="utf-8", newline="") as f:
        r = csv.DictReader(f)
        for row in r:
            task_id = (row.get("task_id") or "").strip() or "T?"
            winner = (row.get("winner") or "").strip() or "TBD"

            overall_winner[winner] += 1
            by_task_winner[task_id][winner] += 1

            tag = (row.get("primary_tag") or "").strip()
            if tag:
                primary_tags[tag] += 1

            for d in dims:
                v = safe_float((row.get(d) or "").strip())
                if v is not None:
                    dim_sums[d] += v
                    dim_counts[d] += 1

    total = sum(overall_winner.values())
    print(f"\nScoring file: {scores_path}")
    print(f"Total rows:   {total}")

    print("\nOverall winner counts:")
    for k, v in overall_winner.most_common():
        pct = (v / total * 100.0) if total else 0.0
        print(f"- {k}: {v} ({pct:.1f}%)")

    print("\nWinner counts by task:")
    for task_id in sorted(by_task_winner.keys()):
        c = by_task_winner[task_id]
        task_total = sum(c.values())
        summary = ", ".join([f"{k}={v}" for k, v in c.most_common()])
        print(f"- {task_id} (n={task_total}): {summary}")

    if primary_tags:
        print("\nPrimary tag distribution:")
        for k, v in primary_tags.most_common(10):
            print(f"- {k}: {v}")

    if any(dim_counts[d] > 0 for d in dims):
        print("\nAverage rubric ratings (if filled):")
        for d in dims:
            if dim_counts[d] > 0:
                avg = dim_sums[d] / dim_counts[d]
                print(f"- {d}: {avg:.2f} (n={dim_counts[d]})")

    print("\nNote: If winners/ratings are 'TBD', this is expected for dry-run artifacts.")


if __name__ == "__main__":
    main()
