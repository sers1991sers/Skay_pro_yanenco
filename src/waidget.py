data = "2018-07-11T02:26:18.671407"


def get_data(date: str) -> str:
    """возвращает строку с датой в формате DD.MM.YYYY"""
    year, month, day = date[:10].split("-")
    return f"{day}.{month}.{year}"


print(get_data(data))
