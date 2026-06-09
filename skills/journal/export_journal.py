"""Journal export skill."""

from typing import List, Dict


def export_to_csv(entries: List[Dict[str, object]]) -> str:
    if not entries:
        return ""

    headers = list(entries[0].keys())
    lines = [",".join(headers)]
    for entry in entries:
        lines.append(",".join(str(entry.get(header, "")) for header in headers))
    return "
".join(lines)
