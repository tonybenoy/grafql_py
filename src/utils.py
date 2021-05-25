from typing import Any, Dict, List


def filter_by(data: List[Dict[str, Any]], key: str, val: str):
    if key.startswith('"') and key.endswith('"'):
        return [item for item in data if key.strip('"') == item[val]]
    words = [w.lower() for w in key.split(" ")]
    return [
        item for item in data if set(words) <= set(w.lower() for w in item[val].split())
    ]
