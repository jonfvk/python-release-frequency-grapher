import re
from datetime import datetime
from typing import List, Tuple, Optional

# Regular expressions for common changelog/version formats
# Example: '## [1.2.3] - 2023-05-01' or 'v1.2.3 (2023-05-01)'
RE_PATTERNS = [
    re.compile(r"^##?\s*\[?(v?\d+\.\d+(?:\.\d+)?)[^\d]*(\d{4}-\d{2}-\d{2})\]?", re.IGNORECASE),
    re.compile(r"^##?\s*\[?(v?\d+\.\d+(?:\.\d+)?)[^\d]*(\d{2}/\d{2}/\d{4})\]?", re.IGNORECASE),
    re.compile(r"^(v?\d+\.\d+(?:\.\d+)?)[^\d]*(\d{4}-\d{2}-\d{2})", re.IGNORECASE),
    re.compile(r"^(v?\d+\.\d+(?:\.\d+)?)[^\d]*(\d{2}/\d{2}/\d{4})", re.IGNORECASE),
]

DATE_FORMATS = [
    "%Y-%m-%d",
    "%d/%m/%Y",
]

def parse_changelog_lines(lines: List[str]) -> List[Tuple[str, datetime]]:
    """
    Parse changelog lines and extract (version, date) pairs.
    Returns a list of (version, datetime) tuples.
    Ignores lines that do not match known patterns.
    """
    results = []
    for line in lines:
        line = line.strip()
        for pat in RE_PATTERNS:
            m = pat.match(line)
            if m:
                version = m.group(1)
                date_str = m.group(2)
                dt = _parse_date(date_str)
                if dt:
                    results.append((version, dt))
                break
    return results

def _parse_date(date_str: str) -> Optional[datetime]:
    for fmt in DATE_FORMATS:
        try:
            return datetime.strptime(date_str, fmt)
        except ValueError:
            continue
    return None

def parse_changelog_file(path: str) -> List[Tuple[str, datetime]]:
    """
    Parse a changelog or version history file and extract (version, date) pairs.
    """
    with open(path, encoding="utf-8") as f:
        lines = f.readlines()
    return parse_changelog_lines(lines)
