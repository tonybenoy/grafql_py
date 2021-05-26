from typing import Any, Dict, List

import pendulum


def filter_by(data: List[Dict[str, Any]], key: str, val: str) -> List[Dict[str, Any]]:
    if key.startswith('"') and key.endswith('"'):
        return [item for item in data if key.strip('"') == item[val]]
    words = [w.lower() for w in key.split(" ")]
    return [
        item for item in data if set(words) <= set(w.lower() for w in item[val].split())
    ]


def datetime_parser(dct: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
    for item in dct:
        item["dateLastEdited"] = pendulum.parse(item["dateLastEdited"])
    return dct
