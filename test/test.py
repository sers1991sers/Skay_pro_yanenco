cart = [
    "6831982476737658",
    "Maestro 1596837868705199",
    "Счет 64686473678894779589",
    "MasterCard 7158300734726758",
    "6831982476737658",
    "Счет 35383033474447895560",
    "Visa Classic 6831982476737658",
    "Visa Platinum 8990922113665229",
    "Visa Gold 5999414228426353",
    "Счет 73654108430135874305",
]

def get_mask_card_number(card_number: int) -> str:
    """Маскировки номера карты"""

    if len(card_number) != 16:
        return "Не верный формат ввода."

    masked_number = f"{card_number[:4]} {card_number[4:6]}** **** {card_number[-4:]}"
    return masked_number

def get_mask_account(number_account: int) -> str:
    """Маскировки номера счета"""
    for number in number_account:
        if number.isdigit():
            cel_number = f"{len(number_account[:-4]) * "*" + number_account[-4:]}"
            return cel_number
        else:
            return "Не верный формат ввода"

def mask_account_card(accaunt=None, check=None) -> str:
    """Маскировки номера счета"""
    account_list = []
    account_list_not_name = []

    if check:
        for i in check:
            masked = i[:5] + "**" + (i[8:])
            account_list.append(masked)
    if accaunt:
        for accoun in accaunt:
            masked = "**" + accoun[2:]
            account_list_not_name.append(masked)
    account_list.extend(account_list_not_name)
    return f"{account_list}"

number_account = "19899891283123"
print(get_mask_account(number_account))

card_number = "7000792289606361"
print(get_mask_card_number(card_number))

print(mask_account_card(cart))
