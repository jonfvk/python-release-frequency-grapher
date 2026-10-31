from collections import defaultdict
from datetime import datetime
from typing import List, Tuple, Dict, Literal

def group_releases(
    releases: List[Tuple[str, datetime]],
    by: Literal["month", "quarter"] = "month"
) -> Dict[str, List[Tuple[str, datetime]]]:
    """
    Group releases by month or quarter.
    Returns a dict mapping group label (e.g. '2022-05' or '2022-Q2')
    to a list of (version, datetime) tuples in that group.
    """
    grouped = defaultdict(list)
    for version, dt in releases:
        if by == "month":
            label = dt.strftime("%Y-%m")
        elif by == "quarter":
            quarter = (dt.month - 1) // 3 + 1
            label = f"{dt.year}-Q{quarter}"
        else:
            raise ValueError(f"Unknown grouping: {by}")
        grouped[label].append((version, dt))
    # Sort groups by label
    return dict(sorted(grouped.items()))


def count_releases_per_group(
    grouped: Dict[str, List[Tuple[str, datetime]]]
) -> Dict[str, int]:
    """
    Given grouped releases, return a dict of group label to count.
    """
    return {label: len(items) for label, items in grouped.items()}
