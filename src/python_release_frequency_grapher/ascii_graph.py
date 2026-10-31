from typing import Dict, Optional

def generate_ascii_bar_graph(
    counts: Dict[str, int],
    max_width: int = 40,
    bar_char: str = '#',
    label_width: Optional[int] = None,
) -> str:
    """
    Generate an ASCII bar graph from a dict of {label: count}.
    Bars are scaled to max_width.
    Returns the graph as a multiline string.
    """
    if not counts:
        return "(No data to display)"
    max_count = max(counts.values())
    if max_count == 0:
        scale = 0
    else:
        scale = max_width / max_count
    # Determine label width for alignment
    if label_width is None:
        label_width = max(len(str(label)) for label in counts)
    lines = []
    for label, count in counts.items():
        bar_len = int(round(count * scale)) if max_count > 0 else 0
        bar = bar_char * bar_len
        lines.append(f"{label.ljust(label_width)} | {bar} ({count})")
    return '\n'.join(lines)
