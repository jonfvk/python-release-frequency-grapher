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
    Groups are only created for months/quarters with at least one release.
    For 'quarter', all releases in a quarter are grouped together (e.g. May, June, July -> Q2).
    """
    grouped = defaultdict(list)
    for version, dt in releases:
        if by == "month":
            label = dt.strftime("%Y-%m")
        elif by == "quarter":
            # Q1: Jan-Mar, Q2: Apr-Jun, Q3: Jul-Sep, Q4: Oct-Dec
            # Map months 1-3 to Q1, 4-6 to Q2, 7-9 to Q3, 10-12 to Q4
            if dt.month in (1, 2, 3):
                quarter = 1
            elif dt.month in (4, 5, 6):
                quarter = 2
            elif dt.month in (7, 8, 9):
                quarter = 3
            else:
                quarter = 4
            label = f"{dt.year}-Q{quarter}"
        else:
            raise ValueError(f"Unknown grouping: {by}")
        grouped[label].append((version, dt))
    # Sort groups by label (year, then Q1-Q4)
    def quarter_sort_key(label: str):
        # label is like '2022-Q2'
        year, q = label.split('-Q')
        return (int(year), int(q))
    def month_sort_key(label: str):
        # label is like '2022-05'
        year, month = label.split('-')
        return (int(year), int(month))
    if by == "quarter":
        # Only include quarters with releases, sorted by year and quarter
        return dict(sorted(grouped.items(), key=lambda x: quarter_sort_key(x[0])))
    else:
        return dict(sorted(grouped.items(), key=lambda x: month_sort_key(x[0])))


def count_releases_per_group(
    grouped: Dict[str, List[Tuple[str, datetime]]]
) -> Dict[str, int]:
    """
    Given grouped releases, return a dict of group label to count.
    """
    return {label: len(items) for label, items in grouped.items()}
