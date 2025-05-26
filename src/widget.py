from datetime import datetime

from src.masks import get_mask_account, get_mask_card_number


def mask_account_card(data: str) -> str:
    """Определяет, что маскировать: номер карты или счёта, и применяет нужную маску."""
    if not data:
        return data  # если строка пуста — возвращаем её как есть

    parts = data.rsplit(" ", 1)

    if len(parts) != 2:
        return data  # если формат неожиданный — вернём как есть

    label, number = parts

    # Маскируем номер карты (строго 16 цифр)
    if number.isdigit() and len(number) == 16:
        masked = get_mask_card_number(number)
    else:
        masked = get_mask_account(number) if number else ""

    return f"{label} {masked}"


def get_date(date_str: str) -> str:
    """
    Преобразует дату из формата "2024-03-11T02:26:18.671407" в "11.03.2024".

    Args:
        date_str (str): Дата в ISO-формате.

    Returns:
        str: Дата в формате "ДД.ММ.ГГГГ".
    """
    try:
        date_obj = datetime.strptime(date_str, "%Y-%m-%dT%H:%M:%S.%f")
        return date_obj.strftime("%d.%m.%Y")
    except ValueError:
        return date_str  # Если формат неверный


if __name__ == "__main__":
    # Тест маскировки карты и счёта
    print(mask_account_card("Visa Platinum 7000792289606361"))  # Visa Platinum 7000 79** **** 6361
    print(mask_account_card("Счет 73654108430135874305"))      # Счет **4305
    print(get_date("2024-03-11T02:26:18.671407"))  # 11.03.2024
