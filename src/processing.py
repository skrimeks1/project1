from datetime import datetime
from typing import Dict, List, Literal


def filter_by_state(
    operations: List[Dict],
    state: str = 'EXECUTED'
) -> List[Dict]:
    """Фильтрует операции по статусу. По умолчанию 'EXECUTED'."""
    return [op for op in operations if op.get('state') == state]


def sort_by_date(
    operations: List[Dict],
    reverse: bool = True
) -> List[Dict]:
    """Сортирует операции по дате. По умолчанию новые сначала."""
    return sorted(
        operations,
        key=lambda x: x['date'],
        reverse=reverse
    )

