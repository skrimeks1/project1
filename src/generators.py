from typing import Dict, Iterator, List


def filter_by_currency(transactions: List[Dict], currency: str) -> Iterator[Dict]:
    """
    Генератор, фильтрующий транзакции по заданной валюте.

    :param transactions: Список транзакций.
    :param currency: Код валюты (например, 'USD').
    :return: Итератор с транзакциями в указанной валюте.
    """
    for transaction in transactions:
        op_amount = transaction.get("operationAmount", {})
        curr = op_amount.get("currency", {}).get("code")
        if curr == currency:
            yield transaction


def transaction_descriptions(transactions: List[Dict]) -> Iterator[str]:
    """
    Генератор, возвращающий описание каждой транзакции.

    :param transactions: Список транзакций.
    :return: Итератор с описаниями.
    """
    for transaction in transactions:
        yield transaction.get("description", "Нет описания")


def card_number_generator(start: int, end: int) -> Iterator[str]:
    """
    Генератор номеров карт в формате 'XXXX XXXX XXXX XXXX'.

    :param start: Начальный номер (от 1).
    :param end: Конечный номер (до 9999_9999_9999_9999).
    :return: Итератор с отформатированными номерами.
    """
    for num in range(start, end + 1):
        card_num = f"{num:016d}"  # Дополняем нулями до 16 цифр
        yield f"{card_num[:4]} {card_num[4:8]} {card_num[8:12]} {card_num[12:16]}"
