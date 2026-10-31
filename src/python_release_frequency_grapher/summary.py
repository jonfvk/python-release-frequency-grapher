from typing import Dict, Optional, List
import math


def mean(values: List[int]) -> Optional[float]:
    """
    Compute the mean (average) of a list of integers.
    Returns None if the list is empty.
    """
    if not values:
        return None
    return sum(values) / len(values)


def median(values: List[int]) -> Optional[float]:
    """
    Compute the median of a list of integers.
    Returns None if the list is empty.
    """
    n = len(values)
    if n == 0:
        return None
    sorted_vals = sorted(values)
    mid = n // 2
    if n % 2 == 1:
        return float(sorted_vals[mid])
    else:
        return (sorted_vals[mid - 1] + sorted_vals[mid]) / 2


def summarize_release_frequencies(
    counts: Dict[str, int]
) -> Dict[str, Optional[float]]:
    """
    Given a dict of {group_label: count}, compute summary statistics:
    - mean: average number of releases per group
    - median: median number of releases per group
    Returns a dict with keys 'mean' and 'median'.
    """
    values = list(counts.values())
    return {
        'mean': mean(values),
        'median': median(values),
    }


def format_summary_statistics(stats: Dict[str, Optional[float]]) -> str:
    """
    Format summary statistics as a human-readable string.
    """
    lines = []
    mean_val = stats.get('mean')
    median_val = stats.get('median')
    if mean_val is not None:
        lines.append(f"Mean releases per group:   {mean_val:.2f}")
    else:
        lines.append("Mean releases per group:   N/A")
    if median_val is not None:
        lines.append(f"Median releases per group: {median_val:.2f}")
    else:
        lines.append("Median releases per group: N/A")
    return '\n'.join(lines)
