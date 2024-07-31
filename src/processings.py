from datetime import datetime

incoming_list = [
    {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
    {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
    {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
    {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
]


def filter_by_state(name: list, state="EXECUTED") -> list:
    """Функция возвращает новый список словарей, содержащий только те словари, у которых ключ state соответствует указанному значению."""
    result_state = [state_key for state_key in name if state_key.get("state") == state]
    return result_state

def sort_by_date(result_state) -> list:
    """Функция сортирует список словарей по ключу date."""
    # Сортирует по дате убыванию

    sorted_date = sorted(result_state, key=lambda x: datetime.fromisoformat(x['date']), reverse=True)
    return sorted_date



filter_state = filter_by_state(incoming_list)
print(filter_state)

# print(filter_by_state(incoming_list))
# print(sort_by_date(sort_by_date))