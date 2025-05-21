def get_mask_card_number(card_number: str) -> str:
    """Маскирует номер карты.

    Пример:
    Вход: "1234567812345678"
    Выход: "1234 56 **** 5678"
    """
    if not card_number:
        return " **** "

    first_part = card_number[:4]
    middle_part = card_number[4:6]  # без "**"
    last_part = card_number[-4:] if len(card_number) > 6 else ""

    return f"{first_part} {middle_part} **** {last_part}".strip()


def get_mask_account(account_number: str) -> str:
    """Маскирует номер счета, показывая только последние 4 цифры (без **)"""
    if not account_number:
        return ""

    if len(account_number) < 4:
        return account_number

    return account_number[-4:]
