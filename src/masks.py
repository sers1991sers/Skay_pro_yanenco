from typing import Any

cart = [
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


def get_mask_card_number(card_number: str) -> str:
    """Маскировки номера карты"""

    if card_number.isalpha():
        name = card_number[:4]
        print(name)

    else:
        masked_number = f"{card_number[:4]} {card_number[4:6]}** **** {card_number[-4:]}"
        return masked_number


# перенести в модуль waidget.py
def get_mask_account(number_account: str) -> str:
    """Маскировки номера счета"""
    for number in number_account:
        if number.isdigit():  #'*' * len(number_account[:-4])
            cel_number = f"{number_account[:-4]}{"*" * len(number_account[-4:])}"
        else:
            return "Не верный формат ввода"
    return cel_number


# исправить принемает только один аргумент строку, содержащию тип и номер карты или счёта
# accaunt=None, check=None
result: list[Any] = []


def mask_account_card(check: str) -> str:
    """сортировка  номеров карт, ссылается -> wiadget -> mask_account_cards()"""

    visa_cart = []
    name_account = ("Счёт")
    name_cart = ("Visa", "MasterCard", "Maestro", "Visa Gold")
    for cart_sort in cart:
        ren = ""

        if cart_sort.startswith(name_cart):
            visa_cart.append(cart_sort)
            if visa_cart:
                for i in visa_cart:
                    num = i[-16:]
                    ren += f"{i[:-16]} {num[:4]} {num[4:6]}** **** {num[-4:]} "
                    result.append(ren)

            if len(cart_sort) == 16 or name_account:
                get_mask_card_number(cart_sort)

    return result



# number_account = "19899891283123"
# print(get_mask_account(number_account))
# card_number = "Счет 64686473678894779589"
# print(get_mask_card_number(card_number))
# print(mask_account_card(cart))
