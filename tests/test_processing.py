from typing import Dict, List

import pytest

from src.processing import filter_by_state, sort_by_date


# Фикстура с данными
@pytest.fixture
def operations() -> List[Dict[str, str | int]]:
    return [
        {"id": 1, "state": "EXECUTED", "date": "2022-10-10T10:00:00"},
        {"id": 2, "state": "CANCELED", "date": "2022-09-15T09:00:00"},
        {"id": 3, "state": "EXECUTED", "date": "2022-10-11T08:00:00"},
        {"id": 4, "state": "PENDING", "date": "2022-10-09T12:00:00"},
    ]


# Тесты для filter_by_state
@pytest.mark.parametrize("state, expected_ids", [
    ("EXECUTED", [1, 3]),
    ("CANCELED", [2]),
    ("PENDING", [4]),
    ("UNKNOWN", []),
])
def test_filter_by_state(operations: List[Dict[str, str | int]], state: str, expected_ids: List[int]) -> None:
    result = filter_by_state(operations, state)
    result_ids = [op["id"] for op in result]
    assert result_ids == expected_ids


# Тест: пустой список
def test_filter_by_state_empty() -> None:
    assert filter_by_state([], "EXECUTED") == []


# Тесты для sort_by_date
def test_sort_by_date_descending(operations: List[Dict[str, str | int]]) -> None:
    result = sort_by_date(operations)
    dates = [op["date"] for op in result]
    assert dates == sorted(dates, reverse=True)


def test_sort_by_date_ascending(operations: List[Dict[str, str | int]]) -> None:
    result = sort_by_date(operations, reverse=False)
    dates = [op["date"] for op in result]
    assert dates == sorted(dates)


# Тест: одинаковые даты
def test_sort_by_date_same_dates() -> None:
    ops = [
        {"id": 1, "date": "2022-01-01T00:00:00"},
        {"id": 2, "date": "2022-01-01T00:00:00"},
    ]
    result = sort_by_date(ops)
    assert [op["id"] for op in result] == [1, 2]
