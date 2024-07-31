from src.masks import cart, mask_account_card

data = "2018-07-11T02:26:18.671407"


def get_data(date: str) -> str:
    """возвращает строку с датой в формате DD.MM.YYYY"""
    year, month, day = date[:10].split("-")
    return f"{day}.{month}.{year}"


def mask_account_cards(check: str) -> str:
    """Маскировки номера карты """
    if check:
        for i in check:
            return mask_account_card(i)
        # if len(i) == 16:
        #     return mask_account_card(i)


# get_mask_card_number()
# print(get_data(data))
# get_mask_account()
# print(mask_account_cards(cart))
