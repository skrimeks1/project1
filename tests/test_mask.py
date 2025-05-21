import pytest

from src.widget import get_date, mask_account_card


@pytest.mark.parametrize("input_str, expected", [
    ("Visa Platinum 7000792289606361", "Visa Platinum 7000 79 **** 6361"),
    ("Счет 73654108430135874305", "Счет 4305"),
    ("Mastercard 1234", "Mastercard 1234"),
    ("Visa7000792289606361", "Visa7000792289606361"),
    ("", ""),
])
def test_mask_account_card(input_str: str, expected: str) -> None:
    assert mask_account_card(input_str) == expected


@pytest.mark.parametrize("input_str, expected", [
    ("2024-03-11T02:26:18.671407", "11.03.2024"),
    ("не_дата", "не_дата"),
])
def test_get_date(input_str: str, expected: str) -> None:
    assert get_date(input_str) == expected

