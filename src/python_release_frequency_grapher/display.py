from typing import List, Tuple, Literal, Optional
from datetime import datetime
from . import parser, grouping, ascii_graph


def display_ascii_release_graph(
    releases: List[Tuple[str, datetime]],
    group_by: Literal["month", "quarter"] = "month",
    max_width: int = 40,
    bar_char: str = '#',
    label_width: Optional[int] = None,
    title: Optional[str] = None,
) -> None:
    """
    Display an ASCII bar graph of release frequency in the terminal.
    Args:
        releases: List of (version, datetime) tuples.
        group_by: 'month' or 'quarter'.
        max_width: Max width of the bar.
        bar_char: Character for the bar.
        label_width: Width for the group label.
        title: Optional title to print above the graph.
    """
    if title:
        print(title)
    if not releases:
        print("(No release data to display)")
        return
    grouped = grouping.group_releases(releases, by=group_by)
    counts = grouping.count_releases_per_group(grouped)
    graph = ascii_graph.generate_ascii_bar_graph(counts, max_width=max_width, bar_char=bar_char, label_width=label_width)
    print(graph)
