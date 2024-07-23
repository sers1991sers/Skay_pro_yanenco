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


# исправить принемает только один аргумент строку, содержащию тип и номер карты или счёта
# accaunt=None, check=None


def mask_account_card(check: str) -> str:
    """Маскировки номера счета"""
    account_list = []
    account_list_not_name = []

    if check:
        for i in check:
            masked = i[:5] + "**" + (i[8:])
            account_list.append(masked)
        return account_list
    # if accaunt:
    #     for accoun in accaunt:
    #         masked = "**" + accoun[2:]
    #         account_list_not_name.append(masked)
    # account_list.extend(account_list_not_name)
    # return f"{account_list}"


print(mask_account_card(cart))
