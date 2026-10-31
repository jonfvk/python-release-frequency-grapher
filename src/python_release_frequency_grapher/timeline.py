from datetime import datetime
from typing import List, Tuple, Optional

def determine_timeline_range(
    releases: List[Tuple[str, datetime]]
) -> Optional[Tuple[datetime, datetime]]:
    """
    Given a list of (version, datetime) tuples, return (start_date, end_date)
    where start_date is the earliest release date and end_date is the latest.
    Returns None if releases is empty.
    """
    if not releases:
        return None
    # Extract all dates
    dates = [dt for _, dt in releases]
    start = min(dates)
    end = max(dates)
    return (start, end)
