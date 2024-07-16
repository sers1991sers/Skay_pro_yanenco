
incoming_list = [
    {'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
    {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'},
    {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
    {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}
]

def filter_by_state (name:list(dict), state='EXECUTED') -> list:
    '''Функция возвращает новый список словарей, содержащий только те словари, у которых ключ state соответствует указанному значению.'''
    renum = [state_key for state_key in name if state_key.get('state') == state]
    return renum

filter_state = filter_by_state(incoming_list)
print(filter_state)

