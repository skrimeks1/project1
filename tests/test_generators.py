import pytest

from src.generators import card_number_generator, filter_by_currency, transaction_descriptions


@pytest.fixture
def sample_transactions():
    return [
        {
            "id": 939719570,
            "state": "EXECUTED",
            "date": "2018-06-30T02:08:58.425572",
            "operationAmount": {
                "amount": "9824.07",
                "currency": {
                    "name": "USD",
                    "code": "USD"
                }
            },
            "description": "Перевод организации",
            "from": "Счет 75106830613657916952",
            "to": "Счет 11776614605963066702"
        },
        {
            "id": 873106923,
            "state": "EXECUTED",
            "date": "2019-03-23T01:09:46.296404",
            "operationAmount": {
                "amount": "43318.34",
                "currency": {
                    "name": "руб.",
                    "code": "RUB"
                }
            },
            "description": "Перевод со счета на счет",
            "from": "Счет 44812258784861134719",
            "to": "Счет 74489636417521191160"
        }
    ]


def test_filter_by_currency(sample_transactions):
    # Тест на фильтрацию USD
    usd_txs = list(filter_by_currency(sample_transactions, "USD"))
    assert len(usd_txs) == 1
    assert usd_txs[0]["id"] == 939719570

    # Тест на фильтрацию RUB
    rub_txs = list(filter_by_currency(sample_transactions, "RUB"))
    assert len(rub_txs) == 1
    assert rub_txs[0]["id"] == 873106923

    # Тест на отсутствующую валюту
    eur_txs = list(filter_by_currency(sample_transactions, "EUR"))
    assert len(eur_txs) == 0


def test_transaction_descriptions(sample_transactions):
    descriptions = list(transaction_descriptions(sample_transactions))
    assert descriptions == ["Перевод организации", "Перевод со счета на счет"]


def test_card_number_generator():
    # Тест генерации 3 номеров
    cards = list(card_number_generator(1, 3))
    assert cards == [
        "0000 0000 0000 0001",
        "0000 0000 0000 0002",
        "0000 0000 0000 0003"
    ]

    # Тест формата номера
    card = next(card_number_generator(9999_9999_9999_9996, 9999_9999_9999_9996))
    assert card == "9999 9999 9999 9996"
