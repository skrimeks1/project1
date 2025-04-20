from datetime import datetime

from src.masks import get_mask_account, get_mask_card_number


def mask_account_card(account_info: str) -> str:
    """
    Маскирует номер карты или счета в строке формата "Visa Platinum 7000792289606361" или "Счет 73654108430135874305".

    Args:
        account_info (str): Строка с типом и номером карты/счета.

    Returns:
        str: Строка с замаскированным номером.
    """
    parts = account_info.split()
    if len(parts) < 2:
        return account_info

    account_type = " ".join(parts[:-1])
    number = parts[-1]

    if "счет" in account_type.lower():
        return f"{account_type} {get_mask_account(number)}"
    return f"{account_type} {get_mask_card_number(number)}"


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
    # Тест маскировки карты и счета
    print(mask_account_card("Visa Platinum 7000792289606361"))  # Visa Platinum 7000 79** **** 6361
    print(mask_account_card("Счет 73654108430135874305"))      # Счет **4305
    print(get_date("2024-03-11T02:26:18.671407"))  # 11.03.2024
