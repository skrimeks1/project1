from datetime import datetime
from typing import Dict, List, Literal


def filter_by_state(
    operations: List[Dict],
    state: Literal['EXECUTED', 'CANCELED'] = 'EXECUTED'
) -> List[Dict]:
    """
    Фильтрует список банковских операций по статусу.

    Args:
        operations: Список операций (каждая операция — словарь с ключом 'state').
        state: Статус для фильтрации. Допустимые значения: 'EXECUTED', 'CANCELED'.
               По умолчанию 'EXECUTED'.

    Returns:
        Список операций, отфильтрованных по статусу.

    Пример:
        operations = [{'id': 1, 'state': 'EXECUTED'}, {'id': 2, 'state': 'CANCELED'}]
        filter_by_state(operations)
        [{'id': 1, 'state': 'EXECUTED'}]
    """
    return [op for op in operations if op.get('state') == state]


def sort_by_date(
    operations: List[Dict],
    reverse: bool = True
) -> List[Dict]:
    """
    Сортирует операции по дате (от новых к старым по умолчанию).

    Args:
        operations: Список операций (каждая операция содержит ключ 'date' в формате ISO).
        reverse: Если True — сортировка по убыванию (новые сначала),
                 если False — по возрастанию.

    Returns:
        Список операций, отсортированных по дате.

    Пример:
        operations = [
        ...     {'date': '2023-01-01T00:00:00.000000'},
        ...     {'date': '2023-01-03T00:00:00.000000'}
        ... ]
        sort_by_date(operations)[0]['date']
        '2023-01-03T00:00:00.000000'
    """
    return sorted(
        operations,
        key=lambda x: datetime.strptime(x['date'], '%Y-%m-%dT%H:%M:%S.%f'),
        reverse=reverse
    )
